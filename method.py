import random
import math
import declaration as d
import classes as c
from declaration import *

# basic font for user typed
pygame.font.init()
my_font_S = pygame.font.SysFont('Comic Sans MS', 12)

def compute_next_node (x0, y0, u0, v0, length, angle_deg):
	# method to find next node based on origin, axis and
	angle = -angle_deg * math.pi / 180

	u1 = (math.cos(angle) * u0 - math.sin(angle) * v0)
	v1 = (math.sin(angle) * u0 + math.cos(angle) * v0)
	x1 = x0 + length * u1
	y1 = y0 + length * v1

	return x1, y1, u1, v1

def compute_bezier_pt_on_crv (p1,p2,p3,t):
	# bezier curve three points

	x1, y1 = p1[0],p1[1]
	x2, y2 = p2[0],p2[1]
	x3, y3 = p3[0],p3[1]


	xp = (1-t)**2*x1 + 2*(1-t)*t*x3 + t**2*x2
	yp = (1-t)**2*y1 + 2*(1-t)*t*y3 + t**2*y2


	return xp ,yp

def point_in_circle(radius, x_center, y_center):
    output = [0, 0]
    x_min = x_center - radius
    x_max = x_center + radius
    y_min = y_center - radius
    y_max = y_center + radius

    while True:
        output[0], output[1] = random.uniform(x_min,x_max), random.uniform(y_min, y_max)
        if math.sqrt(pow(output[0]-x_center,2) + pow(output[1]-y_center,2)) <= radius:
            return output

def compute_color (color_r, color_g, color_b,color_variation):
# we prepare a new color derived from previous color
	r = random.randint(color_r - color_variation, color_r + color_variation)
	if r < 0:
		r = 0
	elif r > 255:
		r = 255
	color_r = r

	g = random.randint(color_g - color_variation, color_g + color_variation)
	if g < 0:
		g = 0
	elif g > 255:
		g = 255
	color_g = g

	b = random.randint(color_b - color_variation, color_b + color_variation)
	if b < 0:
		b = 0
	elif b > 255:
		b = 255
	color_b = b

	return r,g,b

def draw_branch (p0, p1,length, radius_s, radius_e, branch_curvature, color, screen):
	x0 = p0[0]
	y0 = p0[1]
	x1 = p1[0]
	y1 = p1[1]

	# compute mid point
	xm = (x0 + x1) // 2
	ym = (y0 + y1) // 2

	# compute deviation at midpoint
	xm, ym = point_in_circle(length* branch_curvature, xm, ym)
	pm = (xm, ym)

	# check the distance and adjust step
	distance = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
	step = distance // radius_e + 1
	delta_t = 1 / step

	# drawing Branch using Circles

	t = 0
	contour = 0
	# we compute the change of radius
	delta_r = (radius_s - radius_e)
	if radius_s > 2:
		contour = 1
		while t <= 1:
			xp, yp = compute_bezier_pt_on_crv(p0, p1, pm, t)
			radius = radius_s - delta_r * t
			pygame.draw.circle(screen, BLACK, (xp, yp), radius, contour)
			t = t + delta_t

	t = 0
	while t <= 1:
		xp, yp = compute_bezier_pt_on_crv(p0, p1, pm, t)
		radius = radius_s - delta_r * t - contour
		pygame.draw.circle(screen, color, (xp, yp), radius)
		t = t + delta_t











