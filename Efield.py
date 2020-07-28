from manimlib.imports import *

class Efield(Scene):
    def construct(self):
        text1=Text("电场",font='庞门正道标题体')
        text1.shift(LEFT)
        text1.scale(2)
        text2=TexMobject("(Efield)")
        text2.next_to(text1)
        text3=Text("by潘世维",font='庞门正道标题体',color="#66CCFF")
        text3.next_to(text2,DOWN+RIGHT)
        self.play(FadeIn(text1))
        self.play(Write(text2))
        self.wait(0.5)
        self.play(FadeInFrom(text3,DOWN))
        arr=VGroup(text2,text3,text1)
        self.play(Uncreate(arr))
        text5=TextMobject("库仑定律")
        text4 = TexMobject("(Coulomb's\ law)")
        text4.next_to(text5,RIGHT)
        g1=VGroup(text4,text5)
        g1.shift(3*UP+3.5*LEFT)
        self.play(Write(g1))
        point1 = Dot(2*LEFT)
        point2=Dot(2*RIGHT)
        point1.scale(2)
        point2.scale(2)
        self.play(Write(point1))
        self.play(Write(point2))
        F_vector1 = Vector(RIGHT,color=BLUE)
        F_vector2 = Vector(LEFT, color=BLUE)
        F_vector1.next_to(point1)
        F_vector2.next_to(point2,LEFT*1.2)
        self.play(ShowCreation(F_vector1))
        self.play(ShowCreation(F_vector2))
        F1=TexMobject("F1")
        F2 = TexMobject("F2")
        F1.next_to(F_vector1,UP*0.5)
        F2.next_to(F_vector2,UP*0.5)
        self.play(Write(F1))
        self.play(Write(F2))
        t1=TexMobject(r"\left | \vec{F1}\right |=\left |\vec{F2}\right |=\frac{1}{4 \pi \varepsilon_{0}} \frac{q_{1} q_{2}}{r^{2}}")
        t1.shift(UP*2)
        self.wait(1)
        self.play(Write(t1))
        t2=TexMobject(r"\left |\vec{F}\right |=\frac{1}{4 \pi \varepsilon_{0}} \frac{q_{1} q_{2}}{r^{2}}")
        t2.shift(UP * 2)
        self.play(Transform(t1,t2))
        self.wait()
        t3=TextMobject("电场强度")
        t3.shift(3*UP+5.5*LEFT)
        self.play(Transform(g1, t3))
        self.wait(0.5)
        t4=TexMobject(r"\vec{E}=\frac{\vec{F}}{q_{0}}=\frac{1}{4 \pi \varepsilon_{0}} \frac{q}{r^{2}}")
        t4.shift(UP * 2)
        self.play(Transform(t1, t4))