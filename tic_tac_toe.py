import sys
import numpy as np 


class tic_tac_toe:

	def __init__(self):
		self.input_grid = ["-", "-", "-", "-",
							"-", "-", "-",
							"-", "-", "-"]

	def display_grid(self):
		print(" | %s  | %s | %s |" %(self.input_grid[1], self.input_grid[2], self.input_grid[3]))
		print(" | %s  | %s | %s |" %(self.input_grid[4], self.input_grid[5], self.input_grid[6]))
		print(" | %s  | %s | %s |" %(self.input_grid[7], self.input_grid[8], self.input_grid[9]))
		
	def update_grid(self,  grid_no, user):
		self.input_grid[grid_no] = user




tic_tac_toe = tic_tac_toe()


def start_game():

	print("\nTIC-TAC-TOE\n")
	tic_tac_toe.display_grid()



while True:
	start_game()

	# Get user input 1: X
	user_input_x = int(input("\nX: Choose 1-9: "))
	tic_tac_toe.update_grid(user_input_x, "X")

	tic_tac_toe.display_grid()

	# Get user input 1: Y
	user_input_y = int(input("\nY: Choose 1-9: "))
	tic_tac_toe.update_grid(user_input_y, "Y")
	
	tic_tac_toe.display_grid()
	print("-----------------------------------")