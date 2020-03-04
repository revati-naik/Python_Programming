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
		if self.input_grid[grid_no] == "-":
			self.input_grid[grid_no] = user

		else:
			print("You lost your chance!")

	def is_winner(self, user):
		if self.input_grid[1] == user and self.input_grid[2] == user and self.input_grid[3] == user:
			return True

		if self.input_grid[4] == user and self.input_grid[5] == user and self.input_grid[6] == user:
			return True
	
		if self.input_grid[7] == user and self.input_grid[8] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[1] == user and self.input_grid[4] == user and self.input_grid[6] == user:
			return True

		if self.input_grid[2] == user and self.input_grid[5] == user and self.input_grid[7] == user:
			return True

		if self.input_grid[3] == user and self.input_grid[6] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[1] == user and self.input_grid[5] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[3] == user and self.input_grid[5] == user and self.input_grid[7] == user:
			return True


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

	# Check if X is a winner
	if tic_tac_toe.is_winner("X"):
		print("X is the winner")
		break

	# Get user input 1: Y
	user_input_y = int(input("\nO: Choose 1-9: "))
	tic_tac_toe.update_grid(user_input_y, "O")

	# Check if Y is a winner
	if tic_tac_toe.is_winner("Y"):
		print("Y is the winner")
		break
	
	tic_tac_toe.display_grid()
	print("-----------------------------------")