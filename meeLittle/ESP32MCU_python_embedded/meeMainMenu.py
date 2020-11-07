###############################################################
#                                                             #
#                  ~    Written by    ~                       #
#                     Ghennadie Mazin                         #
#                                                             #
###############################################################
### --------------------------------------------------------###

###############################################################
#                       prints                                #
###############################################################
    
### template for "HELP()"
#print("\033[1;32;40m .FUNCTION \033[1;35;40m( .ARGUMENTS ): \033[0;37;40m"
#                        + ".EXPLANATION")

### template for "OTHER FUNCTION ACTIONS"
###print("\033[S;XX;YYm .DOES WHAT? \033[1;35;40m" + "some argument")
## XX: letter colors -> black: 30, red: 31, green: 32, yellow: 33, blue: 34, purple: 35, cyan: 36, white: 37
## YY: bg colors     -> same colors but numbers: 40, 41, 42, 43, 44, 45, 46, 47
## S: style:         -> pure: 0, bold: 1, underline: 2, negative: 3, negative2: 5

### --------------------------------------------------------###
import time
import _thread
from meeSendMsg import *
import meeWRfiles as RW
from meeWRfiles import *

class meeMainMenu:
    def __init__(self, wifi_on, g, k, b, m, bar, settings, MQTT):
        self.menuList = ['Send msg','Received','Settings']
        self.wifi_on = wifi_on
        self.MQTT = MQTT
        self.g = g
        ### utils
        self.k = k
        self.b = b
        self.bar = bar
        self.bar.set_title()
        self.m = m
        self.meeSendMsg = meeSendMsg(self.k, self.g)
        self.getMenuItem = self.m.get_menu_item_number()
        
        ### other sub/menus
        self.set = settings

    def main_menu_show_menu_list(self):
        self.m.set_menu_list(self.menuList)
        
    def show_mainMenu(self):
        self.g.clean_global_buffer()
        self.bar.show_bar()
        self.m.show_menu()
        self.g.show_global_buffer()
        
    def set_main_screen_object(self, obj):
        self.main_screen = obj
        
    def goUp(self, *args):
        self.m.go_up()
        self.show_mainMenu()
    def goDown(self, *args):
        self.m.go_down()
        self.show_mainMenu()
    def passFunc(self, *args):
        self.m.pass_func()
    
    def quit(self, *args):
        self.disable_MMbuttons()
        self.main_screen.main_set_bar_title()
        self.main_screen.enable_MSbuttons()
        self.main_screen.show_mainScreen()

    def start_receiving(self):
        self.MQTT.mee_receive()
    
    def enter(self, *args):
        self.getMenuItem = self.m.get_menu_item_number()
        #print("main_menu, menu item: " +str(self.getMenuItem))
        
        if(self.getMenuItem == 1):
            self.disable_MMbuttons()
            self.meeSendMsg.send_msg()
        elif(self.getMenuItem == 2):
            color = 0x0005
            REC_text = read_file("/messages/get_message.txt")
            
            REC_text = REC_text.replace("[","")
            REC_text = REC_text.replace("]","")
            REC_text = REC_text.replace(" ","")
            REC_text = REC_text.replace("'","")
            REC_text = REC_text.split(",")
            self.g.clean_global_buffer()
            Y = 0
        
            for j in REC_text:
                self.g.write_text(j, 0, Y, color)
                Y += 8
                if(color == 0x0005):
                    color = 0x0004
                else:
                    color = 0x0005
                if(Y >= 57):
                    Y = 0
                    self.REC_text = []
            self.g.show_global_buffer()
        elif(self.getMenuItem == 3):
            self.set.setting_show_menu_list()
            self.set.show_Settings()
            self.disable_MMbuttons()
            self.set.enable_Setbuttons()
        else:
            pass
        
    def enable_MMbuttons(self, *args):
        self.b.enable_buttons(self.quit, self.goUp, self.passFunc, self.enter, self.goDown, self.passFunc)
    def disable_MMbuttons(self, *args):
        self.b.disable_buttons()
