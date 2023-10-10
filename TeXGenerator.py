import jinja2

class TexGenerator:

    def __init__(self, sections):
        self.templatePath = 'template.tex'
        self.preamblePath = 'preamble.tex'
        self.outputPath = 'output.tex'
        self.sections = sections
        with open(self.preamblePath, encoding='utf-8') as preamble:
            self.preamble = preamble.read()
        with open(self.templatePath, encoding='utf-8') as file:
            self.template = jinja2.Template(file.read())
        self.generateTeX()

    def generateTeX(self):
        output = self.template.render(preamble= self.preamble, sections=self.sections)
        with open(self.outputPath, 'w', encoding='utf-8') as file:
            file.write(output)
