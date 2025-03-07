from manim import *
import math

class Create3DSphere(ThreeDScene):
    def construct(self):
        # 设置三维视角 phi仰角 theta方位角
        self.set_camera_orientation(phi=75*math.pi/180,theta=45*math.pi/180)
        #创建三维坐标系
        axes = ThreeDAxes(
            x_length=8,
            y_length=8,
            z_length=8,
            color=WHITE
        )
        # 显示三维坐标系
        self.add(axes)
        
        # 创建并添加一个蓝色球体
        sphere = Sphere(radius=2, 
                        color=BLUE_B,
                        fill_opacity=0.5 #透明度
                        ).set_position(ORIGIN)
        self.add(sphere)
        self.play(Rotate(sphere,angle=2*PI,about_point=ORIGIN),run_time=4,rate_func=smooth)
        self.play(FadeOut(sphere))

        cube = Cube()
        self.add(cube)
        self.play(Rotate(cube,angle=PI/2,about_point=ORIGIN,run_time=5,rate_functions=smooth))
        self.play(FadeOut(cube,axes))
        self.wait()