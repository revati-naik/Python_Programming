import sys
import numpy as np 
import cv2 
import TicTacToe


def startGame(tic_tac_toe):
	print("\nTIC-TAC-TOE\n")
	tic_tac_toe.displayGrid()

def run_code(test_case):
	result = None 
	i = 0
	while tic_tac_toe.countEmptyPositions() > 0:
		tic_tac_toe.displayGrid()
		
		# Get user input 1: X
		success = False
		while not success:
			try:
				if test_case is None:
					user_input_x = int(input("\nX: Choose 1-9: "))
				else:
					user_input_x = test_case[i]
			except Exception as e:
				print("Invalid input. Please try again.")
				continue
			if user_input_x > 0 and user_input_x < 10:
				success = tic_tac_toe.updateGrid(user_input_x, "X")
				if not success:
					i += 1
					continue
				tic_tac_toe.displayGrid()

			else:
				print("Invalid number!")
				i += 1
				continue

		# Check if X is a winner
		result = tic_tac_toe.isWinner("X")
		if result:
			print("X is the winner")
			break

		if tic_tac_toe.countEmptyPositions() == 0:
			result = "draw"
			print("DRAWWWW!!!")
			break
		i += 1

		# Get user input 1: Y
		success = False
		while not success:
			try:
				if test_case is None:
					user_input_y = int(input("\nO: Choose 1-9: "))
				else:
					user_input_y = test_case[i]
			except Exception as e:
				print("Invalid input. Please try again.")
				continue
			if user_input_y > 0 and user_input_y < 10:
				success = tic_tac_toe.updateGrid(user_input_y, "O")
				if not success:
					i += 1
					continue
				tic_tac_toe.displayGrid()

			else:
				print("Invalid number!")
				i += 1
				continue

		# Check if Y is a winner
		result = tic_tac_toe.isWinner("O")
		if result:
			print("Y is the winner")
			break
		
		i += 1
		print("-----------------------------------\n")
		print("Next Move\n")
	return result

tic_tac_toe = TicTacToe.TicTacToe()

def main():
	run_code(None)	
	

if __name__ == '__main__':
	main()









