from manimlib import *
import numpy as np

class myclass(Scene):
    def construct(self):
        l=1.75#模拟的步长
        title=TexText("Euler's method").scale(2).set_color(BLUE)
        self.play(Write(title))
        name=TexText("Made by Erikpsw").shift(4*RIGHT+2*DOWN)
        self.play(Write(name))
        self.wait(3)
        self.play(Uncreate(name))
        self.play(Uncreate(title))
        d=Dot().shift(2*LEFT+0.5*DOWN)
        d.save_state()
        d.v=np.array([0,1,0])
        d.B=np.array([0,0,1])
        t=Title("Explict Euler's Method")
        t1=Tex(r"\begin{cases}\vec{v}\left(t_{1}\right)=\vec{v}\left(t_{0}\right)+M^{-1} \vec{F}\left(t_{0}\right)\Delta t \\ \vec{x}\left(t_{1}\right)=\vec{x}\left(t_{0}\right)+\vec{v}\left(t_{0}\right) \Delta t\end{cases}").next_to(t,DOWN)
        t4=TexText(r"用当前的状态计算速度和加速度$(\text{Forward} )$").next_to(t1,DOWN)
        self.play(ShowCreation(t))
        self.play(ShowCreation(t1))
        self.play(ShowCreation(t4))
        self.wait(4)
        self.play(Uncreate(t1))
        self.play(Uncreate(t4))
        self.play(ShowCreation(d))
        d.a=np.cross(d.v,d.B)
        trace=TracedPath(d.get_center,stroke_color=YELLOW)
        self.add(trace)
        
  
        #显式欧拉方法(略加改进)
        def explict_p(m,dt):
            m.shift(d.v[0]*RIGHT*dt*l+d.v[1]*l*UP*dt)#v[0]为vx
            d.v=(d.v+d.a*dt)/np.linalg.norm(d.v+d.a*dt)#除以模长使速度始终为1
            d.a=np.cross(d.v,d.B)
            #updater是通过add_updater起作用
            #一切修改都需要作用于对象d上
            
        #显式欧拉方法(经典)
        def explict(m,dt):
            d.a=np.cross(d.v,d.B)
            m.shift(d.v[0]*RIGHT*dt*l+d.v[1]*l*UP*dt)
            d.v=(d.v+d.a*dt)#速度变化, 能量不守恒
         
 
        
        d.add_updater(explict)
        self.wait(30)
        self.clear()
        
        d=Dot().shift(2*LEFT)
        d.save_state()
        d.v=np.array([0,1,0])
        d.B=np.array([0,0,1])
        d.a=np.cross(d.v,d.B)
        t=Title("Explict Euler's Method(my version)")
        t2=Tex(r"\begin{cases}\vec{v}\left(t_{1}\right)=\lambda(\vec{v}\left(t_{0}\right)+M^{-1} \vec{F}\left(t_{0}\right)\Delta t) \\ \vec{x}\left(t_{1}\right)=\vec{x}\left(t_{0}\right)+\vec{v}\left(t_{0}\right) \Delta t\end{cases} ").next_to(t,DOWN)
        t4=TexText(r'''为使圆周运动的速度保持不变,我在$\vec{v}\left(t_{1}\right)$前乘上$\lambda$\\
                   其中$\lambda=||\vec{v}(t_0)||/||\vec{v}(t_1)||$''').next_to(t2,DOWN)
        self.play(ShowCreation(t))
        self.play(ShowCreation(t2))
        self.play(ShowCreation(t4))
        self.wait(4)
        self.play(Uncreate(t2))
        self.play(Uncreate(t4))
        self.play(ShowCreation(d))
        trace=TracedPath(d.get_center,stroke_color=YELLOW)
        self.add(trace)
 
        d.add_updater(explict_p)
        self.wait(30)
        self.clear()
        
        self.clear()
        
        d=Dot().shift(2*LEFT)
        d.save_state()
        d.v=np.array([0,1,0])
        d.B=np.array([0,0,1])
        d.a=np.cross(d.v,d.B)
        t=Title("Implict Euler's Method")
        self.play(ShowCreation(t))
        t1=Tex(r"\begin{cases}\vec{v}\left(t_{1}\right)=\vec{v}\left(t_{0}\right)+M^{-1} \vec{F}\left(t_{1}\right)\Delta t \\ \vec{x}\left(t_{1}\right)=\vec{x}\left(t_{0}\right)+\vec{v}\left(t_{1}\right) \Delta t\end{cases}").next_to(t,DOWN)
        t4=TexText(r"用未来的状态去计算速度和加速度再来更新$(\text{Backward} )$").next_to(t1,DOWN)
        self.play(ShowCreation(t1))
        self.play(ShowCreation(t4))
        self.wait(4)
        self.play(Uncreate(t1))
        self.play(Uncreate(t4))
        self.play(ShowCreation(d))
        trace=TracedPath(d.get_center,stroke_color=YELLOW)
        self.add(trace)
        d.vtemp=0
        def implict(m,dt):
            d.vtemp=(d.v+d.a*dt)#t1时的速度
            d.a=np.cross(d.vtemp,d.B)#t1时刻的加速度由速度决定
            d.v=(d.v+d.a*dt)
            m.shift(d.v[0]*RIGHT*dt*l+d.v[1]*l*UP*dt)
          
            
            
        d.add_updater(implict)
        self.wait(30)
        self.clear()
        
        self.clear()
        
       
        
        
        
        