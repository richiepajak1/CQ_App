from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen


"""
variable names in the kivy file must be changed

Add tokens (images) to each category name to give it flare
or potentially change the font, size, color, etc.
"""


class HomeScreen(Screen):
    pass


class DriveScreen(Screen):
    """
    This class handles all information dealing with the drive screen.
    Any python code relating to this screen is handled here

    """


class KnowledgeScreen(Screen):
    """
    This class handles all information dealing with the drive screen.
    Any python code relating to this screen is handled here
    """


class StrategyScreen(Screen):
    """
    This class handles all information dealing with the drive screen.
    Any python code relating to this screen is handled here
    """


class ActionScreen(Screen):
    """
    This class handles all information dealing with the drive screen.
    Any python code relating to this screen is handled here
    """


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("CQ_App.kv")


class CQApp(App):
    def build(self):
        return presentation


CQApp().run()
