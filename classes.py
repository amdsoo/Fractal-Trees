import math
import random
import pygame
from pygame.locals import *
from declaration import *
import declaration as d
import method as m
from array import *
import os

pygame.font.init()

# basic font for user typed
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# small font for user typed
my_font_S = pygame.font.SysFont('Comic Sans MS', 12)


class World():
	def __init__(self):
		self.tile_list = []
		# load images
		'''grey_img = pygame.image.load('img/grey.png')'''
		colmax = screen_width // tile_size
		rowmax = screen_height// tile_size
		col_count = 0

		'''while col_count < colmax:
			# top level
			img = pygame.transform.scale(grey_img, (tile_size, tile_size))
			img_rect = img.get_rect()
			img_rect.x = col_count * tile_size
			img_rect.y = 0
			tile = (img, img_rect)
			self.tile_list.append(tile)

			# lowlevel
			img = pygame.transform.scale(grey_img, (tile_size, tile_size))
			img = pygame.transform.rotate(img, 180)
			img_rect = img.get_rect()
			img_rect.x = col_count * tile_size
			img_rect.y = rowmax* tile_size - tile_size
			tile = (img, img_rect)
			self.tile_list.append(tile)

			col_count +=1'''

	def draw(self, screen):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])

		# Write menu texts
		input_rect = pygame.Rect(tile_size, 0, 4 * tile_size, tile_size)
		pygame.draw.rect(screen, GREY, input_rect)
		text_surface = my_font.render("Level  / " + str(d.level_max_display), False, BLACK)
		screen.blit(text_surface, (input_rect.x + 5, 0))

