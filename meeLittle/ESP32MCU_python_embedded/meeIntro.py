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
from meeGfxGlob import *

class meeIntro:
    def __init__(self, color=0x0000):
        self.g = meeGfx()
        self.text = "mee.little"
        self.color = color
        self.startY_block = 6
        self.startY_text = self.startY_block + 4
        
    def show_intro(self):
        self.blink_rect()
        time.sleep_ms(300)
        self.show_title()
        time.sleep_ms(300)
        self.draw_face()
        time.sleep_ms(2000)
        
    def blink_rect(self):
        self.g.just_rect(8, self.startY_block, 10, 16, self.color)
        self.g.fill_last_drawn_justrect(0xffff)
        for x in range (0, 3):        
            self.g.show_global_buffer()
            if(x < 2):
                self.g.fill_display(0x0000)
    
    def show_title(self):
        y = 16
        for x in range (0, len(self.text)):
            if(x < len(self.text) - 1):
                self.g.cut_and_move_rect(y-8, self.startY_block, 10, 16, y, self.startY_block)
            else:
                self.g.cut_and_move_rect(y-8, self.startY_block, 10, 16, 97, self.startY_block) #out
                
            if(x <= 3):
                self.g.write_text(self.text[0:x+1], 8, self.startY_text, 0xffff)
            elif(x > 3):
                self.g.write_text(self.text[4:x+1], 40, self.startY_text, 0x0004)
            self.g.show_global_buffer()
            y+=8
            if(x == 3):
                time.sleep_ms(700)
        
    def draw_face(self):
        #self.g.write_text(self.text[0:len(self.text)], 8, self.startY_text, 0xffff)
        self.g.draw_circle(48, 45, 18, 0x1002)
        self.g.draw_circle(48, 45, 17, 0x0400)
        self.g.draw_circle(41, 40, 6, 0xffff)
        self.g.draw_circle(55, 40, 4, 0xffff)
        
        ## in_eyes
        self.g.draw_pixel(38, 40, 0x0004)
        self.g.draw_pixel(53, 40, 0x0005)
        self.g.show_global_buffer()  

        time.sleep_ms(800)
        self.g.draw_pixel(38, 40, 0x0000)
        self.g.draw_pixel(53, 40, 0x0000)
        self.g.draw_pixel(41, 40, 0x0004)
        self.g.draw_pixel(55, 40, 0x0005)
        self.g.show_global_buffer()

        ## smile
        time.sleep_ms(500)
        self.g.draw_pixel(55, 50, 0x1006)
        self.g.draw_pixel(54, 51, 0x1005)
        self.g.draw_pixel(53, 52, 0x1004)
        self.g.draw_pixel(52, 53, 0x1003)
        self.g.draw_pixel(51, 53, 0x1002)
        
        self.g.draw_pixel(54, 50, 0x1006)
        self.g.draw_pixel(53, 51, 0x1005)
        self.g.draw_pixel(52, 52, 0x1004)
        self.g.draw_pixel(51, 53, 0x1003)
        self.g.draw_pixel(50, 53, 0x1002)
        self.g.draw_pixel(49, 53, 0x1001)
        self.g.draw_pixel(48, 52, 0x1007)
        self.g.show_global_buffer()
        

