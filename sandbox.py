from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput


class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(text='Default', font_size=40, multiline=False, size_hint_y=0.1)
        f = FloatLayout()
        s = Scatter(center=(Window.width/2, Window.height/2))
        l = Label(text='Default', font_size=50, color=(1, 1, 0, 1))
        t.bind(text=l.setter('text'))

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(f)
        b.add_widget(t)

        return b


TutorialApp().run()