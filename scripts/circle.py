from manim import *
# 在代码中指定 ffmpeg 路径
config.ffmpeg_executable = "D:/Users/HUAWEI/miniforge3/envs/test/Library/bin/ffmpeg.exe"
class myscene(Scene):
    def construct(self):
        test_config = {
            "font_size": 48,
            "font": "Comic Sans MS"
        }
        #fill_opacity=1设置引用
        circle = Circle(radius=2,color=RED,fill_opacity=1)
        circle.set_fill(BLUE_B)
        
        title = Text("Create Circle",**test_config).next_to(circle,UP)
        desc = Text("No corners\tSmooth edge",**test_config).next_to(circle,DOWN)
        self.play(Write(title))
        #DrawBorderThenFill填充的方式
        self.play(DrawBorderThenFill(circle),run_time = 3)
        self.play(circle.animate(run_time=0.5).scale(1.2).scale(0.5))
        self.play(Write(desc))
