import declaration as d
from declaration import *


pygame.font.init()
# basic font for user typed
my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_small_font = pygame.font.SysFont('Comic Sans MS', 15)

button_width = tile_size*0.8
button_height =tile_size*0.8


class Button:
    def __init__(self, button_name, x, y):
        self.button_name = button_name
        self.color = LIGHTSHADE
        self.x = x
        self.y = y
        self.width = button_width
        self.height = button_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.state = "depressed"

        if self.button_name == "simulation":
            self.image = pygame.transform.scale(simu_on_img, (self.width, self.height))
            self.image_ns = pygame.transform.scale(simu_off_img, (self.width, self.height))

        '''if self.button_name == "levelup":
            self.image = pygame.transform.scale(levelup_img, (self.width, self.height))
            self.image_ns = pygame.transform.scale(levelup_img_ns, (self.width, self.height))

        if self.button_name == "leveldown":
            self.image = pygame.transform.scale(leveldown_img, (self.width, self.height))
            self.image_ns = pygame.transform.scale(leveldown_img_ns, (self.width, self.height))'''

    def draw(self, screen):
        # Call this method to draw the button on the screen if visible.
        if self.state == "depressed":
            self.color = LIGHTSHADE
            screen.blit(self.image_ns, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x , self.y))


    def click (self):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y) :
            print ("button clicked -> ", "Status before change", self.state)
            # special treatment for Simulation
            if self.button_name == "simulation":
                if self.state == "pressed":
                    self.state = "depressed"
                else:
                    self.state = "pressed"
            elif self.button_name == "levelup":
                if self.state == "pressed":
                    self.state = "depressed"
                else:
                    self.state = "pressed"
                    d.level_max_display = d.level_max_display +1
                    if d.level_max_display >9:
                        d.level_max_display = 9
                        print ("maximum level reached")
            elif self.button_name == "leveldown":
                if self.state == "pressed":
                    self.state = "depressed"
                else:
                    self.state = "pressed"

class ButtonPush (Button):
    def __init__(self, button_name, type, image ,maxval, minval, deltaval, x, y):
        Button.__init__(self, button_name, x, y)
        #3 possible choices : Boolean, Integer, Float
        if type == "Integer":
            self.type = "Integer"
            self.maxval = maxval
            self.minval = minval
            self.deltaval = 1
        elif type == "Float":
            self.type = "Float"
            self.maxval = 1.0
            self.minval = 0
            self.deltaval = 0.1
        elif type == "Boolean":
            self.type = "Boolean"
            self.maxval = True
            self.minval = False


def check_buttons (button_list):
    for button in button_list:
        button.state = "depressed"









