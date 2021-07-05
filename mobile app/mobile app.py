import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
#from database import Database
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainWindow(Screen):
    #def clockInOut(self):
    #will store time in database

    def showPop(self):
        print("Open!")
        getUser()


class SecondWindow(Screen):
    #will show past punches

    def showPop(self):
        print("Open!")
        getUser()

    pass


class ThirdWindow(Screen):
    #Display hours worked in work week

    def showPop(self):
        print("Open!")
        getUser()

    pass


class WindowManager(ScreenManager):
    pass


class P(Popup):
    username = ObjectProperty(None)

    def assignName(self):
        username = self.username.text
        global gName
        gName = username
        print(username)

    pass


kv = Builder.load_file("stylesheet.kv")


def getUser():
    pop = P()
    pop.open()


class MyApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    MyApp().run()