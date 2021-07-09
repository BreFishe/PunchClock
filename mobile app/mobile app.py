import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import DataBase
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty



kv = Builder.load_file("stylesheet.kv")
db = DataBase("punches.txt")

class WindowManager(ScreenManager):
    gName = StringProperty("")
    pass


class MainWindow(Screen):
    #will store time in database
    pop = ObjectProperty(None)
    uName = ObjectProperty(None)

    def punch(self):
        string = self.uName.text
        if string is not "":
            punchInOut(string)
        else:
            pass

    def update2ndName(self):
        SecondWindow.updateName(self)

    def checkInput(self):
        string = self.uName.text
        if string is "":
            return -1
        else:
            return 1

    def invalidEntry(self):
        pop = Popup(title='invalidEntry',
                    content=Label(text='No info entered.'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()


class SecondWindow(Screen):
    #will show past punches

    def updateName(self):
        string = self.manager.get_screen("main").uName.text

    def on_enter(self,*args):
        string = self.manager.get_screen("main").uName.text
        #Updates Scrolling list with punch times
        if string is not "":
            self.ids.list.text = listFormat(str(punchList(string)))
            self.ids.name_label.text = "Hello " + string
        else:
            self.ids.name_label.text = "No Name Entered"
            self.ids.list.text = "Holding"


    pass


class ThirdWindow(Screen):
    #Display hours worked in work week

    pass

def punchList(name):
    result =  db.get_user(name)
    if result == -1:
        pass
    else:
        return result


def punchInOut(name):
    result = db.add_user(name)
    if result == 1:
        pass
    else:
        db.append_punch(name)

def listFormat(string):
    newString = ""
    for count, obj in enumerate(string.split("#")):
        if count < len(string.split("#"))-1:
            if count % 2 == 0:
                newString = newString +"In:    "+ str(obj).strip("[',] '") + "\n"
            else:
                newString = newString +"Out: "+ str(obj).strip("[',] '") + "\n"
    return newString

# def getUser():
#     pop = P()
#     pop.open()


class MyApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(MainWindow())
        sm.add_widget(SecondWindow())
        sm.add_widget(ThirdWindow())
        return sm

if __name__=="__main__":
    MyApp().run()