from cmath import sqrt
from manimlib import *
import numpy as np
import math
s3=math.sqrt(3)

class myclass(Scene):
    def construct(self):
        d=Dot().shift(2*DOWN+4*LEFT)
        d.v=np.array([1,0,0])
        d.B=np.array([0,0,-0.25])
        d.B2=np.array([0,0,-0.55])
        d.ar=Arrow(d.get_center(),d.get_center()+d.v,buff=0)
        l=Line([-3,3.5,0],[-3,-3.5,0])
        d.g=np.array([0,-0.2,0])
        self.play(ShowCreation(l))
        self.play(ShowCreation(Line([-1,3.5,0],[-1,-3.5,0])))
        self.play(ShowCreation(d))
        d.a=np.array([0.5,0,0])
        trace=TracedPath(d.get_center,stroke_color=YELLOW)
        self.add(trace)
        self.add(d.ar)
        def anim(m):
            B=Arrow(d.get_center(),d.get_center()+d.v,buff=0)
            m.become(B)
            
        d.ar.add_updater(anim)
        
        def explict(m,dt):
            if(d.get_x()<-3):
                d.a=np.array([0.5,0,0])
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                d.v=d.v+d.a*dt
                
            if(d.get_x()>-3 and d.get_x()<-1):
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                d.v=d.v+d.g*dt
                
            if(d.get_x()>=-1):
                m.shift(d.v[0]*RIGHT*dt+d.v[1]*UP*dt)
                d.v=(d.v+d.a*dt)/np.linalg.norm(d.v+d.a*dt)*np.linalg.norm(d.v)
                d.a=np.cross(d.v,d.B2)
            
            
    
        d.add_updater(explict)
        self.wait(23)
        self.clear()