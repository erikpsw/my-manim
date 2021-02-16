from manimlib.imports import *
class Transformation(LinearTransformationScene):
    def construct(self):
        mob = Polygon([1,1.73,0],[2,0,0],[1,-1.73,0],[-1,-1.73,0],[-2,0,0],[-1,1.73,0],color=PURPLE)
        matrix1 = [[1, 0.353], [0, 0.353]]
        self.add_transformable_mobject(mob)
        self.apply_matrix(matrix1)
        self.wait(3)
        t1=TexMobject(r"i=\left[ {\begin{array}{*{20}c}1\\0\end{array}} \right] \rightarrow\left[ {\begin{array}{*{20}c}1\\0\end{array}} \right]").scale(0.9)
        t2=TexMobject(r"j=\left[ {\begin{array}{*{20}c}0\\1\end{array}} \right]\rightarrow\left[ {\begin{array}{*{20}c}\frac{\sqrt{2}}{4} \\\frac{\sqrt{2}}{4}\end{array}} \right]").scale(0.9)
        t3=TexMobject(r"S_{\text{直观图}}=\frac{\sqrt{2}}{4}S_{\text{原}}").scale(0.9)
        TextGroup = VGroup(t1, t2, t3).arrange_submobjects(DOWN, aligned_edge=LEFT,buff=0.6).shift(4.5 * LEFT)
        self.add_title(TextGroup, animate=True)
class Oblique_projection(LinearTransformationScene,GraphScene,ThreeDScene):
    def title(self,text):
        t1= TextMobject(text).to_edge(LEFT).to_edge(UP)
        self.play(Write(t1))

    def text(self,t,dir=0,time=None):
        t1= TextMobject(t).shift(dir)
        self.play(Write(t1,run_time=time))

    def construct(self):

        # t1 = TextMobject("斜二测画法", font='微软雅黑').scale(2.3).shift(UP).set_color([BLUE, YELLOW, ORANGE, RED])
        # self.play(Write(t1))
        # self.wait(1)
        # t2 = TexMobject("Made\,\,by\,\,Erikpsw", color="#66CCFF").next_to(t1, DOWN).shift(2 * RIGHT)
        # t3 = TexMobject("@Alaana").next_to(t2, DOWN)
        # self.play(ShowCreation(t2))
        # self.play(ShowCreation(t3))
        # self.wait(2)
        # G1 = VGroup(t1, t2, t3)
        # self.play(Uncreate(G1))
        # self.wait(1)
        self.title("步骤")
        self.text(r"$y$轴顺时针旋转$45^{\circ} $\\已知图形中平行于$x$轴的线段在直观图中长度保持不变\\平行于$y$轴的线段长度变成原来的一半",time=4)
        self.wait(2)



        # axes = ThreeDAxes()
        # matrix = [[1, 0,0], [0.353, 0.353,0],[0,1,0]]
        # self.play(Write(axes))
        # self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        # self.wait(3)
