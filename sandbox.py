from random import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_string('''
<Label>:
    font_size: 50
<Screen1>:
    name: 'first'
    GridLayout:
        rows: 2
        Label:
            text: root.name
        Button:
            text: 'Go to second'
            on_press: 
                root.manager.current = 'second'
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
                pos: 100, 100
                Label:
                    id: label1
                    text: input_written.text

<Screen2>:
    name: 'second'
    GridLayout:
        rows: 2
        Label:
            text: root.name
        Button:
            text: 'Go to first'
            on_press: 
                root.manager.current = 'first'

'''
)


class Screen1(Screen):
    def change_the_color(self, *args):
        label = self.ids.label1
        label.color = [random() for _ in range(3)] + [1]
        print(label.text)


class Screen2(Screen):
    pass


class TutorialApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='first'))
        sm.add_widget(Screen2(name='second'))
        return sm


TutorialApp().run()
