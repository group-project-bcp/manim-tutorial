from manim import *

labels = [
    "- przyprostokątna leżąca naprzeciwko kąta α", 
    "- przyprostokątna leżąca przy kącie α", 
    "- przeciwprostokątna"
]

FIRST_COLOR = YELLOW
SECOND_COLOR = PURPLE

class RightTriangle(Scene):
    def construct(self):
        self.line_a = Line(UP*2, ORIGIN, color=BLUE)
        self.line_b = Line(ORIGIN, RIGHT*2, color=BLUE)
        self.line_c = Line(RIGHT*2, UP*2, color=BLUE)

        triangle = VGroup(self.line_a, self.line_b, self.line_c)
        triangle.shift(LEFT*4)
        self.play(Create(triangle))

        label_a = MathTex("a").next_to(self.line_a, LEFT)
        label_b = MathTex("b").next_to(self.line_b, DOWN)
        label_c = MathTex("c").next_to(self.line_c).shift(UP*0.2, LEFT)

        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait()

        angle = Angle(self.line_c, self.line_b, quadrant=(1,-1), radius=1, color=FIRST_COLOR, other_angle=False)
        label_alpha = MathTex("\\alpha").next_to(angle, RIGHT).shift(DOWN*0.15 + LEFT*0.3)

        self.play(Write(angle), Write(label_alpha))
        legend = VGroup(
            *[
                self.create_legend_line(label, name, scale=0.4)
                for label, name in zip(["a", "b", "c"], labels)
            ]
        )
        legend.arrange(DOWN, aligned_edge=LEFT)
        legend.to_corner(UP + RIGHT)

        self.play(FadeIn(legend))
        self.wait()

        sin_label = self.create_function("sin", "a", "c").next_to(legend, DOWN)
        self.play(FadeIn(sin_label), *self.color_lines("a", "c"))
        self.wait()

        self.clear_lines()
        cos_label = self.create_function("cos", "b", "c").next_to(sin_label, DOWN)
        self.play(FadeIn(cos_label), *self.color_lines("a", "c"))
        self.wait()

        self.clear_lines()
        tg_label = self.create_function("tg", "a", "b").next_to(cos_label, DOWN)
        self.play(FadeIn(tg_label), *self.color_lines("a", "c"))
        self.wait()

        self.clear_lines()
        ctg_label = self.create_function("ctg", "b", "a").next_to(tg_label, DOWN)
        self.play(FadeIn(ctg_label), *self.color_lines("a", "c"))
        self.wait()

    def create_legend_line(self, label, name, scale=1):
        label = MathTex(label)
        name = Text(name).scale(scale)
        line_group = VGroup(label, name)
        line_group.arrange(RIGHT, buff=0.2)  # arrange elements in the group with equal buffer
        return line_group
    
    def create_function(self, function, x, y):
        label = MathTex(f"{function}(\\alpha) =") #"\\frac{x}{y}".replace("x", x).replace("y", y)
        formula = MathTex("{x}".replace("x", x), "\\over", "{y}".replace("y", y))
        formula.set_color_by_tex(x, FIRST_COLOR)
        formula.set_color_by_tex(y, SECOND_COLOR)
        line_group = VGroup(label, formula)
        line_group.arrange(RIGHT, buff=0.2)  # arrange elements in the group with equal buffer
        return line_group
    
    def clear_lines(self):
        self.line_a.set_color(BLUE)
        self.line_b.set_color(BLUE)
        self.line_c.set_color(BLUE)

    def color_lines(self, letter_one, letter_two):
        to_return = []

        match letter_one:
            case "a":
                to_return.append(ApplyMethod(self.line_a.set_color, FIRST_COLOR))
            case "b":
                to_return.append(ApplyMethod(self.line_b.set_color, FIRST_COLOR))
            case "c":
                to_return.append(ApplyMethod(self.line_c.set_color, FIRST_COLOR))
        match letter_two:
            case "a":
                to_return.append(ApplyMethod(self.line_a.set_color, SECOND_COLOR))
            case "b":
                to_return.append(ApplyMethod(self.line_b.set_color, SECOND_COLOR))
            case "c":
                to_return.append(ApplyMethod(self.line_c.set_color, SECOND_COLOR))

        # if letter_one == "a" or letter_two == "a":
        #     to_return.append(ApplyMethod(self.line_a.set_color, FIRST_COLOR))
        
        # if letter_one == "b" or letter_two == "b":
        #     to_return.append(ApplyMethod(self.line_b.set_color, FIRST_COLOR))
        
        # if letter_one == "c" or letter_two == "c":
        #     to_return.append(ApplyMethod(self.line_c.set_color, FIRST_COLOR))
        

        return to_return