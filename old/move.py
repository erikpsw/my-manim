from manimlib.imports import *

class move(Scene):
    def construct(self):
        mur=ImageMobject("C:\manim-master\my_manim\pic\mur.png")
        self.play(FadeIn(mur))
        self.play(mur.scale, {'scale_factor': 2.5,'about_edge':UP})
        self.wait(1)
        self.play(mur.move_to,UP*1.3,aligned_edge=DOWN)
        self.play(mur.rotate,90*DEGREES,IN)
        self.play(mur.rotate,90*DEGREES,OUT)
        self.play(mur.scale, {'scale_factor': 0.5})
        self.play(mur.rotate, 90 * DEGREES, {'axis' : IN, 'about_point' : ORIGIN})
        self.play(mur.flip,{'axis':RIGHT})
        self.play(mur.flip, {'axis': LEFT})
        self.play(mur.rotate, 90 * DEGREES, {'axis': OUT, 'about_point': ORIGIN})
        self.play(mur.stretch,{'factor':2,'dim':1})
        self.play(mur.stretch,2,0)
        c=Circle(radius=0.5)
        self.play(FadeIn(c))
        self.play(c.next_to,mur,DOWN,buff=6)