from random import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty

Builder.load_string('''
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
        Label:
            text: root.name
        Button:
            text: 'Go to first'
            on_press: 
                root.manager.current = 'first'

''')


class Screen1(Screen):
    text_color = ListProperty([1, 0, 0, 1])

    def change_the_color(self, *args):
        self.text_color = [random() for _ in range(3)] + [1]
        # label = self.ids.label1
        # label.color = self.color
        # label2 = self.ids.label2
        # label2.color = self.color
        # print(label.text)


class Screen2(Screen):
    pass


class TutorialApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1())
        sm.add_widget(Screen2())
        return sm


TutorialApp().run()
