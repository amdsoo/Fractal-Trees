
1/Go to Declaration and edit (for instance)
    # Track current Level Displayed
    level_max_display = 5


2/Go to the classes(), you can edit all the parameter of the trees
Here are the settings you want to edit / 
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

		# self.data explanations
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

you can have up to 10 level (0 to 9),if you want to test 5 levels, put a branch_lenght at 0, this will stop the simulation, or remove the level from the table self.data. 
  1/the length is in pixels  
  2/angle are in degrees 
  3/deviation is a number between 0 and 1, so it is a percentage of randomness. 

3/RUN the main() to observe the results