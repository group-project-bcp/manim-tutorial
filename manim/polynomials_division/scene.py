from manim import *
from division_data_class import DivisionData
from parameters import WAIT_DURATION, fast_preview
from helper_functions import *
from division_data import *

FIRST_COLOR = BLUE
SECOND_COLOR = GREEN
DEFAULT_COLOR = WHITE

class Division(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.divisions = []


    def construct(self):
        self.prepare_scene()

        for poly in polys_to_divide:
            self.poly_division(poly)

        self.wait()

    def prepare_scene(self):
        self.title = Text("Dzielenie wielomianów").to_edge(UP)
        self.add(self.title)
        self.annotation = None
        watermark = Text("Michał Cyran", color=WHITE, opacity=0.3).scale(0.2).to_corner(DR)
        self.add(watermark)
        self.wait()

    def poly_division(self, poly: DivisionData):
        self.result = [" ? "]
        self.first_step = True

        self.dividend = MathTex(*poly.dividend).to_corner(UL).shift(DOWN)
        self.divisor = MathTex(*poly.divisor).next_to(self.dividend, RIGHT)
        self.equal_sign = MathTex("=").next_to(self.divisor, RIGHT)
        self.result_tex = MathTex(*self.result).next_to(self.equal_sign, RIGHT)

        self.play(Write(self.dividend))
        self.play(Write(self.divisor))
        self.play(Write(self.equal_sign))
        self.play(Write(self.result_tex))

        self.current_dividend = self.dividend

        for step in poly.steps:
            self.division_step(step.result, step.products, step.dividends, step.is_last)

        self.wait()
        self.clear()
        self.prepare_scene()

        # self.division_step(
        #     "x^2",
        #     [
        #         "(x^3 + 3x^2)",
        #         "-(x^3 + 3x^2)",
        #         "-x^3 - 3x^2"
        #     ],
        #     [
        #         ["0x^3 + 0x^2 -4x - 12"], 
        #         ["-4x", "- 12"]
        #     ]
        # )

        # self.division_step(
        #     "-4",
        #     [
        #         "(-4x - 12)",
        #         "-(-4x - 12)",
        #         "4x + 12"
        #     ],
        #     [
        #         ["0x - 0"], 
        #         ["0"]
        #     ], last = True
        # )


    def division_step(self, result: str, products: list[str], dividends: list[list[str]], last: bool = False):
        self.write_annotation(
            (
                "Dzielimy pierwszy wyraz dzielnej", 
                "przez pierwszy wyraz dzielnika"
            )
        )

        self.color(self.current_dividend, FIRST_COLOR)
        self.color(self.divisor, SECOND_COLOR)

        self.wait(WAIT_DURATION)
        self.add_to_result(result)
        self.wait(WAIT_DURATION)

        self.color(self.current_dividend, DEFAULT_COLOR)
        self.color(self.divisor, DEFAULT_COLOR)
        self.wait(WAIT_DURATION)

        self.first_step = False

        self.write_annotation(
            (
                "Mnożymy wynik przez dzielnik", 
                "i odejmujemy od dzielnej"
            )
        )

        self.color(self.result_tex, FIRST_COLOR)
        self.play(ApplyMethod(self.divisor.set_color, SECOND_COLOR))
        self.wait(WAIT_DURATION)
        self.color(self.result_tex, DEFAULT_COLOR)
        self.play(ApplyMethod(self.divisor.set_color, DEFAULT_COLOR))

        products = [MathTex(product).next_to(self.current_dividend, DOWN).align_to(self.current_dividend, LEFT) for product in products]

        self.play(Write(products[0]))

        for product in products[1:]:
            self.wait(WAIT_DURATION)
            self.play(Transform(products[0], product))

        self.line = Line(products[0].get_left() + DOWN * 0.4, products[0].get_right() + DOWN * 0.4, color=WHITE)
        self.play(Write(self.line))

        self.wait(WAIT_DURATION)

        new_dividends = [MathTex(*dividend).next_to(products[0], DOWN * 1.2).align_to(products[0], LEFT) for dividend in dividends]

        self.play(Write(new_dividends[0]))

        for dividend in new_dividends[1:]:
            self.wait(WAIT_DURATION)
            self.play(Transform(new_dividends[0], dividend))

        self.current_dividend = new_dividends[0]

        if not last:
            self.write_annotation((
                "Powtarzamy proces dla nowej dzielnej",
            ))
        else:
            self.write_annotation((
                "Gdy otrzymamy 0, kończymy dzielenie",
            ))

    def color(self, obj, color):
        if fast_preview:
            return
        
        if obj is self.dividend or obj is self.divisor:
            index = 1
        elif obj is self.result_tex:
            index = -1
        else:
            index = 0

        self.play(ApplyMethod(obj[index].set_color, color))

    def add_to_result(self, value):
        if self.first_step:
            self.result = [value]
        else:
            self.result.append(value)

        self.play(Transform(self.result_tex, MathTex(*self.result).next_to(self.equal_sign, RIGHT)))

    def write_annotation(self, texts: list[str, ...] | tuple[str, ...], duration: float = 0.5, font_size: int = 20):
        if fast_preview:  # creating annotation takes a lot of time
            return

        if self.annotation is not None:
            self.play(FadeOut(self.annotation))

        self.annotation = polish_latex_text(*texts, font_size=font_size).to_corner(RIGHT, buff=0.5)
        
        self.annotation = self.annotation.to_corner(DR, buff=0.5).shift(UP * 0.3)
        self.play(FadeIn(self.annotation))
        self.wait(duration)