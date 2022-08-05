import os
f=open('run_manim.bat', 'w')

py_flie_name='hello'

classname='SquareToCircle'

low='-pl' #480p
middle='-pm' #720p
best=' ' #1440p
high='--high_quality -p'
str01='manimgl'+" "+py_flie_name+".py "+classname
f.write(str01)
f.close()
os.system('run_manim.bat')

# scroll the middle mouse button to move the screen up and down

# hold down the z on the keyboard while scrolling the middle mouse button to zoom the screen

# hold down the s key on the keyboard and move the mouse to pan the screen

# hold down the d key on the keyboard and move the mouse to change the three-dimensional perspective.
