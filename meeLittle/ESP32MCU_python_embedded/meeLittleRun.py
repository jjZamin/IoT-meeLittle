###############################################################
#                                                             #
#                  ~    Written by    ~                       #
#                     Ghennadie Mazin                         #
#                                                             #
###############################################################
### --------------------------------------------------------###

from meeGfxGlob import *
from meeButtons import *
from meeKeys import *
from meeBar import *
from meeMenu import *
from meeMainScreen import *
from meeMainMenu import *
from meeSettings import *
from meeIntro import *
from meeWiFiMenu import *
from meeWiFiConnect import *
from meeMQTT import *
import _thread

class meeLittleRun:
    def __init__(self):
        self.account_on = True
        self.receiving_on = True
        self.intro = meeIntro()
        
        self.gfx = meeGfx()
        
        self.wifi_connect = meeWiFiConnect(self.gfx)
        self.wifi_on = False
        self.MQTT = meeMQTT(self.gfx)
        self.menu = meeMenu(self.gfx)
        self.menu_bar = meeBar(self.wifi_on, self.gfx)
        self.buttons = meeButtons()
        self.keys = meeKeys(self.buttons, self.gfx, self.MQTT)
        self.menu_WiFi = meeWiFiMenu(self.wifi_on, self.keys, self.gfx, self.buttons, self.menu, self.menu_bar, self.wifi_connect)
        self.menu_settings = meeSettings(self.wifi_on, self.keys, self.gfx, self.buttons, self.menu ,self.menu_bar, self.menu_WiFi)
        
        self.main_menu = meeMainMenu(self.wifi_on, self.gfx, self.keys, self.buttons, self.menu, self.menu_bar, self.menu_settings, self.MQTT)
        self.main_screen = meeMainScreen(self.wifi_on, self.receiving_on, self.account_on, self.gfx, self.menu_bar, self.buttons, self.main_menu, self.wifi_connect)

        self.keys.set_main_screen_object(self.main_screen)
        self.menu_WiFi.set_main_screen_object(self.main_screen)
        self.wifi_connect.set_main_screen_object(self.main_screen)
        self.MQTT.set_main_screen_object(self.main_screen)
        self.main_menu.set_main_screen_object(self.main_screen)
        self.menu_settings.set_main_screen_object(self.main_screen)
        
    def start_receiving(self):
        self.MQTT.mee_receive()        
        
    def main_screen_on(self):
        self.intro.show_intro()
        self.wifi_connect.connect_to_wifi()
        _thread.start_new_thread(self.start_receiving, ())



