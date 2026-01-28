#!/usr/bin/env python3
"""
Convert Markdown files with annotations to DOCX format with vertical Chinese text.
Annotations become proper Word footnotes with colors preserved.
"""

import os
import re
import sys
import glob
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import qn


def hex_to_rgb(hex_color):
    """Convert hex color to RGBColor."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return RGBColor(r, g, b)


def parse_markdown_with_annotations(md_content):
    """
    Parse markdown content and extract text with annotations.
    Returns: (title, paragraphs) where each paragraph has text and annotations.
    """
    title = ""
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        title = re.sub(r'[《》]', '', title)
    
    content_match = re.search(r'\{%\s*capture\s+main_text\s*%\}(.*?)\{%\s*endcapture\s*%\}', 
                               md_content, re.DOTALL)
    
    if not content_match:
        paragraphs_raw = re.findall(r'<p>(.*?)</p>', md_content, re.DOTALL)
        if not paragraphs_raw:
            return title, []
    else:
        content = content_match.group(1)
        paragraphs_raw = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
    
    paragraphs = []
    
    for para_html in paragraphs_raw:
        para_html = para_html.strip()
        if not para_html:
            continue
            
        segments = []
        
        fn_pattern = r'\{%\s*include\s+fn\.html\s+(.*?)\s*%\}'
        
        last_end = 0
        for match in re.finditer(fn_pattern, para_html):
            if match.start() > last_end:
                text_before = para_html[last_end:match.start()]
                text_before = re.sub(r'<[^>]+>', '', text_before).strip()
                if text_before:
                    segments.append({'type': 'text', 'content': text_before})
            
            attrs_str = match.group(1)
            label = re.search(r'label="([^"]*)"', attrs_str)
            color = re.search(r'color="([^"]*)"', attrs_str)
            text = re.search(r'text="([^"]*)"', attrs_str)
            
            label_val = label.group(1) if label else '注'
            color_val = color.group(1) if color else '#267CB9'
            text_val = text.group(1) if text else ''
            
            if text_val:
                segments.append({
                    'type': 'footnote',
                    'label': label_val,
                    'color': color_val,
                    'text': text_val
                })
            
            last_end = match.end()
        
        if last_end < len(para_html):
            remaining = para_html[last_end:]
            remaining = re.sub(r'<[^>]+>', '', remaining).strip()
            if remaining:
                segments.append({'type': 'text', 'content': remaining})
        
        if not segments:
            plain_text = re.sub(r'<[^>]+>', '', para_html).strip()
            if plain_text:
                segments.append({'type': 'text', 'content': plain_text})
        
        if segments:
            paragraphs.append(segments)
    
    return title, paragraphs


def set_vertical_text_direction(section):
    """Set section to use vertical text direction (top-to-bottom, right-to-left)."""
    sectPr = section._sectPr
    
    text_direction = parse_xml(
        r'<w:textDirection w:val="tbRl" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'
    )
    sectPr.append(text_direction)


def create_vertical_docx(title, paragraphs, output_path):
    """Create a DOCX file with vertical Chinese text and proper Word footnotes."""
    doc = Document()
    
    section = doc.sections[0]
    section.page_width = Cm(29.7)
    section.page_height = Cm(21.0)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    
    set_vertical_text_direction(section)
    
    if title:
        title_para = doc.add_paragraph()
        title_run = title_para.add_run(title)
        title_run.font.size = Pt(22)
        title_run.font.bold = True
        title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph()
    
    for para_segments in paragraphs:
        para = doc.add_paragraph()
        
        for segment in para_segments:
            if segment['type'] == 'text':
                run = para.add_run(segment['content'])
                run.font.size = Pt(14)
            elif segment['type'] == 'footnote':
                color = hex_to_rgb(segment['color'])
                color_hex = segment['color'].lstrip('#')
                label_text = f"【{segment['label']}】"
                
                try:
                    para.add_footnote(label_text + segment['text'])
                    
                    footnote_ref = para._element.xpath('.//w:footnoteReference')
                    if footnote_ref:
                        last_ref = footnote_ref[-1]
                        parent_run = last_ref.getparent()
                        if parent_run is not None:
                            rPr = parent_run.find(qn('w:rPr'))
                            if rPr is None:
                                rPr = parse_xml(r'<w:rPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
                                parent_run.insert(0, rPr)
                            color_elem = parse_xml(
                                f'<w:color w:val="{color_hex}" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'
                            )
                            rPr.append(color_elem)
                    
                    footnotes_part = doc.part.footnotes_part
                    if footnotes_part is not None:
                        footnotes_xml = footnotes_part._element
                        all_footnotes = footnotes_xml.findall('.//' + qn('w:footnote'))
                        if all_footnotes:
                            last_footnote = all_footnotes[-1]
                            runs = last_footnote.findall('.//' + qn('w:r'))
                            label_len = len(label_text)
                            char_count = 0
                            for run_elem in runs:
                                t_elem = run_elem.find(qn('w:t'))
                                if t_elem is not None and t_elem.text:
                                    text_in_run = t_elem.text
                                    if char_count < label_len:
                                        overlap = min(len(text_in_run), label_len - char_count)
                                        if overlap > 0:
                                            rPr = run_elem.find(qn('w:rPr'))
                                            if rPr is None:
                                                rPr = parse_xml(r'<w:rPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
                                                run_elem.insert(0, rPr)
                                            existing_color = rPr.find(qn('w:color'))
                                            if existing_color is not None:
                                                rPr.remove(existing_color)
                                            color_elem = parse_xml(
                                                f'<w:color w:val="{color_hex}" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'
                                            )
                                            rPr.append(color_elem)
                                    char_count += len(text_in_run)
                except Exception as e:
                    run = para.add_run(f'[{segment["label"]}]')
                    run.font.size = Pt(10)
                    run.font.superscript = True
                    run.font.color.rgb = color
    
    doc.save(output_path)
    return output_path


def convert_md_to_docx(md_path, output_dir=None):
    """Convert a single markdown file to DOCX."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    title, paragraphs = parse_markdown_with_annotations(md_content)
    
    if not paragraphs:
        print(f"  Skipping {md_path}: No content found")
        return None
    
    if output_dir is None:
        output_dir = os.path.dirname(md_path)
    
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.docx")
    
    create_vertical_docx(title, paragraphs, output_path)
    return output_path


def convert_all_md_files(source_dir='pages', output_dir='output_docx'):
    """Convert all markdown files in the source directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    md_files = glob.glob(os.path.join(source_dir, '**', '*.md'), recursive=True)
    
    converted = []
    for md_path in md_files:
        print(f"Converting: {md_path}")
        try:
            result = convert_md_to_docx(md_path, output_dir)
            if result:
                converted.append(result)
                print(f"  -> {result}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\nConverted {len(converted)} files to {output_dir}/")
    return converted


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--all':
            source = sys.argv[2] if len(sys.argv) > 2 else 'pages'
            output = sys.argv[3] if len(sys.argv) > 3 else 'output_docx'
            convert_all_md_files(source, output)
        else:
            for md_file in sys.argv[1:]:
                result = convert_md_to_docx(md_file)
                if result:
                    print(f"Created: {result}")
    else:
        print("Usage:")
        print("  python scripts/md_to_docx.py file.md          # Convert single file")
        print("  python scripts/md_to_docx.py --all [source] [output]  # Convert all files")
        print("")
        print("Examples:")
        print("  python scripts/md_to_docx.py pages/紅樓夢/紅樓夢1.md")
        print("  python scripts/md_to_docx.py --all pages output_docx")
