import os
f=open('run_manim.bat', 'w')

py_flie_name="Euler's_method"

classname='myclass'

is_save=1

low='-l' #480p
middle='-pm' #720p
best=' ' #1440p
high='--hd'#1080p

quality=best
if(is_save==0):
    str01='manimgl'+" "+py_flie_name+".py "+classname+quality
if(is_save==1):
    str01='manimgl'+" "+py_flie_name+".py "+classname+' -o '+quality 
f.write(str01)
f.close()
os.system('run_manim.bat')

# scroll the middle mouse button to move the screen up and down

# hold down the z on the keyboard while scrolling the middle mouse button to zoom the screen

# hold down the s key on the keyboard and move the mouse to pan the screen

# hold down the d key on the keyboard and move the mouse to change the three-dimensional perspective.
