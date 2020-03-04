import sys
import numpy as np 


class tic_tac_toe:

	def __init__(self):
		self.input_grid = [" - ", " - ", " - ",
							" - ", " - ", " - ",
							" - ", " - ", " - "]

	def display_grid(self):
		print(" | %s  | %s | %s |" %(self.input_grid[0], self.input_grid[1], self.input_grid[2]))
		print(" | %s  | %s | %s |" %(self.input_grid[3], self.input_grid[4], self.input_grid[5]))
		print(" | %s  | %s | %s |" %(self.input_grid[6], self.input_grid[7], self.input_grid[8]))
		

tic_tac_toe = tic_tac_toe()
tic_tac_toe.display_grid()