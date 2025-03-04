from manim import *
class MyScene(Scene):
    def construct(self):
        text = Text("Create Circle",color=WHITE)
        self.play(FadeIn(text))
        circle=Circle(radius=2,color=WHITE)
        self.play(Create(circle))
        self.wait(1)
