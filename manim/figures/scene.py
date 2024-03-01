from parameters import *
from helper_functions import *


class Figures(Scene):
    def construct(self):
        self.prepare_scene()
        self.draw_rectangle()
        self.draw_triangle()
        self.triangle_explanation()
        self.draw_parallelogram()
        self.parallelogram_explaination()
        self.draw_trapeze()
        self.trapeze_explaination()

    def prepare_scene(self):
        self.annotation = None
        watermark = Text("Michał Cyran", color=WHITE, opacity=0.3).scale(0.2).to_corner(DR)
        self.add(watermark)
        self.wait()

    def draw_rectangle(self):
        rectangle = Rectangle(width=3, height=2, color=BLUE).to_edge(LEFT).shift(RIGHT * 2)
        rectangle.set_fill(TEAL, opacity=0.8)
        rectangle.set_stroke(width=0)

        width_label = Tex("a").next_to(rectangle, DOWN)
        height_label = Tex("b").next_to(rectangle, LEFT)

        texts = (
            "Pole prostokąta to iloczyn długości jego boków.",
            "\\ P = a * b",
            "a - długość jednego boku",
            "b - długość drugiego boku"
        )

        title = Text("Pole prostokąta").to_edge(UP)

        self.play(Write(title))
        self.play(Write(rectangle))
        self.play(Write(width_label), Write(height_label))
        self.write_annotation(texts)
        self.wait()
        self.play(FadeOut(title, rectangle, width_label, height_label, self.annotation))
    
    def draw_triangle(self):
        triangle = Polygon(
            LEFT*2, UP*3, RIGHT*2,
            color=TEAL, 
            fill_opacity=0.8, 
            stroke_width=0
        ).to_edge(LEFT).shift(RIGHT * 2 + DOWN * 2)
    
        height = Line(triangle.get_bottom(), triangle.get_top(), color=BLUE)

        texts = (
            "Pole trójkąta to połowa iloczynu",
            "długości podstawy i jej wysokości.",
            "P = \\frac{a * h}{2}",
            "a - długość jednego boku",
            "h - długość wysokości"
        )

        side_a_label = Tex("a").next_to(triangle, DOWN)
        side_b_label = Tex("h").next_to(height, RIGHT)

        title = Text("Pole trójkąta").to_edge(UP)

        self.play(Write(title))
        self.play(Write(triangle))
        self.play(Write(height))
        self.play(Write(side_a_label), Write(side_b_label))
        self.write_annotation(texts)
        self.wait()
        self.play(FadeOut(title, triangle, height, side_a_label, side_b_label, self.annotation))

    def triangle_explanation(self):
        def apply_shift(obj):
            obj.center().to_edge(LEFT).shift(RIGHT * 2)

        title = Text("Skąd wzór na pole trójkąta").to_edge(UP)

        rectangle = Polygon(ORIGIN, UP*3, UP*3 + RIGHT * 4, RIGHT*4, color=BLUE_D, fill_opacity=0.8, stroke_width=0)
        triangle = Polygon(ORIGIN, UP*3, RIGHT*4, color=TEAL, fill_opacity=0.8, stroke_width=0)
        second_triangle = Polygon(ORIGIN, UP*3 + RIGHT * 2, RIGHT*4, color=TEAL, fill_opacity=0.8, stroke_width=0)
        third_triangle = Polygon(ORIGIN, UP*3 + RIGHT * 4, RIGHT*4, color=TEAL, fill_opacity=0.8, stroke_width=0)
        apply_shift(rectangle)
        apply_shift(triangle)
        apply_shift(second_triangle)
        apply_shift(third_triangle)        

        a = Tex("a").next_to(rectangle, DOWN)
        b = Tex("b").next_to(rectangle, LEFT)

        self.play(Write(title))
        self.write_annotation((
            "Pole trójkąta jest równie połowie pola prostokąta, ",
            "gdzie podstawa trójkąta pokrywa się z jednym bokiem prostokąta,",
            "a wysokość trójkąta jest równa drugiemu boku prostokąta."
        ), font_size=15)

        self.play(Write(rectangle))
        self.play(Write(triangle))
        self.play(FadeIn(a), FadeIn(b))
        self.wait()
        self.play(FadeOut(a), FadeOut(b))

        self.play(Transform(triangle, second_triangle))
        a = Tex("a").next_to(rectangle, DOWN)
        h = Tex("h").next_to(triangle).shift(LEFT * 2)
        line = Line(triangle.get_bottom(), triangle.get_top(), color=GREEN, stroke_width=3)
        self.play(Write(line))
        self.play(FadeIn(a), FadeIn(h))
        self.wait()
        self.play(FadeOut(a), FadeOut(h))
        self.play(FadeOut(line))
        
        self.play(Transform(triangle, third_triangle))
        a = Tex("a").next_to(rectangle, DOWN)
        b = Tex("b").next_to(rectangle, RIGHT)
        self.play(FadeIn(a), FadeIn(b))
        self.wait()
        self.play(FadeOut(a, b, rectangle, triangle, title, self.annotation))

    def draw_parallelogram(self):
        parallelogram = Polygon(ORIGIN, UP*3 + RIGHT, UP*3 + RIGHT * 5, RIGHT*4, color=TEAL, fill_opacity=0.8, stroke_width=0).to_edge(LEFT).shift(RIGHT * 2 + DOWN * 2)
        parallelogram.set_stroke(width=0)
        parallelogram.set_fill(TEAL, opacity=0.8)

        height = Line(parallelogram.get_bottom(), parallelogram.get_top(), color=BLUE)

        a = Tex("a").next_to(parallelogram, DOWN)
        h = Tex("h").next_to(height, LEFT)

        texts = (
            "Pole równoległoboku to iloczyn długości",
            "jego podstawy i wysokości.",
            "P = a * h",
            "a - długość podstawy",
            "h - długość wysokości"
        )

        title = Text("Pole równoległoboku").to_edge(UP)

        self.play(Write(title))
        self.play(Write(parallelogram))
        self.play(Write(height))
        self.play(Write(a), Write(h))
        self.write_annotation(texts)
        self.wait()
        
        self.play(FadeOut(title, parallelogram, height, a, h, self.annotation))
        
    def parallelogram_explaination(self):
        def apply_shift(obj):
            obj.center().to_edge(LEFT).shift(RIGHT * 2)

        title = Text("Skąd wzór na pole równoległoboku").to_edge(UP)

        rectangle = Polygon(ORIGIN, UP*3, UP*3 + RIGHT * 4, RIGHT*4, color=BLUE_D, fill_opacity=0.8, stroke_width=0)
        parallelogram = Polygon(ORIGIN, UP*3 + RIGHT, UP*3 + RIGHT * 5, RIGHT*4, color=TEAL, fill_opacity=0.8, stroke_width=0)
        missing_part = Polygon(ORIGIN, UP*3, UP*3 + RIGHT, color=YELLOW, fill_opacity=1, stroke_width=0)
        external_triangle = Polygon(ORIGIN, UP*3, UP*3 + RIGHT, color=YELLOW, fill_opacity=1, stroke_width=0)


        apply_shift(rectangle)
        apply_shift(parallelogram)
        apply_shift(missing_part)
        apply_shift(external_triangle)
        external_triangle.shift(RIGHT * 4)

        self.play(Write(title))
        self.write_annotation((
            "Pole równoległoboku jest równie polu prostokąta, ",
            "gdzie podstawa równoległoboku pokrywa ",
            "się z jednym bokiem prostokąta,",
            "a wysokość równoległoboku jest równa",
            "drugiemu boku prostokąta."
            "",
            "Wystający trójkąt jest równy brakującej",
            "części prostokąta, stąd pole",
            "jest takie samo dla obu figur."
        ), font_size = 15)

        self.play(Write(rectangle))
        self.play(Write(parallelogram))
        self.play(Write(missing_part))
        self.play(Write(external_triangle))
        self.wait()
        self.play(FadeOut(missing_part), FadeOut(external_triangle))
        self.play(Transform(parallelogram, rectangle))
        self.wait()
        self.play(FadeOut(rectangle, parallelogram, title, self.annotation))

        # # self.play(Transform(parallelogram, second_parallelogram))
        # a = Tex("a").next_to(rectangle, DOWN)
        # h = Tex("h").next_to(parallelogram).shift(LEFT * 2)
        # line = Line(parallelogram.get_bottom(), parallelogram.get_top(), color=GREEN, stroke_width=3)
        # self.play(Write(line))
        # self.play(FadeIn(a), FadeIn(h))

    def draw_trapeze(self):
        trapeze = Polygon(ORIGIN, UP*3 + RIGHT, UP*3 + RIGHT * 4, RIGHT*5, color=TEAL, fill_opacity=0.8, stroke_width=0).to_edge(LEFT).shift(RIGHT * 2 + DOWN * 2)
        trapeze.set_stroke(width=0)
        trapeze.set_fill(TEAL, opacity=0.8)

        height = Line(trapeze.get_bottom(), trapeze.get_top(), color=BLUE)

        a = Tex("a").next_to(trapeze, DOWN)
        b = Tex("b").next_to(trapeze, UP)
        h = Tex("h").next_to(height, LEFT)

        texts = (
            "Pole trapezu to iloczyn sumy długości jego podstaw",
            "i wysokości.",
            "P = \\frac{a + b}{2} * h",
            "a, b - długości podstaw",
            "h - długość wysokości"
        )

        title = Text("Pole trapezu").to_edge(UP)

        self.play(Write(title))
        self.play(Write(trapeze))
        self.play(Write(height))
        self.play(Write(a), Write(b), Write(h))
        self.write_annotation(texts)
        self.wait()
        self.play(FadeOut(title, trapeze, height, a, b, h, self.annotation))

    def trapeze_explaination(self):
        def apply_shift(obj):
            obj.center().to_edge(LEFT).shift(RIGHT)
        
        title = Text("Skąd wzór na pole trapezu").to_edge(UP)
        
        trapeze = Polygon(ORIGIN, UP*3 + RIGHT, UP*3 + RIGHT * 4, RIGHT*6, color=TEAL, fill_opacity=0.8, stroke_width=0)
        triangle_1 = Polygon(ORIGIN, UP*3 + RIGHT, RIGHT*6, color=BLUE_D, fill_opacity=0.8, stroke_width=0)
        triangle_2 = Polygon(UP*3 + RIGHT, UP*3 + RIGHT * 4, RIGHT*6, color=BLUE_C, fill_opacity=0.8, stroke_width=0)

        apply_shift(trapeze)
        apply_shift(triangle_1)
        apply_shift(triangle_2)
        triangle_2.shift(RIGHT)

        a = Tex("a").next_to(trapeze, DOWN)
        b = Tex("b").next_to(trapeze, UP)

        height = Line(trapeze.get_bottom(), trapeze.get_top(), color=GREEN, stroke_width=3)
        h = Tex("h").next_to(height, LEFT)

        formula_1 = MathTex("P = \\frac{a * h}{2}").next_to(triangle_1, LEFT).set_color(BLUE_D)
        formula_2 = MathTex("P = \\frac{b * h}{2}").next_to(triangle_2, RIGHT).set_color(BLUE_C).shift(UP * 2 + LEFT)

        step_1 = MathTex("P = \\frac{a * h}{2} + \\frac{b * h}{2}").to_edge(DOWN)
        step_2 = MathTex("P = \\frac{a * h + b * h}{2}").to_edge(DOWN)
        step_3 = MathTex("P = \\frac{(a + b) * h}{2}").to_edge(DOWN)

        self.play(Write(title))
        self.write_annotation((
            "Pole trapezu jest równe sumie pól dwóch trójkątów. ",
            "Jeden z trójkątów ma podstawę równą jednej podstawie trapezu, ",
            "a drugi z trójkątów ma podstawę równą drugiej podstawie trapezu.",
            "Wysokości obu trójkątów są równe wysokości trapezu."
        ), font_size = 15, duration=5)

        self.play(Write(trapeze))
        self.play(Write(triangle_1))
        self.play(Write(triangle_2))
        self.play(Write(height))
        self.play(Write(a), Write(b), Write(h))
        self.wait()
        self.play(Write(formula_1), Write(formula_2))
        self.wait()
        self.play(Write(step_1))
        self.wait()
        self.play(Transform(step_1, step_2))
        self.wait()
        self.play(Transform(step_1, step_3))

        self.wait()
        self.play(FadeOut(trapeze, triangle_1, triangle_2, height, a, b, h, formula_1, formula_2, step_1, title, self.annotation))
                  
    def write_annotation(self, texts: list[str, ...] | tuple[str, ...], duration: int = 2, font_size: int = 20):
        if fast_preview:  # creating annotation takes a lot of time
            return

        # if self.annotation is not None:
        #     self.play(FadeOut(self.annotation))

        self.annotation = polish_latex_text(*texts, font_size=font_size).to_corner(RIGHT, buff=0.5)
        
        self.annotation = self.annotation.to_corner(RIGHT, buff=0.5)
        self.play(FadeIn(self.annotation))
        self.wait(duration)

