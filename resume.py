from weasyprint import HTML

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

    def pdf(self):
        pass

