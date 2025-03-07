from manim import *

import numpy as np

class Saddlesurface(Scene):
    def construct(self):
        # 定义参数范围
        x_range = [-5, 5, 0.25]
        y_range = [-5, 5, 0.25]
        
        # 定义马鞍面的参数方程
        def saddle_func(x, y):
            return (x, y, (x**2 - y**2)/5)
        
        # 创建曲面
        saddle = ParametricSurface(
            saddle_func,
            x_range=x_range,
            y_range=y_range,
            checkerboard_colors=[BLUE, GREEN],
            resolution=(20, 20)
        )
        
        # 添加曲面到场景
        self.add(saddle)
        
        # 设置相机视角
        self.camera = ThreeDCamera()
        self.camera.set_euler_angles(theta=45*DEGREES, phi=60*DEGREES)
        
        # 添加坐标轴
        axes = ThreeDAxes()
        self.add(axes)
        
        # 设置背景颜色
        self.background_color = BLACK

        # 添加一些文本说明
        text = Text("马鞍面", font_size=24).to_corner(UL)
        self.add(text)