class Tree:
	def __init__(self):

		# basic tree definition
		'''self.level_max = 2'''

		#initial color of the trunk
		# brown 105 , 75 , 55
		self.color_ini_R = 105
		self.color_ini_G = 75
		self.color_ini_B = 55

		#color of the last branches
		# green 42 , 222 ,33
		self.color_fin_R = 42
		self.color_fin_G = 222
		self.color_fin_B = 33

		#color of the leaves , last level
		# cherry blossom 255 ,71, 107
		self.color_leave_R = 25
		self.color_leave_G = 5
		self.color_leave_B = 245

		#some parameters to control the results
		self.color_variation = 50
		self.add_branch_deviation= True
		self.stump_ratio = 0.05

		# data
		# level (0)
		# branch_length (1),
		# branch_radius start (2)
		# branch_radius end(3)
		# cone_angle (4)
		# cone_angle_reference (5) //Relative to parent branch, or absolute angle.
		# axis_deviation (6) // a range of degree (+ ou -)
		# branch_max (7)
		# branch_length_deviation  (8)   // a % to diversify the length
		# branch curvature (9)   // a % of curvature of the bezier curv at the midpoint of the Length


		self.data = [
			[0, 220,  35,   30,   45,   "Relative", 0.1,   2,  0.5,  0.1],
			[1, 140,  18,   16,   90,   "Relative", 0.2,   3,  0.3,  0.2],
			[2,  90,  13,   11,   90,   "Relative", 0.2,   3,  0.2,  0.1],
			[3,  75,   9,    8,  100,   "Relative", 0.2,   3,  0.2,  0.3],
			[4,  30,   6,    4,  100,   "Relative", 0.2,   3,  0.2,  0.3],
			[5,  17,   4,    4,  100,   "Relative", 0.2,   3,  0.2,  0.2],
			[6,  11,   3,    3,  100,   "Relative", 0.4,   3,  0.9,  0.2],
			[7,   8,   6,    2,  150,   "Relative", 0.3,   7,  0.2,  0.2],
			[8,   4,   2,    1,   90,   "Relative", 0.2,   3,  0.2,  0  ],
			[9,   2,   1,    1,   90,   "Relative",   0,   2,    0,  0]
		]

	def draw(self, screen):
		# root of the tree

		i  = 1
		j  = 0
		k  = 0
		step =10
		start_node_list  = []
		end_node_list    = []
		next_node_list   = []
		level = 0
		number_of_branches_drawn = 0


		# the number of level to be displayed
		level_max = d.level_max_display

		#color delta interpolation
		delta_red   = (self.color_fin_R - self.color_ini_R) // level_max
		delta_green = (self.color_fin_G - self.color_ini_G) // level_max
		delta_blue  = (self.color_fin_B - self.color_ini_B) // level_max

		# intialize first point of the tree and vertical direction
		x0 = 800
		y0 = 700
		u0 = 0
		v0 = -1
		pt = [x0,y0,u0,v0]
		start_node_list.append(pt)

		color_r = self.color_ini_R
		color_g = self.color_ini_G
		color_b = self.color_ini_B


		# Draw tree segments start from level 0
		while level <= level_max:

			length                  = self.data[level][1]
			radius_s                = self.data[level][2]
			radius_e                = self.data[level][3]
			cone_angle              = self.data[level][4]
			cone_angle_reference    = self.data[level][5]
			axis_deviation          = self.data[level][6]
			branch_max              = self.data[level][7]
			branch_length_deviation = self.data[level][8]
			branch_curvature        = self.data[level][9]

			# compute delta_angle which is the angle between two consecutive branches of same node
			if branch_max == 1:
				delta_angle = 0
			else:
				delta_angle = cone_angle / (branch_max - 1)

			color = (color_r,color_g,color_b)

			for start_node in start_node_list:
			   i = 1
			   x0 = start_node[0]
			   y0 = start_node[1]
			   u0 = start_node[2]
			   v0 = start_node[3]

			   angle_start = cone_angle / 2

			   while i <= branch_max:
				   branch_stump = False
				   # compute new end point and direction, each branch is different
				   if self.add_branch_deviation:
					   length_tmp = length * (1 + random.uniform(-1, 1) * branch_length_deviation)
				   else:
					   length_tmp = length

				   # is it a dead extremity/stump?
				   if self.stump_ratio > 0 and level>0:
					   if random.random ()  < self.stump_ratio:
					       # we flag this branch as a Stump and we make it shorter
					       length_tmp = length_tmp * 2/3
					       branch_stump = True

				   # we add a bit of noise in the angle of each branch
				   angle_start_tmp = angle_start * (1 + random.uniform(-1, 1) * axis_deviation)

				   if cone_angle_reference == "Relative":
					   x1, y1, u1, v1 = m.compute_next_node(x0, y0, u0, v0, length_tmp, angle_start_tmp)
				   else:
					   #we force the verticality if mode is "Absolute" , but Angle_cone is still active
					   x1, y1, u1, v1 = m.compute_next_node(x0, y0, 0, 1, length_tmp, angle_start_tmp)

				   # add the end_node_list to continue if not stump
				   pt = [x1, y1, u1, v1]
				   if branch_stump is False:
					   next_node_list.append(pt)

				   end_node_list.append(pt)

				   #we continue to next branch, adding angle
				   angle_start = angle_start - delta_angle
				   i+=1

			   for end_node in end_node_list:
				   number_of_branches_drawn += 1

				   p0 = start_node[0],start_node[1]
				   p1 = end_node[0] ,end_node[1]

				   # drawing the branch
				   m.draw_branch(p0, p1, length_tmp, radius_s, radius_e, branch_curvature, color, screen)

			   # we clear this list for this specific Start node
			   end_node_list.clear()


			#clean up and prepare next node start
			start_node_list.clear()
			start_node_list = next_node_list.copy()
			next_node_list.clear()
			level+=1

			# we prepare a new color derived from previous color
			if level == level_max:
				color_r, color_g, color_b = self.color_leave_R ,self.color_leave_G ,self.color_leave_B
			else:
				color_r, color_g, color_b = color_r + delta_red, color_g + delta_green, color_b + delta_blue

		print("Drawn branches", number_of_branches_drawn)

	def draw_msg (self,screen,msg):
		newline = ":"
		lines = msg.split(newline)
		i=0
		for line in lines:
			text_surface = my_font_S.render(line, True, WHITE)
			screen.blit(text_surface, (screen_width-5*tile_size, screen_height-4*tile_size+i*15))
			i=i+1


class Grid():
	def __init__(self):
		pass

	def draw (self, screen):
		horiz  =  world_height // tile_size + 1
		vertic =  (world_width-800)  // tile_size + 1

		h, v = 0, 0

		test_indent = 9

		i = 0
		for line in range(0, horiz):
			pygame.draw.line(screen, (255, 255, 255), (0 , line * tile_size),
			                 (screen_width-800, line * tile_size))

			i = i + 1

		i = 0
		for line in range(0, vertic):
			pygame.draw.line(screen, (255, 255, 255), (line * tile_size , 0),
			                 (line * tile_size , screen_height))

			i = i + 1






