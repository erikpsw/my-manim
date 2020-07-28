from manimlib.imports import *
import math


class Graphing(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -3,
        "y_max": 3,
        # "graph_origin": 3*DOWN+6*LEFT,
        "graph_origin": ORIGIN
    }


    def construct(self):
        #Make graph


        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph)
        #Display graph
        self.play(ShowCreation(func_graph))

    def func_to_graph(self, x):
        return (math.asinh(x))


