from manim import *
from parameters import WAIT_DURATION, fast_preview
from helper_functions import *
from horner_exercise import HornerExercise, exercises

class Horner(Scene):
    def construct(self):

        for i, exercise in enumerate(exercises):
            self.prepare_scene(i)
            self.horners_method(exercise=exercise)
            self.clear()
            self.wait()

    def prepare_scene(self, i):
        self.title = Text("Schemat Hornera").to_edge(UP)
        self.subtitle = Text(f"Przykład {i + 1}", font_size=20).next_to(self.title, DOWN)
        self.add(self.title)
        self.add(self.subtitle)
        self.annotation = None
        watermark = Text("Michał Cyran", color=WHITE, opacity=0.3).scale(0.2).to_corner(DR)
        self.add(watermark)
        self.wait()

        if i == 2:
            self.write_annotation((
                "Należy uważać, gdy dzielnik nie posiada",
                "wszystkich kolejnych potęg x",
                "(niektóre współczynniki wynoszą 0)."
            ))

    def horners_method(self, exercise: HornerExercise):
        arguments = [
            "(",
            *exercise.dividend,
            ") : (x ",
            "-" if exercise.divider > 0 else "+",
            str(abs(exercise.divider)),
            ")"
        ]

        equation = MathTex(*arguments).to_corner(UL).shift(DOWN * 1.4)
        # exercise.factors = [1, -4, 1, 6]
        # exercise.results = [1, -2, -3, 0]
        # exercise.divider = 2
        # exercise.calculations = [
        #     "1 * 2 + (-4)",
        #     "(-2) * 2 + 1",
        #     "(-3) * 2 + 6"
        # ]
        # exercise.result_text = ("1x^2", "-2x^1", "-3x^0")

        self.write(equation)

        self.table_data = [
            ["_" for _ in range(len(exercise.factors) + 1)],
            ["_" for _ in range(len(exercise.factors) + 1)],
        ]

        self.table = Table(self.table_data).scale(0.7)
        self.write(self.table)

        for i, factor in enumerate(exercise.factors):
            arrow = Arrow(equation[i + 1].get_center() + DOWN * 0.2, self.table[0][i + 1].get_center() + UP * 0.2, buff=0.1, color=YELLOW)
            
            if not exercise.is_shorten:
                self.write(arrow)

            self.table_data[0][i + 1] = str(factor)
            self.rewrite_table()
        
            self.wait(WAIT_DURATION)

            if not exercise.is_shorten:
                self.delete(arrow)

        arrow = Arrow(equation[-2].get_center() + DOWN * 0.2, self.table.get_entries((2, 1)).get_center() + UP * 0.2, buff=0.1, color=YELLOW)
        self.write(arrow)

        self.write_annotation(
            (
                "Wpisujemy tutaj liczbę, która jest odjęta",
                "od x w drugim nawiasie",
                "(uważamy na znak)."
            ), duration=2)
        
        self.table_data[1][0] = str(exercise.divider)
        self.rewrite_table()
        self.wait(WAIT_DURATION)
        self.delete(arrow)

        arrow = Arrow(self.table.get_entries((1, 2)).get_center() + DOWN * 0.2, self.table.get_entries((2, 2)).get_center() + UP * 0.2, buff=0.1, color=YELLOW)
        self.write(arrow)

        self.write_annotation(
            (
                "Pierwszy współczynnik przepisujemy",
                "z góry."
            ), duration=2)
        

        self.table_data[1][1] = str(exercise.results[0])
        self.rewrite_table()
        self.wait(WAIT_DURATION)
        self.delete(arrow)

        self.write_annotation(
            (
                "Teraz mnożymy wynik przez liczbę po lewej",
                "i dodajemy kolejny współczynnik."
            ), duration=2)
        

        for i, result in enumerate(exercise.results):
            if i == 0:
                continue

            arrow_1 = Arrow(self.table.get_entries((2, i + 1)).get_center(), self.table.get_entries((2, 1)).get_center(), color=YELLOW)
            self.write(arrow_1)
            
            arrow_2 = Arrow(self.table.get_entries((2, 1)).get_center(), self.table.get_entries((1, i + 2)).get_center(), color=YELLOW)
            self.write(arrow_2)
            self.wait(WAIT_DURATION)
            
            calculation = MathTex(exercise.calculations[i - 1]).to_edge(DOWN)
            self.write(calculation)
            self.wait(WAIT_DURATION)
            self.table_data[1][i + 1] = str(result)
            self.rewrite_table()
            self.wait(WAIT_DURATION)
            self.delete(calculation, arrow_1, arrow_2)

        self.write_annotation(
            (
                "Otrzymane wyniki to kolejne współczynniki",
                "wielomianu wynikowego.",
                "Zaczynamy od x do potęgi o 1 mniejszej niż",
                "w początkowym wielomianie."
            ), duration=2)

        result = MathTex(*exercise.result_text).next_to(self.table, DOWN, buff=1)
        self.write(result)

        for i in range(len(exercise.results) - 1):
            arrow = Arrow(self.table.get_entries((2, i + 2)).get_center(), result[i].get_center(), color=YELLOW)
            self.write(arrow)
            self.wait(WAIT_DURATION)
            self.delete(arrow)


    def write_annotation(self, texts: list[str, ...] | tuple[str, ...], duration: float = 0.5, font_size: int = 15):
        if self.annotation is not None:
            self.play(FadeOut(self.annotation))

        self.annotation = polish_latex_text(*texts, font_size=font_size).to_corner(RIGHT, buff=0.5)
        
        self.annotation = self.annotation.to_corner(DR, buff=0.5).shift(UP * 0.3)

        if fast_preview:
            self.add(self.annotation)
        else:
            self.play(FadeIn(self.annotation))
        self.wait(duration)

    def write(self, obj):
        if fast_preview:
            self.add(obj)
        else:
            self.play(Write(obj))

    def delete(self, *args):
        if fast_preview:
            self.remove(*args)
        else:
            self.play(FadeOut(*args))

    def rewrite_table(self):
        if fast_preview:
            self.remove(self.table)
            self.table = Table(self.table_data).scale(0.7)
            self.add(self.table)

        else:
            self.play(Transform(self.table, Table(self.table_data)))