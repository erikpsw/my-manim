from manimlib.imports import *

class language(Scene):
    def construct(self):
        t1=TextMobject(r"ワシらの作る組紐もせやから神さまの技、時間の流れのそのものを顕しとる\\寄り集まって形を作り、捻れて絡まって、時には戻って、途切れ、またつながり\\それが結び。それが時間").shift(2*UP).scale(0.7)
        t2=TextMobject(r"我们编织的结绳也是神的力量，显示了时间的流转\\聚在一起，成型，扭曲，缠绕，有时又还原，断裂，再次连接\\这就是结，这就是时间", font="华文中宋").next_to(t1,DOWN).scale(0.7)
        self.play(Write(t1))
        self.wait(3)
        self.play(Write(t2))
        self.wait(3)
        self.play(Uncreate(t1))
        self.play(Uncreate(t2))
        t1=TextMobject(r'''L'humaine sagesse était tout entière dans ces deux mots :
\\Attendre et espérer !''').shift(2*UP).scale(0.7)
        t2=TextMobject("人类的一切智慧就在这几个字中：希望和等待").next_to(t1,DOWN).scale(0.7)
        self.play(Write(t1))
        self.wait(3)
        self.play(Write(t2))
        self.wait(3)
        self.play(Uncreate(t1))
        self.play(Uncreate(t2))