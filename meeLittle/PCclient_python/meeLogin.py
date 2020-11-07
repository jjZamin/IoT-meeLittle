from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import os

class meeLogin(BoxLayout):
    def __init__(self, parent, **kwargs):
            super().__init__(**kwargs)
            self.mee_chat = parent

    def validate_user(self):

        username = self.ids.username_field.text
        password = self.ids.password_field.text
        info = self.ids.log_in_info

        with open("log_in_dets.txt", "w") as f:
            f.write(f"{username},{password}")

        if(username == "jack" and password == "1234"):
            info.text = "[color=#00FF00]Logged in successfully![/color]"
            self.ids.username_field.text = ""
            self.ids.password_field.text = ""
            self.mee_chat.go_to_messages()
            self.mee_chat.screen_manager.current = "Messenger"
        else:
            info.text = "[color=#FF0000]Wrong password or username[/color]"
            self.ids.username_field.text = ""
            self.ids.password_field.text = ""
