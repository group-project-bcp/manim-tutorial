import manim as mn
import numpy as np

mn.config.disable_caching = True


class CreatePyramid(mn.Scene):
    def create_triangle(self, width, height, color=mn.BLUE):
        return mn.Polygon(
            [-width / 2, 0, 0],
            [width / 2, 0, 0],
            [0, height, 0],
            [0, height, 0],
            fill_opacity=0.5,
            fill_color=color)

    def create_trapezoid(self, width, height, color=mn.BLUE):
        return mn.Polygon(
            [-(width / 2 + height / np.sqrt(3)), 0, 0],
            [width / 2 + height / np.sqrt(3), 0, 0],
            [width / 2, height, 0],
            [-width / 2, height, 0],
            fill_opacity=0.5,
            fill_color=color)

    def create_custom_pyramid(
            self,
            size: int,
            labels: [str] = None,
            colors: [mn.color] = None):
        group = []
        for i in range(size):
            color = colors[i] if colors else mn.BLUE
            label = labels[i] if labels else ""

            polygon: mn.Mobject
            if i == 0:
                polygon = self.create_triangle(2, np.sqrt(3), color=color)
            else:
                polygon = self.create_trapezoid(
                    2 * i, np.sqrt(3), color=color)
                polygon.next_to(group[i - 1][0], mn.DOWN, buff=0)

            text = mn.Text(label)
            text.font_size = 24
            text.move_to(polygon.get_center())

            group.append(mn.VGroup(polygon, text))

        return mn.VGroup(*group)

    def construct(self):
        # ========== Pyramid init ==========

        size = 3
        labels = [
            'Meat & Dairy Products',
            'Fruits & Vegetables',
            'Grain Products'
        ]
        colors = [mn.RED, mn.GREEN, mn.BLUE]

        pyramid = self.create_custom_pyramid(
            size,
            labels=labels,
            colors=colors
        )
        pyramid.move_to(mn.ORIGIN)

        animations = []
        for i in range(size):
            animations.append(mn.FadeIn(pyramid[i]))

        # ========== Title and subtitle ==========

        title = mn.Text("The new food pyramid")
        title.to_edge(mn.UP)
        # title.shift(mn.UP * 0.5)

        subtitle = mn.Text("1970s")
        subtitle.to_edge(mn.DOWN)
        # subtitle.shift(mn.DOWN * 0.5)

        # ========== Render ==========

        self.play(
            mn.AnimationGroup(
                mn.FadeIn(title),
                *animations,
                mn.FadeIn(subtitle),
                lag_ratio=0.5
            )
        )
        self.wait(3)

        # ========== Transform - levels gap grow ==========

        # 1 -> 2
        # 2 -> 3
        # 3 -> 1

        level_1, level_2, level_3 = pyramid

        self.play(mn.ApplyMethod(level_1.shift, mn.UP * 0.25),
                  mn.ApplyMethod(level_3.shift, mn.DOWN * 0.25))

        # ========== Transform - levels transform & subtitle hide ==========

        position_1 = level_1.get_center()
        position_2 = level_2.get_center()
        position_3 = level_3.get_center()

        new_polygon_1 = level_2[0].copy()
        new_polygon_1.color = level_1[0].color
        new_polygon_1.move_to(position_1)

        new_polygon_2 = level_3[0].copy()
        new_polygon_2.color = level_2[0].color
        new_polygon_2.move_to(position_2)

        new_polygon_3 = level_1[0].copy()
        new_polygon_3.color = level_3[0].color
        new_polygon_3.move_to(position_3)

        self.play(mn.Transform(level_1[0], new_polygon_1),
                  mn.Transform(level_2[0], new_polygon_2),
                  mn.Transform(level_3[0], new_polygon_3),
                  mn.FadeOut(subtitle))

        # ========== Transform - move & subtitle show ==========

        new_subtitle = mn.Text("2010s")
        new_subtitle.move_to(subtitle.get_center())

        self.play(mn.ApplyMethod(level_1.move_to, position_2),
                  mn.ApplyMethod(level_2.move_to, position_3),
                  mn.ApplyMethod(level_3.move_to, position_1),
                  mn.FadeIn(new_subtitle))

        # ========== Transform - levels gap shrink ==========

        self.play(mn.ApplyMethod(level_2.shift, mn.UP * 0.25),
                  mn.ApplyMethod(level_3.shift, mn.DOWN * 0.25))
        self.wait(3)
