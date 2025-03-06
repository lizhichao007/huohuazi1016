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
        #填充
        circle.set_fill(PINK)

        #文字
        test = Text("hello world!",**text_config)
        desc = Text("hi,my friend.\n how are you?",**text_config).next_to(test,DOWN)

        #测试用例
        self.play(DrawBorderThenFill(circle),run_time=2)
        #self.play(Write(test))
        