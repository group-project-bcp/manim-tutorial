import manim as mn
import numpy as np


class CreatePyramid(mn.Scene):
    def create_triangle(self, width, height, color=mn.BLUE):
        return mn.Polygon(
            [width / 2, 0, 0],
            [0, height, 0],
            [-width / 2, 0, 0],
            fill_opacity=0.5,
            fill_color=color)

    def create_trapezoid(self, width, height, color=mn.BLUE):
        return mn.Polygon(
            [width / 2, 0, 0],
            [-width / 2, 0, 0],
            [-width / 2 - height / np.sqrt(3), -height, 0],
            [width / 2 + height / np.sqrt(3), -height, 0],
            fill_opacity=0.5,
            fill_color=color)

    def create_pyramid(self, level_count=3):
        tip = self.create_triangle(2, np.sqrt(3))

        levels = []
        labels = []
        for i in range(level_count - 1):
            level = self.create_trapezoid(2 * (i + 1), np.sqrt(3))

            if i == 0:
                level.next_to(tip, mn.DOWN, buff=0)
            else:
                level.next_to(levels[i - 1], mn.DOWN, buff=0)

            levels.append(level)

            label = mn.Text(f"{i + 1}", font="Arial", stroke_width=0.5)
            label.next_to(level, mn.LEFT, buff=0)
            labels.append(label)

        group = mn.VGroup(tip, *levels, *labels)
        group.width = 4
        return group

    def construct(self):
        pyramid1 = self.create_pyramid(7)
        pyramid1.width = 5
        pyramid1.move_to(mn.ORIGIN)
        pyramid1.shift(mn.LEFT * 3.5)

        pyramid2 = self.create_pyramid(7)
        pyramid2.width = 5
        pyramid2.move_to(mn.ORIGIN)
        pyramid2.shift(mn.RIGHT * 3.5)

        # animations  = []
        # for i in range(len(pyramid)):
        #     animations.append(mn.FadeIn(pyramid[i]))

        # self.play(mn.AnimationGroup(*animations, lag_ratio=0.5))
        # self.wait(1)

        self.add(pyramid1)
        self.add(pyramid2)

