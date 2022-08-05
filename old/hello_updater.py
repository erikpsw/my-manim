from manimlib.imports import *

class hello_updater(Scene):
    def construct(self):
        A = Axes(
            x_min=-5, x_max=5,
            y_min=0, y_max=6.5
        ).add_coordinates().shift(3*DOWN)
        self.play(Write(A))
        temp = A.get_axis_labels()
        self.play(Write(temp))
        func = ParametricFunction(lambda t: np.array([t,t**2,0]), t_min=-2.5, t_max=2.5).shift(3*DOWN)
        def anim0(obj,alpha):
            obj.move_to(func.point_from_proportion(alpha))

        self.play(Write(func))
        D=Dot(A.c2p(-2.5, 6.25))
        self.play(Write(D))
        self.wait()
        D2=Dot(A.c2p(-2.5,0))
        dec=DecimalNumber(0)
        dec.add_updater(lambda a:a.set_value(D2.get_center()[0])).shift(3*RIGHT+UP)
        self.play(Write(dec))
        self.play(Write(D2))
        D2.add_updater(lambda a,dt:a.shift(0.05*RIGHT))
        self.play(
            UpdateFromAlphaFunc(D,anim0)
        )
        self.wait()
        G=VGroup(D,D2,dec,func)
        self.play(Uncreate(G))
        self.wait()
        A2=Axes(
            x_min=-5, x_max=5,
            y_min=-3, y_max=3
        ).add_coordinates()
        self.play(ReplacementTransform(A,A2))
        self.play(Uncreate(temp))
        self.wait()
        cir1=Circle(radius=1,color=BLUE)
        vec1=Vector(RIGHT,color=YELLOW)
        G1=VGroup(cir1,vec1)
        cir2 = Circle(radius=1, color=BLUE)
        vec2 = Vector(RIGHT, color=YELLOW)
        G2 = VGroup(cir2, vec2)
        G2.save_state()
        G2.shift(RIGHT)
        def anim1(obj,dt):
            obj.rotate(dt,about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())

        self.play(ShowCreation(G1))
        self.play(Write(G2))
        self.wait()
        dec = DecimalNumber(2)
        dec.add_updater(lambda a: a.set_value(vec2.get_center()[0])).shift(3 * RIGHT + UP)
        path=TracedPath(vec2.get_end)
        G1.add_updater(anim1)
        G2.add_updater(anim2)
        self.add(path,dec)
        path.add_updater(lambda a,dt:a.shift(DOWN*dt))
        self.wait(10)
        G1.clear_updaters()
        G2.clear_updaters()
        path.clear_updaters()
        dec.clear_updaters()
        self.wait()
        G3=VGroup(dec,path,G1,G2)
        self.play(Uncreate(G3))
        A3 = Axes(
            x_min=0, x_max=12,
            y_min=-3, y_max=3
        ).add_coordinates().shift(5*LEFT)
        self.play(ReplacementTransform(A2,A3))
        cir1 = Circle(radius=1, color=BLUE).shift(UP)
        vec1 = Vector(DOWN, color=YELLOW).shift(UP)
        G1 = VGroup(cir1, vec1).shift(5*LEFT)
        self.play(Write(G1))
        def anim1(obj,dt):
            obj.shift(0.03*RIGHT)
            obj.rotate(about_point=cir1.get_center(),angle=-dt)
        G1.add_updater(anim1)
        path = TracedPath(vec1.get_end)
        self.add(path)
        self.wait(6)
        self.clear()
        t11 = TextMobject("Thanks", font='Times New Roman').scale(3)
        t12 = TextMobject("2020年12月26日", font='华文中宋').next_to(t11, DOWN).shift(RIGHT)
        t13 = TextMobject("月考结束了", font='华文中宋').next_to(t12, DOWN).shift(RIGHT)
        self.play(Write(t11))
        self.play(Write(t12))
        self.play(Write(t13))
        self.wait(2)

