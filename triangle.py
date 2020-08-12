from manimlib.imports import *
class triangle(Scene):
    def construct(self):
        trans = np.array([[0.5,0.5 * math.sqrt(3) ], [-0.5 * math.sqrt(3),0.5 ]])
        trans2 = np.array([[0.5, -0.5 * math.sqrt(3)], [0.5 * math.sqrt(3),0.5 ]])
        ori = np.array([0, 0,0])
        dotx=0
        t0=TextMobject("Made by Erikpsw",color="#39C5BB")
        ret=Polygon(np.array([0,0,0]),np.array([6,0,0]),np.array([6,6,0]),np.array([0,6,0])).shift(5*LEFT).shift(3*DOWN)
        self.play(ShowCreation(ret))
        t0.next_to(ret,RIGHT).shift(2*DOWN)
        self.play(ShowCreation(t0))
        self.wait(0.5)
        now=0
        count=0
        past=1
        for i in range(100):
            self.clear()
            count=count+1
            dot1=np.array([6,now])
            dot2=np.matmul(dot1,trans)
            dot1=np.append(dot1,0)
            dot2=np.append(dot2,0)
            pol1 = Polygon(ori, dot1, dot2).shift(5*LEFT).shift(3*DOWN)
            if(count==5):
                count=0
                t1=TexMobject("l= "+str(round(math.sqrt(((now/6)**2)+1),3))).next_to(ret,RIGHT)
                past=round(math.sqrt(((now/6)**2)+1),3)
            else:
                t1 = TexMobject("l= " + str(past)).next_to(ret, RIGHT)
            self.add(pol1,ret,t1,t0)
            self.wait(0.05)
            now=now+0.02
            if(dot2[1]>=6):
                dotx=dot2[0]
                break
        yet=0
        count=0
        arc1=Arc(
            radius=2,
            stroke_width=10,
            angle=15*DEGREES,
            start_angle=0*DEGREES
        ).shift(5*LEFT).shift(3*DOWN)
        arc2 = Arc(
            radius=2,
            angle=-15 * DEGREES,
            stroke_width=10,
            start_angle=90 * DEGREES
        ).shift(5 * LEFT).shift(3 * DOWN)
        self.play(ShowCreation(arc1))
        t2=TexMobject("15^{\circ}").next_to(arc1,RIGHT)
        self.play(ShowCreation(t2))
        self.play(ShowCreation(arc2))
        t3 = TexMobject("15^{\circ}").next_to(arc2, UP)
        self.play(ShowCreation(t3))
        self.wait(1.5)
        for i in range(100):
            self.clear()
            count = count + 1
            dot2=np.array([dotx-yet,6])
            dot1=np.matmul(dot2,trans2)
            dot1=np.append(dot1,0)
            dot2=np.append(dot2,0)
            pol2 = Polygon(ori, dot1, dot2).shift(5*LEFT).shift(3*DOWN)
            if (count == 5):
                count = 0
                t1 = TexMobject("l= " + str(round(math.sqrt((((dotx-yet) / 6) ** 2) + 1), 3))).next_to(ret, RIGHT)
                past = round(math.sqrt((((dotx-yet)/ 6) ** 2) + 1), 3)
            else:
                t1 = TexMobject("l= " + str(past)).next_to(ret, RIGHT)
            self.add(pol2, ret, t1,t0)
            self.wait(0.05)
            yet=yet+0.02
            if(dot2[0]<=0):
                break