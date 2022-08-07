from manimlib import *

class myclass(Scene):
    def construct(self):
        d=Dot().shift(5*LEFT)
        trace=TracedPath(d.get_center , stroke_color=YELLOW)
        self.add(d,trace)
        
        x1=ValueTracker(0)
        n2=Tex("0")
        n2.add_updater(lambda t:t.become(Tex(str(round(x1.get_value(),1)))))
        self.play(ShowCreation(n2))
        self.play(x1.set_value,1,rate_func=smooth,run_time=3)
        
        ori=self.time
        def anim(obj,dt):
            obj.shift(dt*RIGHT*2)
            obj.shift(UP*(self.time-ori)*0.01)

        d.add_updater(anim)
        self.wait(4)

       
        