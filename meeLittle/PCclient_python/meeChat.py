from meeLogin import *
import kivy
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from meeMessages import *
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require("1.11.1")

## By Ghennadie Mazin

## CHAT CLASS
class meeChat(App):
    def build(self):

        Window.size = (1000,600)      

        self.screen_manager = ScreenManager()
        ##connect page
        self.login = meeLogin(self)
        screen = Screen(name="Login")
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)        
        return self.screen_manager

    def go_to_messages(self):
        self.go_to_messages = meeMessages()
        screen = Screen(name="Messenger")
        screen.add_widget(self.go_to_messages)
        self.screen_manager.add_widget(screen)

if __name__ == "__main__":
   mee_chat = meeChat()
   mee_chat.run()