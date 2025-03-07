from manim import *
class MyScene(Scene):
    def construct(self):
        rate_functions = smooth
        circle = Circle(radius=0.5,color=WHITE)
        self.play(Create(circle))
        circle.move_to(UP*2)
        circle.scale(0.5)
        self.wait()

        square = Square(side_length=1,color=BLUE)
        self.play(Create(square))
        square.move_to(DOWN*2)
        square.scale(0.5)
        self.wait()
        
        rectangle = Rectangle(width=2,height=1,color=YELLOW)
        self.play(Create(rectangle))
        rectangle.move_to(RIGHT*2)
        rectangle.scale(0.5)
        self.wait()
        
        polygon= RegularPolygon(n=6)
        polygon.set_color(GREEN)
        self.play(Create(polygon))
        polygon.move_to(LEFT*2)
        polygon.scale(0.5)
        self.wait()

        text=Text("END",color=RED)
        self.add(text)
        self.wait()