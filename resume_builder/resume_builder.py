from weasyprint import HTML, CSS
from jinja2 import Environment, PackageLoader, select_autoescape
import datetime as dt
import json

class Tags():
    """
    Used for applying an array of tags to objects
    """

    def __init__(self, tags=[]):
        self.tags = tags

    def get_tags(self):
        return self.tags


class TaggedString(str, Tags):
    """
    Basic Python String with ability to add tags
    """

    def __new__(cls, value, *args, **kwargs):
        return super(TaggedString, cls).__new__(cls, value)

    def __init__(self, value, tags=[]):
        super(TaggedString, self).__init__(tags)


class BasicDetails():
    """
    Holds basic contact details
    """

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')
        self.phone = kwargs.get('phone', '')
        self.address = kwargs.get('address', '')
        self.website= kwargs.get('website', '')

class Experience(Tags):
    """
    Details of experience such as place of work,
    internships etc.
    """

    def __init__(self, **kwargs):
        self.start_date = self.__get_date(kwargs.get('start_date', None))
        self.end_date = self.__get_date(kwargs.get('end_date', None))
        self.title = kwargs.get('title', '')
        self.details = kwargs.get('details', [])

        if 'tags' in kwargs:
            super().__init__(kwargs['tags'])

    @staticmethod
    def __get_date(date):
        if date is not None:
            return dt.datetime.strptime(date, '%Y-%m')
        else:
            return None

class Education(Experience):
    pass

class WorkExperience(Experience):
    pass

class Resume():
    """
    Contains resume data and functions
    for manipulating and exporting
    """

    def __init__(self, **kwargs):
        self.basic_details = BasicDetails(**kwargs)
        self.work_experience = []
        self.education = []

    def __str__(self):
        # Render the resume in plain text
        return (
            f'{self.first_name} {self.last_name}'
        )

    def _get_template(self, template, tag=None):
        # Helper function to load and render templates

        env = Environment(
                loader=PackageLoader('resume_builder', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template(template)

        # Filter experiences and education  if a specific tag was requested
        if tag:
            filtered_work_experience = filter(lambda e: tag in e.tags,
                                              self.work_experience)
            filtered_education = filter(lambda e: tag in e.tags, self.education)
        else:
            filtered_work_experience = self.work_experience
            filtered_education = self.education

        return template.render(basic_details=self.basic_details,
                               work_experience=filtered_work_experience,
                               education=filtered_education)

    def get_html(self, html_template='resume.html', tag=None):
        # Render resume HTML based on a tag if supplied
        return self._get_template(html_template, tag=tag)

    def _get_css(self, css_template='style.css'):
        # Get the CSS from templates
        return self._get_template(css_template)

    def export_pdf(self, file_path='resume.pdf', tag=None):
        # Render HTML and use it to export PDF to a file
        html = HTML(string=self.get_html(tag=tag))
        css = CSS(string=self._get_css())
        html.write_pdf(file_path, stylesheets=[css])

    def add_work_experience(self, work_experience):
        self.work_experience.append(work_experience)

    def add_education(self, education):
        self.education.append(education)

    def _serialize(self, obj):
        if (isinstance(obj, BasicDetails) or
            isinstance(obj, WorkExperience) or
            isinstance(obj, Education)):
            return obj.__dict__

        if isinstance(obj, dt.date):
            return obj.strftime('%Y-%m')

        return None

    def get_json(self):
        return json.dumps(self.__dict__, default=self._serialize)

    def load_json(self, json_string):
        load_dict = json.loads(json_string)

        self.basic_details = BasicDetails(**load_dict['basic_details'])

        for work_experience in load_dict['work_experience']:
            self.add_work_experience(WorkExperience(**work_experience))

        for education in load_dict['education']:
            self.add_education(Education(**education))
