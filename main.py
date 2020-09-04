from resume_builder import resume_builder as rb
import datetime as dt
import sys

resume = rb.Resume(first_name='Phil',
                   last_name='Nicholls',
                   phone='+97258-473-9564',
                   email='phil.j.nicholls@gmail.com',
                   address='Nahal meron 527/1 Nili 7193000 Israel',
                   website='http://philjnicholls.com')
work_experience = rb.WorkExperience(start_date='2000-05',
                           end_date='2003-6',
                           title='Semantico', tags=['project manager',
                                                    'full-stack developer'],
                           role='Project Manager',
                           details=['Did some managing of projects',
                                    'Turned up']
                          )
resume.add_work_experience(work_experience)

education = rb.Education(start_date='2001-02',
                           end_date='2002-05',
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
json = resume.get_json()
print(json)
new_resume = rb.Resume()
new_resume.load_json(json)
print(new_resume.get_html())
