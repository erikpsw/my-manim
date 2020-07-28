import os

f=open('run_manim.bat', 'w')
classname='mylatex'
py_flie_name='latextest.py'
low='-pl' #480p
middle='-pm' #720p
best=' ' #1440p
high='--high_quality'
str01='python manim.py'+" "+py_flie_name+" "+classname+" "+low
f.write(str01)
f.close()
os.system('run_manim.bat')