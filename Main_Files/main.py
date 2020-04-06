from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from Buttons_Images.Texts import *
from kivy.core.audio import SoundLoader
from time import *



import random
random.randint(5,8)
class Background(Widget):
    pass


class bubble(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_touch_down(self, touch):

        if touch.x >= self.x and touch.x <= (self.x + 255) and touch.y <= self.y + 255 and touch.y >= (self.y):

            self.sound = SoundLoader.load("Pop.wav")
            self.sound.play()
            for i in range(10):
                self.opacity -= .1
                sleep(.055)

        super().on_touch_down(touch)

    def on_touch_up(self, touch):


        sleep(1)
        self.opacity = 1

        super().on_touch_up(touch)


class MainApp(App):
    def build(self):
        self.load_kv("main.kv")


MainApp().run()