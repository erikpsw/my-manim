from manimlib.imports import *

class hello(Scene):
    def construct(self):
        hello=TextMobject("我是潘世维",color=YELLOW)
        rectangle=Rectangle(color=BLUE)
        rectangle.surround(hello)
        group1=VGroup(hello,rectangle)
        welcome=TextMobject("Welcome to manim",color=RED)

        #position
        self.play(Write(hello))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(1)
        self.play(ApplyMethod(group1.scale,2.8))
        self.wait(1)
        self.play(Transform(hello,welcome))
        self.wait(1)