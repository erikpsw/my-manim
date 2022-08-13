from cmath import sqrt
from manimlib import *
import numpy as np
import math
s3=math.sqrt(3)

class myclass(Scene):
    def construct(self):
        d=Dot().shift(3*LEFT+1.5*DOWN)
        d.v=np.array([-s3/2,-1/2,0])
        d.B=np.array([0,0,-1])
        d.B2=np.array([0,0,-1])
        l=Line([-2,3.5,0],[-2,-3.5,0])
        self.play(ShowCreation(l))
        self.play(ShowCreation(Line([0,3.5,0],[0,-3.5,0])))
        self.play(ShowCreation(d))
        d.a=np.cross(d.v,d.B)
        d.g=np.array([0,-s3/4,0])
        trace=TracedPath(d.get_center,stroke_color=YELLOW)
        self.add(trace)
        def explict(m,dt):
            if(d.get_x()<-2):
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                d.v=(d.v+d.a*dt)/np.linalg.norm(d.v+d.a*dt)
                d.a=np.cross(d.v,d.B)
            if(d.get_x()>=-2 and d.get_x()<0):
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                # d.v=d.v+d.g*dt
            if(d.get_x()>=0):
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                d.v=(d.v+d.a*dt)/np.linalg.norm(d.v+d.a*dt)
                d.a=np.cross(d.v,d.B2)
        d.add_updater(explict)
        self.wait(27)
        self.clear()