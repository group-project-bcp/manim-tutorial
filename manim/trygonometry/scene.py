from parameters import WAIT_DURATION, fast_preview
from helper_functions import *

class Trygonometry(Scene):
    def construct(self):
        self.prepare_scene()
        self.write_right_triangle()
        self.fade_out()
        self.write_any_angle()

    def prepare_scene(self):
        self.title = Text("Funkcje trygonometryczne").to_edge(UP)
        self.add(self.title)
        self.annotation = None
        watermark = Text("Michał Cyran", color=WHITE, opacity=0.3).scale(0.2).to_corner(DR)
        self.add(watermark)

        self.mobjects_to_fade = []

    def write_right_triangle(self):
        self.subtitle = Text("kąt ostry w trójkącie prostokątnym", font_size=20).next_to(self.title, DOWN)
        self.write(self.subtitle)

        triangle = Polygon(ORIGIN, UP * 3, RIGHT * 3, color=BLUE).to_edge(LEFT).shift(DOWN * 2 + RIGHT)
        self.create(triangle)
        self.wait(WAIT_DURATION)
        
        line1 = Line(triangle.get_vertices()[2], triangle.get_vertices()[1])
        line2 = Line(triangle.get_vertices()[2], triangle.get_vertices()[0])

        # Create the angle using the lines
        angle = Angle(line1, line2, radius=1)
        self.alpha_label = MathTex("\\alpha").next_to(angle, RIGHT * 0.03).shift(DOWN * 0.1)
        self.create(angle)
        self.write(self.alpha_label)

        self.a_label = MathTex("a").next_to(triangle, LEFT)
        self.b_label = MathTex("b").next_to(triangle, DOWN)
        
        midpoint = (triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2
        self.c_label = MathTex("c").next_to(midpoint, RIGHT)        
        self.write(self.a_label, self.b_label, self.c_label)
        
        self.write_latex_annotation([
            ["sin \\ \\alpha =", "{a", "\\over" ,"c}"],
            ["cos \\ \\alpha =", "{b", "\\over" ,"c}"],
            ["tg \\ \\alpha =", "{a", "\\over" ,"b}"],
            ["ctg \\ \\alpha =", "{b", "\\over" ,"a}"]
        ])
        self.wait()

    def write_any_angle(self):
        self.subtitle = Text("dla dowolnego kąta - znak wartości w poszczególnych ćwiartkach", font_size=20).next_to(self.title, DOWN)
        self.write(self.subtitle)

        self.wait(WAIT_DURATION)

        number_plane_shift = LEFT * 4 + DOWN * 0.3

        self.number_plane = NumberPlane(
            x_range=(-5, 5, 2),
            y_range=(-5, 5, 2),
            x_length=5,
            y_length=5,
        ).move_to(number_plane_shift)

        self.create(self.number_plane)

        self.x = Line(ORIGIN, RIGHT, color=BLUE).shift(number_plane_shift)
        self.y = Line(RIGHT, RIGHT + UP * 2, color=YELLOW).shift(number_plane_shift)
        self.r = Line(ORIGIN, RIGHT + UP * 2, color=RED).shift(number_plane_shift)
        self.create(self.r, self.y, self.x)

        self.wait(WAIT_DURATION)

        self.angle = Angle(self.x, self.r, radius=0.7, color=GREEN)
        self.alpha_label = MathTex("\\alpha", color=GREEN, font_size=36).next_to(self.angle, LEFT * 0.03).shift(DOWN * 0.1 + RIGHT * 0.2)
        self.create(self.angle)
        self.write(self.alpha_label)

        self.r_label = MathTex("r", color=RED).move_to(self.r).shift(LEFT * 0.3)
        self.y_label = MathTex("y", color=YELLOW).next_to(self.y, RIGHT)
        self.x_label = MathTex("x", color=BLUE).next_to(self.x, DOWN)
        self.write(self.r_label, self.y_label, self.x_label)

        self.write_latex_annotation([
            ["sin \\ \\alpha =", "{y", "\\over" ,"r}"],
            ["cos \\ \\alpha =", "{x", "\\over" ,"r}"],
            ["tg \\ \\alpha =", "{y", "\\over" ,"x}"],
            ["ctg \\ \\alpha =", "{x", "\\over" ,"y}"]
        ])

        self.quarter = Text("I ćwiartka", font_size=24).next_to(self.number_plane, RIGHT, buff=2).shift(UP * 1.9)
        self.signs = Text("Znaki x, y (jako współrzędnych) i r:", font_size=16).next_to(self.quarter, DOWN, buff=0.2)
        self.sign_values = MathTex("x: +", ",", "y: +", ",", "r: +", font_size=37).next_to(self.signs, DOWN, buff=0.2)
        self.sign_values[0].set_color(BLUE)
        self.sign_values[2].set_color(YELLOW)
        self.sign_values[4].set_color(RED)
        self.r_expl = Text("(r zawsze dodatnie jako długość ramienia)", font_size=16).next_to(self.sign_values, DOWN, buff=0.2)
        self.write(self.quarter)
        self.write(self.signs) 
        self.write(self.sign_values, self.r_expl)
        self.wait(WAIT_DURATION)
        
        self.sin_exp = MathTex("sin\\ \\alpha = {", "+", "\\over ", "+", "} = +", font_size=30).next_to(self.r_expl, DOWN, buff=0.4)
        self.cos_exp = MathTex("cos\\ \\alpha = {", "+", "\\over ", "+", "} = +", font_size=30).next_to(self.sin_exp, DOWN, buff=0.2)
        self.tg_exp = MathTex("tg\\ \\alpha = {", "+", "\\over ", "+", "} = +", font_size=30).next_to(self.cos_exp, DOWN, buff=0.2)
        self.ctg_exp = MathTex("ctg\\ \\alpha = {", "+", "\\over ", "+", "} = +", font_size=30).next_to(self.tg_exp, DOWN, buff=0.2)
        
        self.sin_exp[1].set_color(YELLOW)
        self.sin_exp[3].set_color(RED)
        self.cos_exp[1].set_color(BLUE)
        self.cos_exp[3].set_color(RED)
        self.tg_exp[1].set_color(YELLOW)
        self.tg_exp[3].set_color(BLUE)
        self.ctg_exp[1].set_color(BLUE)
        self.ctg_exp[3].set_color(YELLOW)
        
        self.write(self.sin_exp)
        self.write(self.cos_exp)
        self.write(self.tg_exp)
        self.write(self.ctg_exp)
        self.wait(WAIT_DURATION)

        quarters = ["II", "III", "IV"]
        
        data = [
            (-1, 2), (-1, -2), (1, -2),
        ]

        x_shifts = [DOWN, UP, UP]
        y_shifts = [LEFT, LEFT, RIGHT]
        r_shifts = [RIGHT * 0.3, RIGHT * 0.3, LEFT * 0.3]

        sin_expls = [
            ["sin\\ \\alpha = {", "+", "\\over ", "+", "} = +"],
            ["sin\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
            ["sin\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
        ]

        cos_expls = [
            ["cos\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
            ["cos\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
            ["cos\\ \\alpha = {", "+", "\\over ", "+", "} = +"],
        ]

        tg_expls = [
            ["tg\\ \\alpha = {", "+", "\\over ", "-", "} = -"],
            ["tg\\ \\alpha = {", "-", "\\over ", "-", "} = +"],
            ["tg\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
        ]

        ctg_expls = [
            ["ctg\\ \\alpha = {", "-", "\\over ", "+", "} = -"],
            ["ctg\\ \\alpha = {", "-", "\\over ", "-", "} = +"],
            ["ctg\\ \\alpha = {", "+", "\\over ", "-", "} = -"],
        ]


        for i, (x, y) in enumerate(data):
            self.fade(self.quarter, self.signs, self.sign_values, self.r_expl, self.sin_exp, self.cos_exp, self.tg_exp, self.ctg_exp, self.angle, self.alpha_label)
            self.quarter = Text(f"{quarters[i]} ćwiartka", font_size=24).next_to(self.number_plane, RIGHT, buff=2).shift(UP * 1.9)
            self.write(self.quarter)

            new_x = Line(ORIGIN, RIGHT * x, color=BLUE).shift(number_plane_shift)
            new_y = Line(RIGHT * x, RIGHT * x + UP * y, color=YELLOW).shift(number_plane_shift)
            new_r = Line(ORIGIN, RIGHT * x + UP * y, color=RED).shift(number_plane_shift)
            new_x_label = MathTex("x", color=BLUE).next_to(new_x, x_shifts[i])
            new_y_label = MathTex("y", color=YELLOW).next_to(new_y, y_shifts[i])
            new_r_label = MathTex("r", color=RED).move_to(new_r).shift(r_shifts[i])

            self.transform((self.x, new_x), (self.y, new_y), (self.r, new_r), (self.x_label, new_x_label), (self.y_label, new_y_label), (self.r_label, new_r_label))
            self.angle = Angle(new_x, new_r, radius=0.7, color=GREEN, other_angle=i % 2 == 0)
            self.alpha_label = MathTex("\\alpha", color=GREEN, font_size=36).next_to(self.angle, y_shifts[i] * -0.03).shift(y_shifts[i] * 0.2)

            self.write(self.angle, self.alpha_label)

            self.write(self.signs)
            self.sign_values = MathTex(f"x: {'+' if x > 0 else '-'}", ",", f"y: {'+' if y > 0 else '-'}", ",", "r: +", font_size=37).next_to(self.signs, DOWN, buff=0.2)
            self.sign_values[0].set_color(BLUE)
            self.sign_values[2].set_color(YELLOW)
            self.sign_values[4].set_color(RED)

            self.write(self.sign_values, self.r_expl)
            self.sin_exp = MathTex(*sin_expls[i], font_size=30).next_to(self.r_expl, DOWN, buff=0.4)
            self.cos_exp = MathTex(*cos_expls[i], font_size=30).next_to(self.sin_exp, DOWN, buff=0.2)
            self.tg_exp = MathTex(*tg_expls[i], font_size=30).next_to(self.cos_exp, DOWN, buff=0.2)
            self.ctg_exp = MathTex(*ctg_expls[i], font_size=30).next_to(self.tg_exp, DOWN, buff=0.2)
            
            self.sin_exp[1].set_color(YELLOW)
            self.sin_exp[3].set_color(RED)
            self.cos_exp[1].set_color(BLUE)
            self.cos_exp[3].set_color(RED)
            self.tg_exp[1].set_color(YELLOW)
            self.tg_exp[3].set_color(BLUE)
            self.ctg_exp[1].set_color(BLUE)
            self.ctg_exp[3].set_color(YELLOW)
            

            self.write(self.sin_exp)
            self.wait(WAIT_DURATION)
            self.write(self.cos_exp)
            self.wait(WAIT_DURATION)
            self.write(self.tg_exp)
            self.wait(WAIT_DURATION)
            self.write(self.ctg_exp)
            
            self.wait(WAIT_DURATION * 2)

    def play_animation(self, *mobjects: Mobject, animation):
        if not fast_preview:
            self.play(*[animation(mobject) for mobject in mobjects])
        else:
            self.add(*mobjects)

        for mobject in mobjects:
            self.mobjects_to_fade.append(mobject)

    def write(self, *mobjects: Mobject):
        self.play_animation(*mobjects, animation=Write)

    def create(self, *mobjects: Mobject):
        self.play_animation(*mobjects, animation=Create)

    def fade(self, *mobjects: Mobject):
        if not fast_preview:
            self.play(*[FadeOut(mobject) for mobject in mobjects])
        else:
            self.remove(*mobjects)

    def transform(self, *pairs: tuple[Mobject, Mobject]):
        if not fast_preview:
            self.play(*[Transform(pair[0], pair[1]) for pair in pairs])
        else:
            self.remove(*[pair[0] for pair in pairs])
            self.add(*[pair[1] for pair in pairs])

        for pair in pairs:
            self.mobjects_to_fade.append(pair[1])

    def fade_out(self):
        if not fast_preview:
            self.play(*[FadeOut(mobject) for mobject in self.mobjects_to_fade])
        else:
            self.remove(*self.mobjects_to_fade)

    def write_annotation(self, texts: list[str] | tuple[str, ...], duration: float = 0.5, font_size: int = 15):
        if self.annotation is not None:
            self.play(FadeOut(self.annotation))

        self.annotation = polish_latex_text(*texts, font_size=font_size).to_corner(RIGHT, buff=0.5)
        
        self.annotation = self.annotation.to_corner(DR, buff=0.5).shift(UP * 0.3)

        if fast_preview:
            self.add(self.annotation)
        else:
            self.play(FadeIn(self.annotation))
        self.wait(duration)

    def write_latex_annotation(self, texts: list[list[str]], duration: float = 0.5, font_size: int = 40):
        if self.annotation is not None:
            self.play(FadeOut(self.annotation))

        self.annotation = VGroup()
        for list_of_texts in texts:
            annotation = MathTex(*list_of_texts, font_size=font_size)
            annotation.set_color_by_tex("r", RED)
            annotation.set_color_by_tex("y", YELLOW)
            annotation.set_color_by_tex("x", BLUE)
            self.annotation.add(annotation)

        self.annotation.arrange(DOWN, buff=0.5)
        self.annotation.to_edge(RIGHT, buff=0.5)

        if fast_preview:
            self.add(self.annotation)
        else:
            self.play(FadeIn(self.annotation))
        self.wait(duration)

