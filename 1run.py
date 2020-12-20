import os

f=open('run_manim.bat', 'w')
classname='MathematicalInduction'
py_flie_name='MathematicalInduction.py'
low='-pl' #480p
middle='-pm' #720p
best=' ' #1440p
high='--high_quality -p'
str01='python manim.py'+" "+py_flie_name+" "+classname+" "+high
f.write(str01)
f.close()
os.system('run_manim.bat')
