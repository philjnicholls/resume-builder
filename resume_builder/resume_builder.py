from weasyprint import HTML
from jinja2 import Environment, PackageLoader, select_autoescape

class Experience():
    pass

class Resume():
    """
    Contains resume data and functions
    for manipulating and exporting
    """

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')
        self.phone = kwargs.get('phone', '')
        self.address = kwargs.get('address', '')
        self.template = kwargs.get('template', 'resume.html')

    def __str__(self):
        return (
            f'{self.first_name} {self.last_name}'
        )

    def html(self):
        env = Environment(
                loader=PackageLoader('resume_builder', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template(self.template)
        return template.render(first_name=self.first_name,
                               last_name=self.last_name)

    def pdf(self, file_path='resume.pdf'):
        html = HTML(string=self.html())
        html.write_pdf(file_path)

