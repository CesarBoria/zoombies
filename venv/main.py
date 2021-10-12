from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from os.path import join


class mainScreen(GridLayout):
    label_text = StringProperty('Hello')
    img = join(r'C:\Users\Cesar Boria\ownCloud\Photos', 'Lake-Constance.jpg')
    def __init__(self, **kwargs):
        super(mainScreen, self).__init__(**kwargs)

    def kill(self):
        self.label_text = "Lets kill some motherfocker ZOOMBIES!!"


class zoombiesApp(App):
    def build(self):
        return mainScreen()


zoombiesApp().run()