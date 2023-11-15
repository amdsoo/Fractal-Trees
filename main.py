# Ariel Morandy -  Sept 2023
import declaration as d
from declaration import *
import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog
import classes as c
import method as m
import userinterface as ui


# local variables

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tree Processor')

# basic font for Large Text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# small font for user typed
my_font_S = pygame.font.SysFont('Comic Sans MS', 12)

draw_relationships = False

# show a long message
display_long_message = False
long_message = ""

# list to manage button activity
button_list = []

# create the main Objects
world  = c.World()
grid   = c.Grid()
tree   = c.Tree()


# Main Button
button_simulation = ui.Button("simulation", tile_size, tile_size)
button_simulation.state = "pressed"

# List of Buttons
button_level_up = ui.Button("levelup", 30 * tile_size, tile_size)
button_level_up.state = "depressed"
button_level_down = ui.Button("leveldown", 31* tile_size, tile_size)
button_level_down.state = "depressed"

# game loop
run = True
while run:
	clock.tick(60)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
			button_simulation.click()
			ui.check_buttons (button_list)
			'''button_level_up.click()
			button_level_down.click()'''


	button_simulation.draw(screen)
	button_level_up.draw(screen)
	button_level_down.draw(screen)


	if button_simulation.state == "pressed":
		screen.fill(GREY)
		world.draw(screen)
		tree.draw(screen)
		button_simulation.state = "depressed"

	pygame.display.update()


pygame.quit()
