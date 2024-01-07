import manim as mn
import numpy as np


class CreatePyramid(mn.Scene):
    def create_trapezoid(self, width, height):
        return mn.Polygon(
            [width / 2, 0, 0],
            [-width / 2, 0, 0],
            [-width / 2 - height / np.sqrt(3), -height, 0],
            [width / 2 + height / np.sqrt(3), -height, 0],
            fill_opacity=0.5,
            fill_color=mn.BLUE)

    def construct(self):
        # self.camera.background_color = mn.RED

        triangle1 = mn.Polygon(
            [1, 0, 0],
            [0, np.sqrt(3), 0],
            [-1, 0, 0],
            fill_opacity=0.5,
            fill_color=mn.BLUE)

        triangle1.shift(mn.UP)

        trapezoid1 = self.create_trapezoid(2, np.sqrt(3))
        trapezoid2 = self.create_trapezoid(4, np.sqrt(3))
        trapezoid3 = self.create_trapezoid(6, np.sqrt(3))

        trapezoid1.next_to(triangle1, mn.DOWN, buff=0)
        trapezoid2.next_to(trapezoid1, mn.DOWN, buff=0)
        trapezoid3.next_to(trapezoid2, mn.DOWN, buff=0)

        group = mn.VGroup(triangle1, trapezoid1, trapezoid2, trapezoid3)
        group.width = 5

        # self.add(group)
        # self.play(mn.Write(group))

        animations = [
            mn.FadeIn(group[0]),
            mn.FadeIn(group[1]),
            mn.FadeIn(group[2]),
            mn.FadeIn(group[3]),
        ]
        self.play(mn.AnimationGroup(*animations, lag_ratio=0.5))

        self.wait(1)
