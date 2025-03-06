from manim import *

config.ffmpeg_executable = "D:/Users/HUAWEI/miniforge3/envs/test/Library/bin/ffmpeg.exe"

class demo(Scene):
    def construct(self):
        #字体实例
        text_config = {
            "font_size":48,
            "font":"Comic Sans MS"
        }

        #创建圆
        circle = Circle(radius=2,color=BLUE,fill_opacity=1)
        circle.set_fill(PINK) #填充

        #创建正方形
        square = Square(side_length=2,color=RED,fill_opacity=1)
        square.set_fill(YELLOW)

        #创建矩形
        rectangle = Rectangle(width=2,height=3,color=GREEN,fill_opacity=1)
        rectangle.set_fill(GREEN_B)

        #文字
        test = Text("hello world!",**text_config)
        desc = Text("hi,my friend.\n how are you?",**text_config).next_to(test,DOWN)
        start = Text("start",**text_config)
        end = Text("end",**text_config)

        #创建一条直线
        line = Line(start=ORIGIN,end=(5,0,0),color=YELLOW_A,stroke_width=3)

        #创建sin(x)函数
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )
        curve = axes.plot(
            lambda x: np.sin(x),
            color=RED,
            x_range=[-5, 5]
        )

        #测试用例

        #=====开始=====
        self.play(Write(start))
        self.play(FadeOut(start))

        # self.play(DrawBorderThenFill(circle),run_time=2)
        # self.play(FadeOut(circle))

        # self.play(Write(test))
        # self.play(Write(desc))
        # self.play(FadeOut(test,desc),set_time=2)
        
        # self.play(Create(square))
        # self.play(Transform(square,circle))
        # self.play(FadeOut(square)) #choice is master, is not slave.

        # self.play(DrawBorderThenFill(rectangle))
        # self.play(ScaleInPlace(rectangle,scale_factor=0.5))
        # self.play(FadeOut(rectangle))

        # polygon= RegularPolygon(n=6)
        # polygon.set_color(GREEN)
        # self.play(Rotate(polygon,angle=2*PI,about_point=ORIGIN,duration=2))
        # self.play(FadeOut(polygon))

        # self.play(Create(line))
        # self.play(FadeOut(line))

        self.add(axes, curve)
        self.play(Create(curve))
        self.play(FadeOut(curve,axes))


        #=====结束=====
        self.play(Write(end))
        self.play(FadeOut(end))