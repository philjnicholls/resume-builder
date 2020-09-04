from resume_builder import resume_builder as rb
import datetime as dt
import sys

resume = rb.Resume(first_name='Phil',
                   last_name='Nicholls',
                   phone='+97258-473-9564',
                   email='phil.j.nicholls@gmail.com',
                   address='Nahal meron 527/1 Nili 7193000 Israel',
                   website='http://philjnicholls.com')
experience = rb.Experience(start_date=dt.datetime(2000, 5, 1),
                           end_date=dt.datetime(2003, 7, 1),
                           title='Semantico', tags=['project manager',
                                                    'full-stack developer'],
                           role='Project Manager',
                           details=['Did some managing of projects',
                                    'Turned up']
                          )
resume.add_experience(experience)

education = rb.Education(start_date=dt.datetime(1998, 5, 1),
                           end_date=dt.datetime(2000, 7, 1),
                           title='St. Vincent College',
                           details=[('Studied Information Technology, '
                                    'Physchology and Sociaology')]
                          )
resume.add_education(education)


if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    tag = None

print(resume.get_html(tag=tag))
resume.export_pdf('resume.pdf')
