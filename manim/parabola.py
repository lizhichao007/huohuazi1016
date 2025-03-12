from manim import *

class ParabolaAnimation(Scene):
    def construct(self):
        # 定义抛物线的参数
        a = 1
        h = 0
        k = 0

        # 绘制坐标系
        ax = Axes(
            x_range=(-10, 10),
            y_range=(-10, 10),
            x_length=20,
            y_length=20,
        )

        # 定义抛物线函数
        def parabola_func(x):
            return a * (x - h) ** 2 + k

        # 创建抛物线图形
        parabola = ax.plot(parabola_func, color=BLUE)

        # 添加参数显示
        a_label = MathTex(f"a = {a}").to_corner(UL)
        h_label = MathTex(f"h = {h}").next_to(a_label, DOWN)
        k_label = MathTex(f"k = {k}").next_to(h_label, DOWN)

        self.add(ax, parabola, a_label, h_label, k_label)

        # 动画：改变 a 的值
        self.play(animate(a.set_value(0.5)).during(2),
                  animate(parabola).set_color(YELLOW).during(2))

        # 更新参数显示
        a_label = MathTex(f"a = {a.value}").to_corner(UL)
        h_label = MathTex(f"h = {h}").next_to(a_label, DOWN)
        k_label = MathTex(f"k = {k}").next_to(h_label, DOWN)
        self.remove(a_label, h_label, k_label)
        self.add(a_label, h_label, k_label)

        # 动画：改变 h 的值
        self.play(Animation(h.set_value(2)).during(2),
                  Animation(parabola).set_color(PINK).during(2))

        # 更新参数显示
        a_label = MathTex(f"a = {a.value}").to_corner(UL)
        h_label = MathTex(f"h = {h.value}").next_to(a_label, DOWN)
        k_label = MathTex(f"k = {k}").next_to(h_label, DOWN)
        self.remove(a_label, h_label, k_label)
        self.add(a_label, h_label, k_label)

        # 动画：改变 k 的值
        self.play(Animation(k.set_value(-3)).during(2),
                  Animation(parabola).set_color(GREEN).during(2))

        # 更新参数显示
        a_label = MathTex(f"a = {a.value}").to_corner(UL)
        h_label = MathTex(f"h = {h.value}").next_to(a_label, DOWN)
        k_label = MathTex(f"k = {k.value}").next_to(h_label, DOWN)
        self.remove(a_label, h_label, k_label)
        self.add(a_label, h_label, k_label)
        self.wait(2)