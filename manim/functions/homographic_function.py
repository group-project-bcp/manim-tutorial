from function import Function
from manim import *
from parameters import *

class HomographicFunction(Function):
    def __init__(self, coefficient: int, shift: tuple):
        self.coefficient = coefficient
        self.shift = shift
        self.formula = fr"f(x) = \frac{coefficient}{{x - {shift[0]}}} + {shift[1]}"
        self.function = lambda x: np.array([x, coefficient / (x - shift[0]) + shift[1] , 0])

    def transform(self, scene, graph_of_func, formula, t_range, axes):
        new_formula = MathTex(self.formula)
        new_formula.to_corner(UP + RIGHT, buff=0.5)

        scene.play(Transform(formula, new_formula)) # Transform(graph_of_func, left_function)

        left_range = [t_range[0], self.shift[0] - 0.1, t_range[2]]
        right_range = [self.shift[0] + 0.1, t_range[1], t_range[2]]

        left_function = ParametricFunction(self.function, t_range=left_range)
        left_function.set_color(BLUE).shift(LEFT * 3)
        
        right_function = ParametricFunction(self.function, t_range=right_range)
        right_function.set_color(BLUE).shift(LEFT * 3)

        scene.remove(graph_of_func)
        scene.play(Write(left_function))

        scene.play(Write(right_function))
        scene.wait(WAIT_DURATION)

        vertical_asymptote = DashedLine(axes.c2p(self.shift[0], -10), axes.c2p(self.shift[0], 10), color=RED)
        horizontal_asymptote = DashedLine(axes.c2p(-10, self.shift[1]), axes.c2p(10, self.shift[1]), color=RED)
        vertical_asymptote.set_color(YELLOW)
        horizontal_asymptote.set_color(GREEN)

        scene.play(Write(vertical_asymptote, run_time=1), Write(horizontal_asymptote, run_time=1))

        x_asymptote_label = MathTex(f"x = {self.shift[0]}").next_to(vertical_asymptote.get_center(), DOWN).shift(RIGHT).set_color(YELLOW)
        y_asymptote_label = MathTex(f"y = {self.shift[1]}").next_to(horizontal_asymptote.get_center(), RIGHT).shift(UP).set_color(GREEN)

        scene.play(Write(x_asymptote_label), Write(y_asymptote_label))

        scene.wait(WAIT_DURATION)
        scene.play(FadeOut(left_function, right_function, vertical_asymptote, horizontal_asymptote, x_asymptote_label, y_asymptote_label))
        scene.wait(WAIT_DURATION)
        # vertex = Dot().move_to(axes.c2p(*self.vertex))
        # vertex_label = MathTex(f"W({self.vertex[0]}, {self.vertex[1]})").next_to(vertex, DOWN)

        # scene.play(Create(vertex), Write(vertex_label))
        # scene.play(Create(line_to_x_axis), Create(line_to_y_axis))
        # scene.wait(WAIT_DURATION)
        # scene.remove(vertex, vertex_label, line_to_x_axis, line_to_y_axis)
