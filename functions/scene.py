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

        self.adnotation = None

    def linear_function(self):
        self.transform_title("Funkcja liniowa")
        
        texts = (
            ("Funkcja liniowa jest postaci:"), 
            ("$f(x) = ax + b$", ""),
            ("Jesli:"),
            ("$a > 0$", ", to funkcja jest rosnaca"),
            ("$a < 0$", ", to funkcja jest malejaca"),
            ("Im wieksze jest a (na modul)"), 
            ("tym funkcja jest bardziej stroma")
        )

        self.write_adnotation(texts, 4)

        for function in linear_functions_1:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)
        
        texts = (
            ("Funkcja przecina os OY w punkcie (0, b)"),
            ("Funkcja przecina os OX w punkcie", "$(\\frac{-b}{a}, 0)$"),
        )

        self.write_adnotation(texts)

        for function in linear_functions_2:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)


    def quadratic_function(self):
        self.transform_title("Funkcja kwadratowa")

        texts = (
            ("Funkcja kwadratowa jest postaci:"), 
            ("$f(x) = ax^2 + bx + c$", ""),
            ("Jesli:"),
            ("$a > 0$", ", to parabola jest skierowana do gory"),
            ("$a < 0$", ", to parabola jest skierowana w dol")
        )

        self.wait(WAIT_DURATION)

        self.write_adnotation(texts)

        for function in quadratic_functions_1:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

        texts = (
            ("Postac kanoniczna funkcji kwadratowej to: "), 
            ("$f(x) = a(x - p)^2 + q$", ""),
            ("Gdzie p i q wspolrzedne wierzcholka")
        )

        self.write_adnotation(texts)

        for function in quadratic_functions_2:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

    def homographic_function(self):
        self.transform_title("Funkcja homograficzna")

        texts = (
            ("Funkcja homograficzna jest postaci:"), 
            ("$f(x) = \\frac{a}{x - p} + q$", ""),
            ("Gdzie:"),
            ("p i q to przesuniecie w osiach odpowiednio OX i OY"),
            ("Asymptota pionowa to prosta x = p"),
            ("Asymptota pozioma to prosta y = q")
        )

        self.write_adnotation(texts)

        self.wait(WAIT_DURATION)

        for function in homographic_functions:
            function.transform(self, self.graph_of_func, self.formula, self.t_range, self.axes)

    def transform_title(self, new_title: str):
        new_title = Tex(new_title)
        new_title.to_edge(UP)

        self.play(Transform(self.title, new_title))

    def write_adnotation(self, texts: list[str], duration: int = 2):
        if fast_preview:  # creating adnotation takes a lot of time
            return

        if self.adnotation is not None:
            self.play(FadeOut(self.adnotation))

        self.adnotation = VGroup().to_corner(RIGHT, buff=0.5)

        for text in texts:
            self.adnotation.add(Tex(*text, font_size=20))
        
        self.adnotation = self.adnotation.arrange(DOWN).to_corner(RIGHT, buff=0.5)
        self.play(FadeIn(self.adnotation))
        self.wait(duration)


