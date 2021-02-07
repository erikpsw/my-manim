from manimlib.imports import *
import math
class symmetry(GraphScene):
    def axe(self,x1,x2,y1,y2,t=0):
        A=Axes(
            x_min=x1,x_max=x2,
            y_min=y1,y_max=y2
        ).shift(t)
        temp = A.get_axis_labels()
        return VGroup(A,temp)

    def title(self,text):
        t1= TexMobject(text).to_edge(LEFT).to_edge(UP)
        self.play(Write(t1))

    def tex(self,t,dir=0):
        t1= TexMobject(t).shift(dir)
        self.play(Write(t1))

    def text(self, t, dir=0):
        t1 = TextMobject(t).shift(dir)
        self.play(Write(t1))
    def construct(self):
        self.title(r"\mathrm{case}\,1:\text{关于}y\text{轴对称(偶函数)}")
        self.wait(2)
        A=self.axe(-3,3,0,3).shift(DOWN)
        self.play(Write(A))
        self.wait(2)
        func = FunctionGraph(lambda x: x ** 2, x_min=-1.5, x_max=1.5).shift(DOWN)
        self.play(Write(func))
        self.wait(2)
        l1 = Line(A[0].c2p(1,1),A[0].c2p(1,0) , color=BLUE)
        self.play(Write(l1))
        t1=TexMobject("x_0").next_to(l1,DOWN)
        self.play(Write(t1))
        self.wait()
        l2 = Line(A[0].c2p(-1, 1), A[0].c2p(-1, 0), color=BLUE)
        self.play(Write(l2))
        t2 = TexMobject("-x_0").next_to(l2, DOWN)
        self.play(Write(t2))
        self.wait()
        l3=DashedLine(A[0].c2p(-1, 1),A[0].c2p(1.5,1))
        self.play(Write(l3))
        self.wait()
        t3=TexMobject("f(x_0)=f(-x_0)").next_to(l3,RIGHT)
        self.play(Write(t3))
        self.wait()
        self.clear()
        self.title(r"\mathrm{case}2:\text{关于原点对称(奇函数)}")
        A = self.axe(-3, 3, -2.5, 2.5)
        self.play(Write(A))
        self.wait(2)
        func = FunctionGraph(lambda x: x **3, x_min=-1.4, x_max=1.4)
        self.play(Write(func))
        self.wait(2)
        l1 = Line(A[0].c2p(1, 1), A[0].c2p(1, 0), color=BLUE)
        self.play(Write(l1))
        t1 = TexMobject("x_0").next_to(l1, DOWN)
        self.play(Write(t1))
        self.wait()
        l2 = Line(A[0].c2p(-1, -1), A[0].c2p(-1, 0), color=BLUE)
        self.play(Write(l2))
        t2 = TexMobject("-x_0").next_to(l2, UP)
        self.play(Write(t2))
        self.wait()
        t3 = TexMobject("f(x_0)=-f(-x_0)").next_to(func, RIGHT).shift(UP)
        self.play(Write(t3))
        self.wait()
        self.clear()
        self.title(r"\mathrm{case}3:f(x)\text{关于}x=\frac{a+b}{2}\text{对称}")
        self.tex("f(a+mx)=f(b-mx)\Leftrightarrow f(a+b-mx)=f(mx)",UP)
        self.tex(r"\frac{a+mx+b-mx}{2}=\frac{a+b}{2}")
        

