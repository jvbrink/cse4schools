import numpy as np
import matplotlib.pyplot as plt
import random, time, sys

colors = {"ocean": "#0066FF", "miss": "#0066FF", "hit": "#FF0000", 'ship': "#0066FF"}

def draw_grid(grid, ax=None, test=False):
	if ax == None: 
		ax = plt.gca()
		ax.axis([-0.5, 9.5, -0.5, 9.5])
		ax.patch.set_facecolor("gray")
		ax.set_aspect('equal', 'box')
		ax.xaxis.set_major_locator(plt.NullLocator())
		ax.yaxis.set_major_locator(plt.NullLocator())
		ax.set_xticks(range(10))f
		ax.set_yticks(range(10))
		ax.set_title("Battleship!", fontsize=26)
		ax.set_xlabel('X-coordinate', fontsize=22)
		ax.set_ylabel('Y-coordinate', fontsize=22)
		ax.autoscale_view()
		mng = plt.get_current_fig_manager()
		#mng.full_screen_toggle()
		plt.ion()
		plt.show()

	for (x, y), value in np.ndenumerate(grid):
		fcolor = colors[value]
		if test and value == 'ship': fcolor="#000000"
		hatch = "xxx" if value == "miss" else ""

		rect = plt.Rectangle([x-0.45, y-0.45], 0.9, 0.9, facecolor=fcolor, edgecolor='black', hatch=hatch)
		ax.add_patch(rect)

	plt.draw()
	return ax

def set_up(X, Y):
	grid = []
	for i in range(X):
		grid.append(['ocean']*Y)

	return grid

def welcome():
	print """*************************************
*************************************
***                               *** 
***     WELCOME TO BATTLESHIP!    *** 
***                               *** 
***     (write exit to close)     *** 
***                               *** 
************************************* 
*************************************
"""

def fire_shot(grid):
	remaining = sum([g.count("ship") for g in grid])
	if remaining == 0:
		print "You did it captain! We sunk all the enemy battleships!"
	print "There are %s %d coordinates you need to hit!" % (['still', 'only'][remaining>3], remaining)
	print "We have %d missiles remaining in storage." % (shots_left)
	print "Captain, where would you like us to fire?"

	while True:
		X = raw_input("X-coordinate: ")
		if X.lower() == "exit": sys.exit()
		Y = raw_input("Y-coordinate: ")
		if Y.lower() == "exit": sys.exit()
		
		try:
			X = int(X)
			Y = int(Y)
		
			try:
				if grid[X][Y] == "miss" or grid[X][Y] == "hit":
					print "We have already fired at that position captain. Please try again"

				if grid[X][Y] == "ocean":
					grid[X][Y] = "miss"
					print "\nFiring on your selected positon now";
					print "Miss! ";
					print "Our misile went straight into the ocean!\n\n"
					return grid

				if grid[X][Y] == "ship":
					grid[X][Y] = "hit"
					print "\nFiring on your selected positon now";
					print "Hit! "; 
					print "Our misile hit the enemy ship!\n\n"
					return grid

			except: 
				print "Those coordinates are outside our map!"

		except:
			print "Only integer coordinates are valid!"




def place_ships(grid, gridsize):
	ships = [5, 4, 3, 3, 2]

	while ships:
		size = ships.pop()
		if random.randint(0, 1):
			x = random.randint(0, gridsize-1)
			y = random.randint(0, gridsize-1 - size)
			while "ship" in grid[x][y:y+size]:
				x = random.randint(0, gridsize-1)
				y = random.randint(0, gridsize-1 - size)
			for i in range(size):
				grid[x][y+i] = "ship"
		else:
			x = random.randint(0, gridsize - 1 - size)
			y = random.randint(0, gridsize - 1)

			while "ship" in np.transpose(grid)[y][x:x+size]:
				x = random.randint(0, gridsize-1 - size)
				y = random.randint(0, gridsize-1)
			for i in range(size):
				grid[x+i][y] = "ship"

	return grid

if __name__ == '__main__':
	gridsize = 10
	grid = set_up(gridsize, gridsize)
	ax = draw_grid(grid)

	grid = place_ships(grid, gridsize)
	welcome()

	ax = draw_grid(grid, ax=ax, test=False)

	shots_left = 50
	while shots_left > 0:
		grid = fire_shot(grid)
		ax = draw_grid(grid,  test=False)
		shots_left -= 1
		