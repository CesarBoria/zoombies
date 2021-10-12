from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class mainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(mainScreen, self).__init__(**kwargs)
        self.cols = 2
        b = Button(text='Press me!', on_press=self.kill)
        self.add_widget(b)
        self.l = Label(text='Hello world')
        self.add_widget(self.l)

    def kill(self, instance):
        self.l.text = "Lets kill some motherfocker ZOOMBIES!!"


class zoombiesApp(App):
    def build(self):
        return mainScreen()


zoombiesApp().run()