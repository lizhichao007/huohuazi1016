from manim import * 
class MyScene(Scene):
    # CONFIG = {
    #     "camera_config":{
    #         "background_image":r"C:\\Users\\l60071018\Desktop\\1.PNG"
    #     },
    # }
    def construct(self):

        # text1 = Text("ABCDEFG")
        # text2 = Text("a-b-c-d-e-f-g")
        # text3 = Text("C")
        # text4 = Text("D")

        #方向
        # text1.to_edge(UL)
        # self.add(text1)

        # text2.to_edge(UR)
        # self.add(text2)

        # text3.to_edge(DR)
        # self.add(text3)

        # text4.to_edge(DL)
        # self.add(text4)

        # 移动move_to
        # circle= Circle(radius=1,color=RED)
        # self.play(Create(circle))
        # circle.move_to(UP*2+4*RIGHT)
        # self.play(Create(circle))
        # self.play(FadeOut(circle))

        # 移动next_to
        # rectangle = Rectangle(height=2,width=1,color=YELLOW)
        # self.play(Create(rectangle))
        # rectangle.next_to(DOWN*2+4*LEFT)
        # self.play(Create(rectangle))

        # 平移
        # self.add(text1)
        # text2.shift(UP*2)
        # self.play(Write(text1),Write(text2),run_time = 2)

        # 旋转
        # self.play(Rotate(mobject=text2,angle=2 * PI))
        # self.wait(1)
        # self.play(FadeOut(text2))

        # text1.rotate(PI/2)
        # self.play(Write(text1),run_time = 1)

        # 翻转
        # self.play(Write(text1))
        # text1.flip(LEFT)
        # self.play(Write(text1))

        # dot1 = Dot()
        # dot2 = Dot()
        # dot2.shift(UP)
        # dot3 = Dot()
        # dot3.shift(DOWN)
        # # 单个演示
        # self.play(Write(dot1))
        # # 多个演示
        # self.play(*[
        #     Transform(i.copy(),j) for i ,j in zip ([dot1,dot1],[dot2,dot3])
        # ])
        # self.wait()

        # 渐变
        # circle = Circle(radius=1,color=RED)
        # rectangle = Rectangle(height=2,width=4,color=YELLOW)
        # self.play(FadeIn(circle))
        # self.play(FadeOut(circle))
        # #self.play(Transform(circle,rectangle))
        # # rate_functions  value: smooth,linear,there_and_back
        # self.play(ReplacementTransform(rectangle,circle),rate_functions=there_and_back,run_time = 5)

        # 无动画添加文字
        # hello = Text("hello,world!",color=RED_A)
        # how = Text("how are you ?",color=GREEN)
        # how.shift(DOWN)
        # self.add(hello)
        # self.wait()
        # #逐渐写出来的语句
        # self.play(Write(how))

        # 数组  不成立
        # demo = Text("A","B","C","D","E","F","G")
        # demo[0].set_color=(RED)
        # demo[1].set_color=(ORIGIN)
        # demo[2].set_color=(YELLOW)
        # demo[3].set_color=(GREEN)
        # demo[4].set_color=(BLUE)
        # demo[5].set_color=(GREEN)
        # demo[6].set_color=(PURPLE)
        # self.play(Write(demo))
        # self.wait()

        test = Text("test",color=RED)
        self.add(test)
        self.wait()











        
