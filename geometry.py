from manimlib.imports import *


class geometry(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,  # X坐标范围
        "x_tick_frequency": 1,  # X坐标刻度密度
        # "x_labeled_nums": range(0, 11, 1),  # X坐标刻度数值
        "x_axis_label": "$x$",  # X坐标标注

        "y_min": -5,
        "y_max": 5,  # Y坐标范围
        "y_tick_frequency": 1,  # Y坐标刻度密度
        # "y_labeled_nums": range(0, 100, 10),  # Y坐标刻度数值
        "y_axis_label": "$y$",  # Y坐标标注
        "exclude_zero_label": True,  # 不显示Y坐标的0刻度

        "graph_origin": ORIGIN,
        "y_labeled_nums": range(-5, 5, 1),
        "x_labeled_nums": range(-5, 5, 1),
    }
    def construct(self):
        self.setup_axes(animate=True)
        x=self.coords_to_point(-1,-2)
        y=self.coords_to_point(1, 3)
        a=self.coords_to_point(2, 0)
        line_1 = Line(x,
                      y,
                      color=RED,
                      stroke_width=6.0)

        line_2 = Line(1*LEFT,
                      y,
                      color=BLUE,
                      stroke_width=10.0,
                      path_arc=-1)
        arc=Arc(
                radius=3,
                stoke_width=13,
                starta_angle=45*DEGREES,
                angle=90*DEGREES)


        dot=Dot(
            a,
            radius=0.1,
            stroke_width=0,
            fill_color=RED
        )
        self.play(ShowCreation(line_1))
        self.wait(1)
        self.play(Transform(line_1,line_2))
        self.wait(0.5)
        self.play(ShowCreation(arc))
        self.wait(1)
        self.play(FadeOut(arc))
        self.play(FadeOut(line_1))
        self.play(ShowCreation(dot))

