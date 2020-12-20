from manimlib.imports import *

class magnetic(Scene):
    def construct(self):
        text1=Text("磁场",font='华文中宋')
        text1.shift(LEFT)
        text1.scale(2)
        text2=TexMobject("(Magnetic Efield)")
        text2.next_to(text1)
        text3=Text("by Erikpsw",color="#66CCFF").next_to(text2,DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.clear()
        self.wait(1)
        t0=TextMobject("小磁针北极所指示的方向为磁场方向")
        self.play(Write(t0))
        t1=TexMobject(r"磁通量\Phi =B S \sin \theta ").next_to(t0,DOWN)
        self.play(Write(t1))
        self.wait(1)
