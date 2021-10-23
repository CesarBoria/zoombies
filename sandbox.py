from random import random

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

Builder.load_string('''
<Ball>:
    size: 100, 100
    canvas:
        Ellipse:
            pos: root.x_b, root.y_b
            size: self.size
<Label>:
    font_size: 50
    color: 1, 0, 1, 1
<Button>:
    color: 1, 0, 0, 1
    background_color: 0, 1, 0, 1
<Screen1>:
    name: 'first'
    GridLayout:
        rows: 2
        Label:
            text: root.name
        Button:
            text: 'Go to second'
            on_press: root.manager.current = 'second'
        BoxLayout:
            orientation: 'vertical'
            FloatLayout:
                TextInput:
                    id: input_written
                    text: 'Default'
                    size_hint_y: 0.2
                    multiline: False
                    font_size: self.height/2
                    on_text: root.change_the_color()
            Scatter:
                Label:
                    pos: self.width/2, self.height/2
                    id: label1
                    text: input_written.text
                    color: root.text_color
        Label:
            id: label2
            text: input_written.text[:3]
            color: root.text_color
<Screen2>:
    name: 'second'
    GridLayout:
        rows: 2
        cols: 2
        canvas:
            Color: 
                rgba: 1, 0, 0, 1        
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: root.name
        Button:
            text: 'Go to first'
            on_press: 
                root.manager.current = 'first'
        Button:
            text: 'Move!'
            # on_press: root.move_the_circle()
        BoxLayout:
            canvas:
                Color: 
                    rgba: 0, 0, 1, 1
                Rectangle:
                    pos: self.width, 0
                    size: self.width, self.height
                Color:
                    rgba: 1, 0, 0, 1
            
        Ball:
''')


class Ball(Widget):
    x_b = ObjectProperty(0)
    y_b = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s = [10, 10]
        with self.canvas:
            self.r = Rectangle(pos=(10, 10), size=self.s)
        self.velocity = [4, 2]
        self.velocity_b = [4, 2]
        Clock.schedule_interval(self.update, 1/60)
        Clock.schedule_interval(self.update_b, 1/60)

    def update(self, dt):
        x, y = self.r.pos
        if x + self.s[0] > self.width or x < 0:
            self.velocity[0] *= -1
        if y + self.s[0] > self.height or y < 0:
            self.velocity[1] *= -1
        self.r.pos = (x + self.velocity[0], y + self.velocity[1])

    def update_b(self, dt):
        print(f'self.x_b + 100: {self.x_b + 100}, self.width: {self.width}')
        if self.x_b  > self.width or self.x_b < 0:
            self.velocity_b[0] *= -1
        if self.y_b > self.height or self.y_b < 0:
            self.velocity_b[1] *= -1
        self.x_b += self.velocity_b[0]
        self.y_b += self.velocity_b[1]
        print(self.velocity_b[0])


class Screen1(Screen):
    text_color = ListProperty([1, 0, 0, 1])

    def change_the_color(self):
        self.text_color = [random() for _ in range(3)] + [1]


class Screen2(Screen):
    pass


class TutorialApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1())
        sm.add_widget(Screen2())
        return sm


TutorialApp().run()
