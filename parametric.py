from manimlib.imports import *
import math

class parametric(Scene):
    def f1(self,t):
        return np.array((2*np.cos(t),math.sqrt(3)*np.sin(t),0))

    def f2(self,t):
        return np.array((2/np.cos(t),math.sqrt(3)*np.tan(t),0))

    def construct(self):
        t1=TextMobject("Parametric Equation",font='Times New Roman',color="#39C5BB").scale(2.3).shift(UP)
        self.play(Write(t1))
        self.wait(1)
        t2 = TexMobject("Made\,\,by\,\,Erikpsw", color="#66CCFF").next_to(t1, DOWN).shift(2 * RIGHT)
        self.play(ShowCreation(t2))
        self.wait(2)
        self.play(Uncreate(t1))
        self.play(Uncreate(t2))
        self.wait(1)
        A=Axes(
            x_min=-5,x_max=5,
            y_min=-3,y_max=3
        ).add_coordinates()
        self.play(Write(A))
        temp=A.get_axis_labels()
        self.play(Write(temp))
        func=FunctionGraph(lambda x:x**2,x_min=-1.5,x_max=1.5)
        self.play(Write(func))
        t=TexMobject("y=x^2").next_to(func,RIGHT)
        self.play(Write(t))
        self.wait(1)
        G1=VGroup(Dot(A.c2p(-1.5,2.25)),
                  Dot(A.c2p(-1,1)),
                  Dot(A.c2p(-0.5, 0.25)),
                  Dot(A.c2p(0, 0)),
                  Dot(A.c2p(0.5, 0.25)),
                  Dot(A.c2p(1, 1)),
                  Dot(A.c2p(1.5,2.25)))
        self.play(*[Write(dots)for dots in G1])
        self.wait(1)
        self.play(*[Uncreate(dots) for dots in G1])
        G=VGroup(t,func)
        self.play(Uncreate(G))
        self.wait(1)
        f=ParametricFunction(self.f1,t_max=TAU,color=RED)
        self.play(Write(f))
        self.wait(1)
        t=TexMobject(r"\frac {x^2} {4}+\frac {y^2} {3}=1").next_to(f,RIGHT).shift(2*UP)
        self.play(Write(t))
        t2=TexMobject(r"\frac {x^2} {a^2}+ \frac {y^2} {b^2}=1").next_to(f,RIGHT).shift(2*UP)
        self.wait(2)
        self.play(ReplacementTransform(t,t2))
        self.wait(2)
        t=TexMobject(r"\rho =\frac{ep}{1-e\cos\theta}").next_to(f,RIGHT).shift(2*UP)
        self.play(ReplacementTransform(t2, t))
        self.wait(2)
        G = VGroup(t, f)
        self.play(Uncreate(G))
        self.wait(1)
        func = FunctionGraph(lambda x: -x, x_min=-2, x_max=2,color="#66CCFF")
        self.play(Write(func))
        self.wait(1)
        G = VGroup(A, func,temp)
        self.play(ApplyMethod(G.shift,1.5*LEFT))
        self.wait(1)
        t = TexMobject(
            r"\begin{cases}x=x_0+t\cos\theta,\\y=y_0+t\sin\theta \end{cases}(\theta\in [0,\pi])").shift(2 * UP+3 *RIGHT)
        self.play(Write(t))
        self.wait(1)
        self.play(Uncreate(func))
        self.play(Uncreate(t))
        G = VGroup(A, temp)
        self.play(ApplyMethod(G.shift, 1.5 * RIGHT))
        self.wait(1)
        f = ParametricFunction(self.f2, t_max=TAU)
        self.play(Write(f))
        self.wait(1)
        self.play(Uncreate(f))
        self.wait(1)
        A2 = Axes(
            x_min=-7, x_max=7,
            y_min=-1.5, y_max=1.5
        ).add_coordinates()
        temp2 = A2.get_axis_labels()
        G2=VGroup(A2,temp2)
        self.play(ReplacementTransform(G,G2))
        func = FunctionGraph(lambda x: math.sin(x), x_min=-TAU, x_max=TAU, color=BLUE)
        self.play(Write(func))
        self.wait(1)
        func2 = FunctionGraph(lambda x: math.cos(x), x_min=-TAU, x_max= TAU, color=YELLOW)
        self.play(Write(func2))
        self.wait(1)
        self.play(Uncreate(func))
        self.play(Uncreate(func2))
        self.wait(1)
        func = FunctionGraph(lambda x: math.tan(x), x_min=-TAU, x_max=TAU, color=PURPLE)
        self.play(Write(func))
        self.wait(2)
        self.play(Uncreate(func))
        self.play(Uncreate(G2))
        self.wait(1)
        t11 = TextMobject("Thanks", font='Times New Roman').scale(3)
        t12 = TextMobject("2020年12月20日", font='华文中宋').next_to(t11, DOWN).shift(RIGHT)
        self.play(Write(t11))
        self.play(Write(t12))
        self.wait(2)

