from kivy.config import Config
# Set the window size to aapproximate an Android application
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '667')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.image import Image

import constants

class Task(Widget):

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)

        self.avatar = FloatLayout(
            size=(166, 139)
        )
        avatar_photo = Image(
            source=constants.avatar_fn,
            size=(100,100),
            pos=(self.avatar.size[0]/2-50, self.avatar.size[1]/2-50)
        )
        avatar_background = RoundedRectangle(
            pos=(0,0),
            size=self.avatar.size,
            radius=[(10, 10), (10, 10), (10, 10), (10, 10)]
        )

        self.avatar.add_widget(avatar_background)
        self.avatar.add_widget(avatar_photo)

        self.add_widget(self.avatar)


class TaskApp(App):
    def build(self):
        return Task()


if __name__ == '__main__':
    TaskApp().run()