import gint as g

class ui:
    def rect(self,x1:int,y1:int,x2:int,y2:int,color):
        g.drect(x1,y1,x2,y2,color)
        g.dupdate()
    def text(self,x:int,y:int,content:str,color):
        g.dtext(x,y,color,content)
        g.dupdate()

def cls():
    g.dclear(g.C_WHITE)
    g.dupdate()

class Colors:
    Black = g.C_BLACK
    White = g.C_WHITE
    Red = g.C_RED
    Green = g.C_GREEN
    Blue = g.C_BLUE

def ScreenSaver(path_to_image:str = ""):
    cls()
    if path_to_image == "":
        DVD = [
            "                       ",
            "   ####    ####        ",
            "  #       #    #       ",
            "  #       #    #       ",
            "  #       ######   ### ",
            "  #       #            ",
            "  #       #            ",
            "   ###    #            ",
            "                       ",
            "  ####   #####  #   #  ",
            "  #   #  #      #   #  ",
            "  #   #  #      #   #  ",
            "  #   #  #####  #   #  ",
            "  #   #  #       # #   ",
            "  #   #  #       # #   ",
            "  ####   #####    #    ",
        ]
        DVD_WIDTH = 23
        DVD_HEIGHT = 16
    else:
        with open(path_to_image,"r") as f:
            DVD = f.readlines()
            DVD_WIDTH = max([len(line) for line in DVD])
            DVD_HEIGHT = len(DVD)
    
    def draw_logo(x, y, color=g.C_BLACK, bg=g.C_WHITE):
        for dy in range(DVD_HEIGHT):
            for dx in range(DVD_WIDTH):
                if 0 <= x+dx < g.DWIDTH and 0 <= y+dy < g.DHEIGHT:
                    pixel = DVD[dy][dx]
                    g.dpixel(x+dx, y+dy, color if pixel == '#' else bg)
    
    x, y = 50, 50
    dx, dy = 2, 2
    bg = g.C_WHITE
    fg = g.C_BLACK
    
    while True:
        g.dclear(bg)
        draw_logo(x, y, fg, bg)
        g.dupdate()

        # Move
        x += dx
        y += dy

        # Bounce
        if x <= 0 or x + DVD_WIDTH >= g.DWIDTH:
            dx = -dx
        if y <= 0 or y + DVD_HEIGHT >= g.DHEIGHT:
            dy = -dy
        # Exit if any key pressed
        ev = g.pollevent()
        if ev.type == g.KEYEV_DOWN and ev.key == g.KEY_EXIT:
            break
        
        