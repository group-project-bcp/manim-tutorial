from manim import *

titles = {
    "arithmetic": "Ciag arytmetyczny",
    "geometric": "Ciag geometryczny"
}

labels = {
    "arithmetic": "+r",
    "geometric": "\\cdot q"
}

formulas = {
    "arithmetic": "a_{n} = a_{1} + (n-1)r",
    "geometric": "a_{n} = a_{1} \\cdot q^{n-1}"
}

class Series(Scene):
    def construct(self):
        self.intro()
        self.exercise_example()

    def intro(self):
        for series in ["arithmetic", "geometric"]:
            label_text = labels[series]
            formula_text = formulas[series]

            title = Tex(titles[series])
            title.to_edge(UP)
            self.play(Write(title))

            series = VGroup(*[MathTex(f"a_{i}").shift(RIGHT*i*2) for i in range(1, 7)], MathTex("\\dots").shift(RIGHT*14))
            series.to_edge(LEFT)
            self.play(Write(series), run_time=5)


            for i in range(5):
                a1 = series[i]
                a2 = series[i + 1]
                arrow = CurvedArrow(a1.get_center(), a2.get_center(), color=YELLOW)
                self.play(Create(arrow))

                label = MathTex(label_text).next_to(arrow, DOWN)
                self.play(Write(label))


            formula = MathTex(formula_text)
            formula.to_edge(DOWN)
            self.play(Write(formula))

            self.wait()
            self.clear()

    def exercise_example(self):
        title = Tex("Przyklad")
        title.to_edge(UP)
        self.play(Write(title))

        label_0 = Tex("Dany ciag jest arytmatyczny.").next_to(title, DOWN)
        label_1 = MathTex("a_{2} = 4, a_{4} = 10.").next_to(label_0, DOWN)
        label_2 = Tex("Znajdz roznice tego ciagu.").next_to(label_1, DOWN)

        self.play(Write(label_0), run_time=1)
        self.play(Write(label_1), run_time=1)
        self.play(Write(label_2), run_time=1)
        self.wait()

        a2 = MathTex("a_{2}").shift(LEFT*2)
        a4 = MathTex("a_{4}").shift(RIGHT*2)
        arrow = CurvedArrow(a2.get_center(), a4.get_center(), color=YELLOW)
        label = MathTex("+?").next_to(arrow, DOWN)

        self.play(Write(a2))
        self.play(Write(a4))
        self.play(Create(arrow))
        self.play(Write(label))
        self.wait()

        self.remove(label)
        
        a3 = MathTex("a_{3}")
        self.play(ReplacementTransform(arrow, a3))

        arrow = CurvedArrow(a2.get_center(), a3.get_center(), color=YELLOW)
        label = MathTex("+r").next_to(arrow, DOWN)
        
        arrow_2 = CurvedArrow(a3.get_center(), a4.get_center(), color=YELLOW)
        label_2 = MathTex("+r").next_to(arrow_2, DOWN)

        self.play(Create(arrow))
        self.play(Write(label))
        self.play(Create(arrow_2))
        self.play(Write(label_2))
        self.wait()

        self.remove(label, label_2)
        self.remove(arrow_2)

        arrow_2 = CurvedArrow(a2.get_center(), a4.get_center(), color=YELLOW)
        label = MathTex("+2r").next_to(arrow_2, DOWN)
        self.play(ReplacementTransform(arrow, arrow_2))
        self.play(Write(label))

        self.remove(a3)
        self.wait()

        equation = MathTex("a_{2} + 2r = a_{4}").to_edge(DOWN)
        self.play(Write(equation))

        self.wait()
        trasnformed_equation = MathTex("4 + 2r = 10").to_edge(DOWN)
        self.play(ReplacementTransform(equation, trasnformed_equation))
        
        self.wait()
        simplified_equation = MathTex("2r = 6").to_edge(DOWN)
        self.play(ReplacementTransform(trasnformed_equation, simplified_equation))

        self.wait()
        solution = MathTex("r = 3").to_edge(DOWN)
        self.play(ReplacementTransform(simplified_equation, solution))
    
        self.wait()
        self.clear()