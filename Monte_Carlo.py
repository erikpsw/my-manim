from manimlib.imports import *
import random
arr=[]
yes=0
for i in range(1, 1000):
    r1 = random.uniform(-4, 4)
    r2 = random.uniform(-4, 4)
    if (r1 * r1 + r2 * r2) < 9:
        yes = yes + 1
    else:
        continue
    arr.append(64 * round(yes / i, 2))
class Monte_Carlo(GraphScene):
    def construct(self):
        text=Text("蒙特卡洛方法",font='庞门正道标题体',color="#39C5BB")
        text.set_width(11)
        for i in range(6):
            self.play(ShowIncreasingSubsets(text[i], run_time=0.3))
        self.play(Uncreate(text))
        axes = Axes(
            x_min=-4.9,
            x_max=6,
            y_min=-5,
            y_max=5
        )
        axes.scale(0.7)
        axes.shift(3.5*LEFT)
        axes.add_coordinates([-4,-3,3,4],[-4,-3,3,4])
        self.play(ShowCreation(axes), run_time=2)
        self.play(ShowCreation(axes.get_axis_labels()))
        # dot=Dot(axes.coords_to_point(0,0))
        # t=TextMobject(str(dot.get_center()[0]))
        # self.play(ShowCreation(t))
        circle=Circle(
            arc_center=3.335*LEFT,
            radius=2.1
        )
        self.play(ShowCreation(circle))
        ret=Rectangle(
            height=5.6,
            width=5.6,
            color="#66CCFF"
        )
        ret.shift(3.335*LEFT)
        self.play(ShowCreation(ret))
        t1=TexMobject(r'''       S_
        {circle} = 28.27433 ''')
        t1.shift(3.5*UP+2*RIGHT)
        self.play(ShowCreation(t1))
        t2=TexMobject("S_{current} =")
        t2.shift(2.5*UP+2*RIGHT)
        self.play(ShowCreation(t2))
        In=0
        count=0
        for i in range(1,1000):
            count=count+1
            r1=random.uniform(-4,4)
            r2=random.uniform(-4,4)
            if (r1*r1+r2*r2)<9:
                dot1 = SmallDot(axes.coords_to_point(r1, r2),color=YELLOW)
                In=In+1
            else:
                dot1 = SmallDot(axes.coords_to_point(r1,r2))
            self.play(ShowCreation(dot1), run_time=0.005)
            if(count==60):
                count=0
                t3=TexMobject("S_{current} ="+r"\frac{"+str(In)+"}{"+str(i)+"}"+r"\times "+str(64)+"="+str(64*round(In/i,2)) )
                t3.shift(2.5*UP+3*RIGHT)
                self.play(Transform(t2,t3))
        self.clear()
        self.wait(2)



