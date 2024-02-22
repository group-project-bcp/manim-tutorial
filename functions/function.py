from manim import *
from parameters import *

class Function:
    def __init__(self, formula: str, function):
        self.formula = formula
        self.function = function

    def transform(self, scene, graph_of_func, formula, t_range, axes):
        new_graph_of_func = ParametricFunction(self.function, t_range=t_range)
        new_graph_of_func.set_color(BLUE)
        new_graph_of_func.shift(LEFT * 3)
        # new_graph_of_func.set_color(RED)

        new_formula = MathTex(self.formula)
        new_formula.to_corner(UP + RIGHT, buff=0.5)

        scene.play(Transform(graph_of_func, new_graph_of_func), Transform(formula, new_formula))
        scene.wait(WAIT_DURATION)

