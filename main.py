from resume_builder import resume_builder as rb

resume = rb.Resume(first_name='Phil', last_name='Nicholls')

print(resume.html())
resume.pdf('resume.pdf')
