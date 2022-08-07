from manimlib import *

class hello_updater(Scene):
    def construct(self):

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
        t11 = Text("Thanks", font='Times New Roman').scale(3)
        t12 = Text("2020年12月26日", font='华文中宋').next_to(t11, DOWN).shift(RIGHT)
        t13 = Text("月考结束了", font='华文中宋').next_to(t12, DOWN).shift(RIGHT)
        self.play(Write(t11))
        self.play(Write(t12))
        self.play(Write(t13))
        self.wait(2)

