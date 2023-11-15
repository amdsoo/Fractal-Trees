import pygame

# Track current Level Displayed
level_max_display = 5

cargo_list = []
machine_list = []

deltax = 0
deltay = 0

# structure of relationship
# machine1, connector1 IN name, machine2, connector2 OUT name, Flag
# Flag is not used and default is True
relationship_list = []

# define game variables
tile_size = 50
screen_width = 1600
screen_height = 800

world_width = 1600
world_height = 800

scroll_step = tile_size

# Define some colors
BLACK = (0  ,  0,  0)
WHITE = (255,255,255)

RED   = (255,  0,  0)
GREEN = (0  ,255,  0)
BLUE  = (0  ,0 , 255)

YELLOW  = (255,255,  0)
CYAN    = (0  ,255,255)
MAGENTA = (255,  0,255)

LIGHTSHADE = (170, 170, 170)
DARKSHADE = (100, 100, 100)

RUSTY = (99, 11, 27)
GREY = (126,132,140)

# mouse click index
LEFT = 1
RIGHT = 3

# initialisation of images paths

simu_off_img = pygame.image.load('img/simulationOFF.bmp')
simu_on_img = pygame.image.load('img/simulationON.bmp')

levelup_img = pygame.image.load('img/img_up.png')
levelup_img_ns = pygame.image.load('img/img_up_ns.png')

leveldown_img = pygame.image.load('img/img_down.png')
leveldown_img_ns = pygame.image.load('img/img_down_ns.png')

