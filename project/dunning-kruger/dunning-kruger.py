import manim as mn

mn.config.disable_caching = True


class CreateDunningKruger(mn.Scene):
    def construct(self):

        # ========== Title ==========

        title = mn.Text("Dunning-Kruger Effect", font_size=24)
        title.to_edge(mn.UP)

        # self.play(mn.FadeIn(title))
        self.add(title)

        # ========== Axes ==========

        axes = mn.Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            tips=True,
            axis_config={"include_numbers": False, "include_ticks": False},
        )

        # self.play(mn.Create(axes))
        self.add(axes)

        # ========== X labels ==========

        x_start_label = mn.MathTex("Know\ nothing", font_size=24)
        x_start_label.next_to(
            axes.x_axis.get_start(),
            direction=mn.DOWN,
            aligned_edge=mn.LEFT
        )

        x_mid_label = mn.MathTex(
            "Competence", font_size=36)
        x_mid_label.next_to(
            axes.x_axis.get_midpoint(),
            direction=mn.DOWN,
            aligned_edge=mn.ORIGIN,
        )

        x_end_label = mn.MathTex("Guru", font_size=24)
        x_end_label.next_to(
            axes.x_axis.get_end(),
            direction=mn.DOWN,
            aligned_edge=mn.RIGHT)

        # self.play(
        #     mn.FadeIn(x_start_label),
        #     mn.FadeIn(x_mid_label),
        #     mn.FadeIn(x_end_label)
        # )
        self.add(x_start_label, x_mid_label, x_end_label)

        # ========== Y labels ==========

        y_start_label = mn.MathTex("Low", font_size=24)
        y_start_label.next_to(
            axes.y_axis.get_start(),
            direction=mn.LEFT,
            aligned_edge=mn.DOWN,
        )

        y_mid_label = mn.MathTex(
            "Confidence", font_size=36
        ).rotate(90 * mn.DEGREES)
        y_mid_label.next_to(
            axes.y_axis.get_midpoint(),
            direction=mn.LEFT,
            aligned_edge=mn.ORIGIN,
        )

        y_end_label = mn.MathTex("High", font_size=24)
        y_end_label.next_to(
            axes.y_axis.get_end(),
            direction=mn.LEFT,
            aligned_edge=mn.UP)

        # self.play(
        #     mn.FadeIn(y_start_label),
        #     mn.FadeIn(y_mid_label),
        #     mn.FadeIn(y_end_label)
        # )
        self.add(y_start_label, y_mid_label, y_end_label)

        # ========== Line ==========

        points = [
            (0, 0),
            (1, 8),
            (2, 2),
            (4, 2),
            (6, 5),
            (8, 7),
            (10, 8),
        ]

        path = mn.VMobject()
        path.set_points_smoothly([axes.c2p(x, y) for x, y in points])

        # self.play(mn.Create(path))
        self.add(path)

        # ========== Wait ==========

        self.wait(5)

        # ========== Lines ==========

        # axes.start_new_path(axes.c2p(0, 0))
        # axes.add_line_to(axes.c2p(1, 8))
        # axes.add_line_to(axes.c2p(2, 1))
        # axes.add_line_to(axes.c2p(4, 2))
        # axes.add_line_to(axes.c2p(6, 4))
        # axes.add_line_to(axes.c2p(8, 6))
        # axes.add_line_to(axes.c2p(10, 8))

        # ========== Function ==========

        # graph = axes.plot(
        #     lambda x: x ** 2,
        #     x_range=[0, 10],
        #     use_smoothing=False
        # )
        # self.add(axes, graph)

        # ========== Numpy ===========

        # x, y = [0, 1, 2, 4, 6, 8, 10], [0, 8, 1, 2, 4, 6, 8]
        # points = mn.VGroup()

        # for i in range(len(x)):
        #     points += mn.Dot(axes.c2p(x[i], y[i])).scale(1)

        # plt0 = np.polyfit(x, y, deg=6)[0]
        # plt1 = np.polyfit(x, y, deg=6)[1]
        # plt2 = np.polyfit(x, y, deg=6)[2]
        # plt3 = np.polyfit(x, y, deg=6)[3]
        # plt4 = np.polyfit(x, y, deg=6)[4]
        # plt5 = np.polyfit(x, y, deg=6)[5]
        # plt6 = np.polyfit(x, y, deg=6)[6]

        # def reg_eq(x): return plt6 + plt5*x + plt4*x**2 + \
        #     plt3*x**3 + plt2*x**4 + plt1*x**5 + plt0*x**6

        # plt = axes.plot(reg_eq)
        # self.add(points)
        # self.add(plt)
