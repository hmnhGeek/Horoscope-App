from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

import horoscope as cope
import threading
import os

Builder.load_file("blueprint.kv")


class home(Screen):
    def load_horoscope(self, zodiac):
        self.manager.current = "loading_screen"
        threading.Thread(target=lambda: self.update(zodiac)).start()

    def update(self, zodiac):
        try:
            predcn = cope.horoscope.get_prediction(zodiac)
            sm.get_screen("results").set_heading(zodiac)
            sm.get_screen("results").set_label("\n\n"+predcn)
            self.manager.current = "results"
        except:              
            content = Button(text="No Internet\nTap to close!")
            popup = Popup(title="No Internet Connection!!", content=content, auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()
            self.manager.current = "homepage"

class Loading(Screen):
    pass

class ResultScreen(Screen):
    def set_heading(self, data):
        self.ids.heading.text = data.capitalize() 
    def set_label(self, data):
        self.ids.result_label.text = data

class AboutAstroHoroscope(Screen):
    def load(self):
        f = open("about.txt", "r")
        about_data = f.read()
        f.close()

        return about_data

class AllZodiacs(Screen):
    def load_all(self):
        zodiac_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "zodiacs/zodiacs.txt"))
        f = open(zodiac_file, "r")
        lines = f.readlines()
        f.close()

        string = "\n\n".join(lines)
        
        return string

sm = ScreenManager(transition=NoTransition())
sm.add_widget(home(name="homepage"))
sm.add_widget(Loading(name="loading_screen"))
sm.add_widget(ResultScreen(name="results"))
sm.add_widget(AboutAstroHoroscope(name="about"))
sm.add_widget(AllZodiacs(name="all"))

class AstroHoroscope(App):
    def build(self):
        return sm

#if __name__ == '__main__':
AstroHoroscope().run()
