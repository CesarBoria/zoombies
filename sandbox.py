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
        Scatter:
            pos: 100, 100
            Label:
                text: input_written.text
''')


class ScatterWidget(BoxLayout):
    pass


class TutorialApp(App):
    def build(self):
        return ScatterWidget()


TutorialApp().run()