from manimlib.imports import *
import math
class square_root(GraphScene):

    def construct(self):
        ret1=Rectangle(
                    height=math.sqrt(2),
                    width=math.sqrt(2),
                    color="#66CCFF"
                )
        ret1.shift(4*RIGHT)
        ret1.scale(2.5)
        self.play(ShowCreation(ret1))
        t2 = TexMobject("S=2")
        t2.shift(4 * RIGHT)
        self.play(ShowCreation(t2))
        t1=TexMobject("\sqrt{2}=1.4142135")
        t1.next_to(ret1,DOWN)
        self.play(ShowCreation(t1))
        ret2 = Rectangle(
            height=1,
            width=2,
            color="#66CCFF"
        )
        ret2.shift(3 * LEFT)
        t3 = TexMobject("S=2")
        t3.shift(3 * LEFT)
        ret2.scale(2.5)
        self.play(ShowCreation(ret2))
        self.play(ShowCreation(t3))
        t4=TexMobject("2")
        t4.next_to(ret2,DOWN)
        t5=TexMobject("1")
        t5.next_to(ret2,RIGHT)
        self.play(ShowCreation(t4))
        self.play(ShowCreation(t5))
        group1=VGroup(ret2,ret1,t1,t2,t3,t4,t5)
        self.play(group1.shift,UP*2)
        t6=TexMobject(r"{\normalsize L_{width(now)}=\frac{L_{length}+L_{width}}{2}}")
        t6.to_edge(DOWN)
        t6.to_edge(LEFT)
        t6.shift(UP)
        width=2
        height=2/width
        self.play(ShowCreation(t6))
        for i in range(1,5):
            group1=VGroup(t4,t5)
            t7=TexMobject(r"=\frac{"+str(height)+"+"+str(width)+"}{2}")
            t10=TexMobject("="+str(round((height+width)/2,6)))
            t7.next_to(t6,RIGHT)
            t10.next_to(t7,RIGHT)
            self.play(TransformFromCopy(group1,t7))
            self.play(TransformFromCopy(t7,t10))
            width=round((height+width)/2,3)
            height=round(2/width,3)
            ret3= Rectangle(
            height=height,
            width=width,
            color="#66CCFF"
            )
            ret3.shift(3 * LEFT+UP*2)
            ret3.scale(2.5)
            self.play(Transform(ret2,ret3))
            t8=TexMobject(str(width))
            t9=TexMobject(str(height))
            t8.next_to(ret3, DOWN)
            t9.next_to(ret3, RIGHT)
            self.play(Transform(t4,t8))
            self.play(Transform(t5,t9))
            self.play(FadeOut(t7))
            self.play(FadeOut(t10))
        t11=TexMobject(r"\to \sqrt{2}")
        t12=TexMobject("(after\,\,\, infinity\,\,\, iterations)")
        t11.next_to(t6,RIGHT)
        t12.next_to(t6,DOWN)
        self.play(ShowCreation(t11))
        self.play(FadeInFrom(t12,DOWN))
        self.wait(2)
        self.clear()
        t13=Text("参考",font="微软雅黑")
        t13.to_edge(UP)
        self.play(FadeInFrom(t13, UP))
        t14=Text("[1]https://www.zhihu.com/question/20690553/answer/543620219",font="Consolas").scale(0.8).next_to(t13, DOWN).to_corner(LEFT)
        t15=Text("[2]http://www.cs.cornell.edu/courses/cs1112/2018fa",font="Consolas").scale(0.8).next_to(t14, DOWN).to_corner(LEFT)
        self.play(FadeInFrom(t14, UP))
        self.play(FadeInFrom(t15, UP))
        self.wait(2)




