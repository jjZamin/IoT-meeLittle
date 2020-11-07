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

from machine import Pin, SPI
import ssd1331
import time
import framebuf

print("\033[1;32;40m[ loaded module ]: " + "\033[1;37;40m meeGfxGlob " + "\033[0;37;40m")
print("\033[1;37;40m[ object ] =" + "\033[1;32;40m meeGfx\033[1;35;40m(): \033[0;37;40m")

###############################################################
#                       mee.Graphics                          #
#                                                             #
###############################################################
class meeGfx:
    def __init__(self):
        spi = SPI(mosi=Pin(23), miso= Pin(19), sck=Pin(18), polarity=1, phase=1)
        self.display = ssd1331.SSD1331(spi, dc=Pin(32), cs=Pin(5), rst=Pin(33))
        self.display.fill(0x0000)
        
        ### global buffer ###
        self.dispWidth = self.display.width
        self.dispHeight = self.display.height
        
        # ALL_buffer #
        self.global__buffer = bytearray(self.display.width*self.display.height * 2)
        self.global___frame__buffer = framebuf.FrameBuffer(self.global__buffer, self.display.width, self.display.height, framebuf.RGB565)
        
    def fill_display(self, color):
        self.display.fill(color)

    ### texts
    def write_text(self, text, x, y, color):
        self.global___frame__buffer.text(text, x, y, color)

    ### rects
    def filled_rect(self, x, y, w, h, c):
        self.global___frame__buffer.fill_rect(x, y, w, h, c)
        
    def just_rect(self, x, y, w, h, c):
        global jrecX, jrecY, jrecW, jrecH
        jrecX, jrecY, jrecW, jrecH = x, y, w, h
        self.global___frame__buffer.rect(x, y, w, h, c)    
    def fill_last_drawn_justrect(self, color):
        self.filled_rect(jrecX+1, jrecY+1, jrecW-2, jrecH-2, color)    
    def fill_last_drawn_justrect_R(self, part, color):
        if(part <= jrecW):
            self.filled_rect(jrecX+1, jrecY+1, part-1, jrecH-2, color)
        else:
            self.filled_rect(jrecX+1, jrecY+1, jrecW-2, jrecH-2, color)
    def fill_last_drawn_justrect_R(self, part, color):
        if(part <= jrecW):
            self.filled_rect(jrecX+1, jrecY+1, part-1, jrecH-2, color)
        else:
            self.filled_rect(jrecX+1, jrecY+1, jrecW-2, jrecH-2, color)
    def fill_justrect(self, x, y, w, h, color):
        self.filled_rect(x+1, y+1, w-2, h-2, color)
    
    ### lines
    def make_Vline(self, x, y, h, c):
        self.global___frame__buffer.vline(x, y, h, c)
    def make_Hline(self, x, y, h, c):
        self.global___frame__buffer.hline(x, y, h, c)
    def make_line(self, x1, y1, x2, y2, c):
        self.global___frame__buffer.line(x1, y1, x2, y2, c)
        
    ### pixels
    def draw_pixel(self, x, y, c):
        self.global___frame__buffer.pixel(x, y, c)

    def blit_global(self, x, y):
        self.global___frame__buffer.blit(self.global___frame__buffer, x, y)
    
    ### global buffer   
    def show_global_buffer(self):
        self.display.blit_buffer(self.global___frame__buffer, 0, 0, self.dispWidth, self.dispHeight)
    def clean_global_buffer(self):
        self.global___frame__buffer.fill(0x0000)
        
    def cut_and_move_rect(self, cutX, cutY, cutW, cutH, x, y):
        loc_rec_buff = bytearray(cutW * cutH * 2)
        loc_frame_rec_buff = framebuf.FrameBuffer(loc_rec_buff, cutW, cutH, framebuf.RGB565)
        start_loc = cutY * self.display.width * 2  + cutX * 2
        for u in range (0, cutH):
            loc_rec_buff[u*cutW*2 : u*cutW*2 + cutW*2] = self.global__buffer[start_loc:start_loc + cutW*2]
            self.global__buffer[start_loc:start_loc + cutW*2] = bytearray(cutW*2)
            start_loc += self.display.width*2
        self.global___frame__buffer.blit(loc_frame_rec_buff, x, y)

    def cut_and_move_text(self, cutX, cutY, letters, x, y, cutH=8):
        cutW = letters * 8 + 2 * (letters-1)
        loc_txt_buff = bytearray(cutW * cutH * 2)
        loc_frame_txt_buff = framebuf.FrameBuffer(loc_txt_buff, cutW, cutH, framebuf.RGB565)
        start_loc = cutY * self.display.width * 2  + cutX * 2
        for u in range (0, cutH):
            loc_txt_buff[u*cutW*2 : u*cutW*2 + cutW*2] = self.global__buffer[start_loc:start_loc + cutW*2]
            self.global__buffer[start_loc:start_loc + cutW*2] = bytearray(cutW*2)
            start_loc += self.display.width*2
        self.global___frame__buffer.blit(loc_frame_txt_buff, x, y)
        
        
    # Bresenham's algorithm for a circle    
    def _set_circle(self, xc, yc, x, y, color):
        self.draw_pixel(xc+x, yc+y, color); 
        self.draw_pixel(xc-x, yc+y, color); 
        self.draw_pixel(xc+x, yc-y, color); 
        self.draw_pixel(xc-x, yc-y, color); 
        self.draw_pixel(xc+y, yc+x, color); 
        self.draw_pixel(xc-y, yc+x, color); 
        self.draw_pixel(xc+y, yc-x, color); 
        self.draw_pixel(xc-y, yc-x, color);
    def draw_circle(self, xc, yc, r, color):
        x = 0
        y = r
        d = 3 - 2 * r
        self._set_circle(xc, yc, x, y, color)
        while y>=x:
            x+=1
            if(d > 0):
                y-=1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            self._set_circle(xc, yc, x, y, color)
    
    def filled_circle(self, xc, yc, r, color):
        while r > 0:
            x = 0
            y = r
            d = 3 - 2 * r
            r -= 1
            self._set_circle(xc, yc, x, y, color)
            while y>=x:
                x+=1
                if(d > 0):
                    y-=1
                    d = d + 4 * (x - y) + 10
                else:
                    d = d + 4 * x + 6
                self._set_circle(xc, yc, x, y, color)

