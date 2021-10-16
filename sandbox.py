from random import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<Label>:
    font_size: 150
<ScatterWidget>:
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
''')


class ScatterWidget(BoxLayout):
    def change_the_color(self, *args):
        label = self.ids.label1
        label.color = [random() for _ in range(3)] + [1]
        print(label.text)


class TutorialApp(App):
    def build(self):
        return ScatterWidget()


TutorialApp().run()
