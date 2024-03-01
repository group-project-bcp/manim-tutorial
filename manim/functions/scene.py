from manim import *
from drawing_schedule import *
from parameters import *


class Functions(Scene):
    def construct(self):
        self.prepare_scene()
        self.linear_function()
        self.quadratic_function()
        self.homographic_function()

    def prepare_scene(self):
        watermark = Text("Michał Cyran", color=WHITE, opacity=0.3).scale(0.2).to_corner(DR)
        self.add(watermark)
        self.wait()

        self.x_range = [-4, 4]
        self.y_range = [-4, 4]
        self.t_range = [*self.x_range, 0.1]
        
        
        self.title = Tex("")
        self.title.to_edge(UP)
        self.play(Write(self.title))

        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=self.x_range[1] - self.x_range[0],
            y_length=self.y_range[1] - self.y_range[0],
            axis_config={
                "include_numbers": True,
                "color": BLUE,
            },
        )

        self.axes.shift(AXES_SHIFT)

        if fast_preview:
            self.add(self.axes)
        else:
            self.play(Create(self.axes))

        def func(t):
            return np.array([t, t, 0])

        self.graph_of_func = ParametricFunction(func, t_range=[-3, 3, 1])
        self.graph_of_func.set_color(BLUE)
        self.graph_of_func.shift(LEFT * 3)

        self.formula = Tex("f(x) = x")
        self.formula.to_corner(UP + RIGHT, buff=0.5)

        self.play(Write(self.formula))
        self.play(Create(self.graph_of_func))

        self.annotation = None

    def linear_function(self):
        self.transform_title("Funkcja liniowa")
        
        texts = (
            "Funkcja liniowa jest postaci:", 
            "\\ f(x) = ax + b",
            "Jesli:",
            "\\ a > 0", 
            "to funkcja jest rosnąca,",
            "\\ a < 0", 
            "to funkcja jest malejąca.",
            "Im większe jest a (na moduł),",
            "tym funkcja jest bardziej stroma."
        )

        self.write_annotation(texts, 4)

        for function in linear_functions_1:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)
        
        texts = (
            "Funkcja przecina os OY w punkcie",
            "\\ (0, b)",
            "Funkcja przecina os OX w punkcie", 
            "(\\frac{-b}{a}, 0)",
        )

        self.write_annotation(texts)

        for function in linear_functions_2:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

    def quadratic_function(self):
        self.clear_formula()
        self.transform_title("Funkcja kwadratowa")

        texts = (
            "Funkcja kwadratowa jest postaci:", 
            "\\ f(x) = ax^2 + bx + c",
            "Jeśli:",
            "\\ a > 0",
            "to parabola jest skierowana do góry",
            "\\ a < 0", 
            "to parabola jest skierowana w dół"
        )

        self.wait(WAIT_DURATION)

        self.write_annotation(texts)

        for function in quadratic_functions_1:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

        texts = (
            "Postac kanoniczna funkcji kwadratowej to: ", 
            "\\ f(x) = a(x - p)^2 + q",
            "Gdzie p i q współrzędne wierzchołka."
        )

        self.write_annotation(texts)

        for function in quadratic_functions_2:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

    def homographic_function(self):
        self.clear_formula()
        self.transform_title("Funkcja homograficzna")

        texts = (
            "Funkcja homograficzna jest postaci:", 
            "f(x) = \\frac{a}{x - p} + q",
            "Gdzie:",
            "p i q to przesunięcie w osiach",
            "odpowiednio OX i OY",
            "Asymptota pionowa to prosta x = p",
            "Asymptota pozioma to prosta y = q"
        )

        self.write_annotation(texts)

        self.wait(WAIT_DURATION)

        for function in homographic_functions:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

    def transform_title(self, new_title: str):
        new_title = Tex(new_title)
        new_title.to_edge(UP)

        self.play(Transform(self.title, new_title))

    def clear_formula(self):
        self.play(Transform(self.formula, Tex("").to_corner(UP + RIGHT, buff=0.5)))
        self.play(Transform(self.graph_of_func, Tex("").shift(LEFT * 3)))

    def write_annotation(self, texts: list[str, ...] | tuple[str, ...], duration: int = 2, font_size: int = 20):
        if fast_preview:  # creating annotation takes a lot of time
            return

        if self.annotation is not None:
            self.play(FadeOut(self.annotation))

        self.annotation = polish_latex_text(*texts, font_size=font_size).to_corner(RIGHT, buff=0.5)

        self.annotation = self.annotation.to_corner(RIGHT, buff=0.5)
        self.play(FadeIn(self.annotation))
        self.wait(duration)


def polish_latex_text(*args, **kwargs):
    group = VGroup()
    font_size = 20
    if "font_size" in kwargs.keys():
        font_size = kwargs["font_size"]

    for arg in args:
        if "\\" in arg:
            group.add(MathTex(arg, font_size=font_size + 10))  # MathTex is a bit smaller than Text
        else:
            group.add(Text(arg, font_size=font_size))
    group.arrange(DOWN)
    return group


