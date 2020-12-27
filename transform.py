from manimlib.imports import *

class transform(Scene):
    def construct(self):
        text1=Text("磁场",font='华文中宋')
        text1.shift(LEFT)
        text1.scale(2)
        text2=TexMobject("(Magnetic field)")
        text2.next_to(text1)
        text3=TextMobject("by Erikpsw").next_to(text2,DOWN)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.play(Write(text3))
        G=VGroup(text1,text2,text3)
        self.wait(1)
        self.play(Uncreate(G))
        self.wait(1)
        t1=TextMobject(r"A magnetic field is a vector field\\ that describes the magnetic influence on \\moving electric charges\\ electric currents\\ and magnetic materials.").shift(UP)
        self.play(AddTextWordByWord(t1, run_time=10.0))
        A = Axes(
            x_min=-5, x_max=5,
            y_min=-3, y_max=3
        )
        self.play(ClockwiseTransform(t1, A))
        self.wait()
        self.play(Uncreate(A))
        points = []
        for x in range(-5, 6):
            points.append(Dot(point=np.array([x, 0.0, 0.0])))
        group = VGroup(*points)
        anno = TextMobject("Show submobjects one by one")
        anno.shift(2 * DOWN)
        self.add(anno)
        self.play(ShowSubmobjectsOneByOne(group, run_time=3.0))
        self.clear()
        square = Square()
        square.generate_target()
        square.target.shift(2 * UP)
        anno = TextMobject("Move to target")
        anno.shift(2 * DOWN)
        self.add(square)
        self.play(MoveToTarget(square))
        self.clear()
        square = Square(fill_opacity=1.0)
        anno = TextMobject("Draw border then fill")
        anno.shift(2 * DOWN)
        self.add(anno)
        self.add(square)
        self.play(DrawBorderThenFill(square))
        self.wait(3)







