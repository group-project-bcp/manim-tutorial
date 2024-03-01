from function import Function
from manim import *
from parameters import *


class QuadraticFunction(Function):
    def __init__(self, formula: str, vertex: tuple):
        self.vertex = vertex
        self.formula = formula
        self.function = lambda x: np.array([x, (x - vertex[0])**2 + vertex[1], 0])

    def transform(self, scene, graph_of_func, formula, t_range, axes):
        super().transform(scene, graph_of_func, formula, t_range, axes)
        vertex = Dot().move_to(axes.c2p(*self.vertex))
        vertex_label = MathTex(f"W({self.vertex[0]}, {self.vertex[1]})").next_to(vertex, DOWN)
        line_to_x_axis = Line(vertex.get_center(), axes.c2p(self.vertex[0], 0), color=YELLOW)
        line_to_y_axis = Line(vertex.get_center(), axes.c2p(0, self.vertex[1]), color=YELLOW)

        scene.play(Create(vertex), Write(vertex_label))
        scene.play(Create(line_to_x_axis), Create(line_to_y_axis))
        scene.wait(WAIT_DURATION)
        scene.remove(vertex, vertex_label, line_to_x_axis, line_to_y_axis)

