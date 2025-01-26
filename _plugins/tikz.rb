require 'digest/md5'
module Jekyll
  module Tags
    class Tikz < Liquid::Block
      def initialize(tag_name, text, tokens)
        super
        # @fname = fname.strip
        @fname = "filename"
        @fname = fname.gsub(/[^\w\s_-]+/, '')
                      .gsub(/(^|\b\s)\s+($|\s?\b)/, '\\1\\2')
                      .gsub(/\s+/, '_')
      end

      def render(context)
        @latex = %Q{
\\documentclass[varwidth]{standalone}
\\usepackage{tikz}
\\usepackage{amsmath,amssymb,latexsym}
... [latex/tikz packages] ...
\\begin{document}
#{super}
\\end{document}
}

        dtikz = File.join(Dir.pwd, "_tikz") # dir of tex, pdf files
        dsvg = File.join(Dir.pwd, "assets", "svg") # dir of public svg files
        FileUtils.mkdir_p dtikz
        FileUtils.mkdir_p dsvg

        ftex = File.join(dtikz, "#{@fname}.tex")
        File.open(ftex, 'w') { |file| file.write("#{@latex}") }

        @md5 = Digest::MD5.hexdigest(@latex)
        @imgsrc = File.join("/assets", "svg", "#{@fname}-#{@md5}.svg")
        "<img width='100%' src=\"#{@imgsrc}\" type=\"image/svg+xml\" />"
      end
    end
  end
end

Liquid::Template.register_tag('latex', Jekyll::Tags::Tikz)
