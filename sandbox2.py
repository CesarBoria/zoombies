from kivy.app import App
from kivy.lang import Builder
from kivy.properties import Clock, NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

Builder.load_string('''
<Ball2>:
    canvas.before:
        Color: 
            rgba: 1, 0, 0, 1
        Rectangle:
            # size: 10, 10
            pos: root.x_pos, 100
        
''')


class Ball(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.r = Rectangle(pos=(10, 10), size=(100, 100))
        self.velocity = [4, 3]
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        x, y = self.r.pos
        if x + 100 > self.width or x < 0:
            self.velocity[0] *= -1
        if y + 100 > self.height or y < 0:
            self.velocity[1] *= -1
        self.r.pos = (x + self.velocity[0], y + self.velocity[1])


class Ball2(Widget):
    x_pos = NumericProperty(10)
    # y = NumericProperty(10)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        self.x_pos += 4


class Main(App):
    def build(self):
        return Ball2()


obj = Main()
obj.run()