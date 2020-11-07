from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from paho_client import *
import os

## By Ghennadie Mazin

class meeMessages(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.I_SENT_IT_FLAG = False

        self.broker = ""
        self.topic = ""
        self.client_id = ""
        self.ids.BROKER_IP.text = ""
        self.ids.TOPIC.text = ""
        self.ids.CLIENT_ID.text = ""
        info = self.ids.BROKER_CONNECTED_INFO
        info.text = "[color=#FF0000]DISCONNECTED[/color]"

        self.show_text = self.ids.SHOW_MESSAGES

        if(os.path.isfile("log_in_dets.txt")):
            with open("log_in_dets.txt", "r") as f:
                d = f.read().split(",")
                self.user_name = d[0]
                self.password = d[1]
        else:
            self.user_name = ""
            self.password = ""
        self.client = PAHOclient(self)

    def ON_CONNECT(self):
        self.broker = self.ids.BROKER_IP.text
        self.topic = self.ids.TOPIC.text
        self.client_id = self.ids.CLIENT_ID.text
        info = self.ids.BROKER_CONNECTED_INFO

        self.client.set_brokerID(self.broker)
        self.client.set_user(self.user_name)
        self.client.set_password(self.password)
        self.client.set_topic(self.topic)
        self.client.set_clientID(self.client_id)
        self.client.INIT_CLIENT()
        self.client.set_on_funcs()
        self.client.INIT_USR_PASS()
        self.client.connect_to_broker()
        connected = self.client.return_is_connected()
        self.client.INIT_LOOP()
        self.client.subscribe_to_topic()

        if(connected):
            info.text = "[color=#00FF00]CONNECTED[/color]"
        else:
            info.text = "[color=#FF0000]DISCONNECTED[/color]"

    def ON_DISCONNECT(self):
        info = self.ids.BROKER_CONNECTED_INFO
        self.client.unsubscribe_topic()
        self.client.END_LOOP()
        self.client.disconnect_from_broker()
        connected = self.client.return_is_connected()

        if(connected):
            info.text = "[color=#00FF00]CONNECTED[/color]"
        else:
            info.text = "[color=#FF0000]DISCONNECTED[/color]"

    def ON_SEND(self):
        
        self.I_SENT_IT_FLAG = True
        topic = self.ids.TOPIC.text
        msg = self.ids.MESSAGE_INTPUT.text
        if(msg == "mee.clear()"):
            self.ids.MESSAGE_INTPUT.text = ""
            self.show_text.text = ""
            return

        self.ids.MESSAGE_INTPUT.text = ""
        self.client.publish_instant(topic, msg)
        self.show_text = self.ids.SHOW_MESSAGES
        self.show_text.text += "\n" + "[color=#00FF00]" + self.ids.CLIENT_ID.text + "[/color]: " + msg
        
        
    def ON_RECEIVE(self, topic, msg):
        ## showing messages

        if(self.I_SENT_IT_FLAG):
            self.I_SENT_IT_FLAG = False
        else:
            self.show_text = self.ids.SHOW_MESSAGES
            self.show_text.text += "\n" + "[color=#00FF00]" + topic + "[/color]: " + msg