from manim import *
import numpy as np

def saddle_surface(u,v):
    x=u
    y=v
    z=(x**2-y**2)/1
    return (x,y,z)
saddle = Surface(
    saddle_surface,
    u_range=[-1,1],
    v_range=[-1,1],
    resolution=(50,50) #分辨率，数值越高，曲面越光滑
)
saddle.set_color(BLUE).set_opacity(0.8)

class SaddleSurfaceScene(ThreeDScene):
    def construct(self):
        self.add(saddle)
        self.set_camera_orientation(phi=60*DEGREES,theta=45*DEGREES)
        