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

import machine

class meeMainScreen:
    def __init__(self, wifi_on, receiving_on, account_on, g, bar, b, main_menu, wifi_connect):
        self.wifi_on = wifi_on
        self.reveiving_on = receiving_on
        self.wifi_connect = wifi_connect
        self.account_on = account_on
        ### utils
        self.bar = bar
        self.bar.set_title()
        self.b = b
        self.g = g
        self.mm = main_menu
    
    def main_set_bar_title(self):
        self.bar.set_title()

    def set_if_wifi_is_on(self):
        self.bar.set_if_wifi_is_on(self.wifi_connect.check_if_connected())
        self.wifi_on = self.wifi_connect.check_if_connected()
    
    def show_mainScreen(self):
        self.set_if_wifi_is_on()
        self.g.clean_global_buffer()
        if(self.account_on == False):
            self.screen_create_account()

        else:
            if(self.wifi_on == True):
                if(self.reveiving_on == True):
                    self.screen_stuff_receving()
                else:
                    self.screen_stuff_normal()
            else:
                self.screen_connect_to_wifi()
        self.g.show_global_buffer()
        
    def screen_stuff_receving(self):
        self.bar.show_bar() 
        self.g.write_text("receiving", 11, 15, 0x0004)
        self.g.write_text("[ON]", 31, 25, 0x0006)
        self.g.write_text("menu", 32, 55, 0x00a0)

    def screen_stuff_normal(self):
        self.bar.show_bar()
        self.g.write_text("receiving", 11, 15, 0x0004)
        self.g.write_text("[OFF]", 28, 25, 0x00a0)
        self.g.write_text("menu", 32, 55, 0x1001)
    
    def screen_connect_to_wifi(self):
        self.bar.show_bar()
        self.g.write_text("Connect", 18, 25, 0x1001)
        self.g.write_text("To Wi-Fi", 15, 35, 0x0005)
        self.g.write_text("menu", 32, 55, 0x0004)
    
    def screen_create_account(self):
        self.bar.show_bar()
        self.g.write_text("Create", 23, 25, 0x1001)
        self.g.write_text("an account", 8, 35, 0x1005)
        self.g.write_text("menu", 32, 55, 0x0004)
        
    def passFunc(self, *args):
        pass
    
    def enter_menu(self, *args):
        self.disable_MSbuttons()
        self.mm.main_menu_show_menu_list()
        self.mm.enable_MMbuttons()
        self.mm.show_mainMenu()
    
    def enable_MSbuttons(self, *args):
        self.b.enable_buttons(self.passFunc, self.passFunc, self.passFunc, self.enter_menu, self.passFunc, self.passFunc)
    def disable_MSbuttons(self, *args):
        self.b.disable_buttons()
