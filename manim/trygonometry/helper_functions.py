from manim import *


def polish_latex_text(*args, **kwargs):
    group = VGroup()
    font_size = 20
    if "font_size" in kwargs.keys():
        font_size = kwargs["font_size"]

    for arg in args:
        if "\\" in arg:
            group.add(MathTex(arg, font_size=font_size + 10))  # MathTex is a bit smaller than Text
        else:
            group.add(Text(arg, font_size=font_size))
    group.arrange(DOWN)
    return group
