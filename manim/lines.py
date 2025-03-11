from manim import *
class DynamicLineScene(Scene):
    def construct(self):
        # 创建起点和终点
        start_point = np.array([0, 0, 0])
        end_point = np.array([1, 0, 0])
        #circle = Circle(radius=2,color=BLUE)
        # 创建直线
        line = Line(start_point, end_point,color=YELLOW_B)
        self.add(line)

        # 定义更新函数
        def update_line(mob, alpha):
            new_end_point = np.array([5 * alpha, 0, 0])
            mob.put_start_and_end_on(start_point, new_end_point)
            #circle.set_radius(alpha*1)
            #circle.move_to(ORIGIN)

        # 创建动画
        animation = UpdateFromAlphaFunc(line,  update_line)
        # 播放动画
        self.play(animation, run_time=5)