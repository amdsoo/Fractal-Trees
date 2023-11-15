
1/Go to declaration.py and edit (for instance)
    # Track current Level Displayed
    level_max_display = 5


2/Go to the classes.py, you can edit all the parameter of the trees
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
		# branch_length (1)in pixels
		# branch_radius start (2) in pixels
		# branch_radius end(3) in pixels
		# cone_angle (4) in degrees
		# cone_angle_reference (5) //Relative to parent branch, or absolute angle.
		# axis_deviation (6) // a % to diversify the angle of deviation
		# branch_max (7) , number of branches at this level
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



3/RUN the main.py to observe the results