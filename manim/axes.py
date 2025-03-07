from manim import *
class My_axes(Scene):
    def construct(self):
        axes = Axes(
            x_axis_config={"unit_size":0.5},
            x_range=[0,5],
            y_axis_config={"unit_size":1},
            y_range=[0,5]
        )
        self.add(axes)