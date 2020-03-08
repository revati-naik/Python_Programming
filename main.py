import TicTacToe

##
## Header function for the game to dispaly the initial empty grid
##
## :type       tic_tac_toe:  class instance
## :param      tic_tac_toe:  class instance passed to use the class method in the function
##
def startGame(tic_tac_toe):
	print("\nWelcome to TIC-TAC-TOE\n")
	# tic_tac_toe.displayGrid()

##
## Main function written to run the game which takes either user inputs or default inputs or unittest
## inputs depending on where the function is called
##
## :type       test_case:  list
## :param      test_case:  The test cases which is a list of multiple sublists for default test and
##                         unittest. It is None for user inputs
##
## :returns:   Returns the result of the game. "True" for a win of the player (X or Y). Else "False".
##             Or "draw" in case
## :rtype:     string
##
def run_code(tic_tac_toe, test_case):
	result = None 
	i = 0

	# Loops until there are empty spaces available on the grid for more inputs
	while tic_tac_toe.countEmptyPositions() > 0:
		tic_tac_toe.displayGrid()

		# Get user input 1: "X"
		success = False
		while not success:
			try:
				# We use user inputs to test the game.
				if test_case is None:
					user_input_x = int(input("\nX: Choose 1-9: "))
				
				# We use the default test cases as user inputs
				else:
					user_input_x = test_case[i]
			except Exception as e:
				# The inputis not a number
				print("Invalid input. Please try again.")
				continue
			# Checks if the user input or the default input lies between 0-9
			if user_input_x > 0 and user_input_x < 10:
				# Updates the input on the grid
				success = tic_tac_toe.updateGrid(user_input_x, "X")
				
				# checks if the grid could add the new user input 
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

		# Draw condition when all the spaces have been filled out on the grid
		if tic_tac_toe.countEmptyPositions() == 0:
			result = "draw"
			print("DRAWWWW!!!")
			break
		i += 1

		# Get user input 2: "O"
		success = False
		while not success:
			try:
				# We use user inputs to test the game.
				if test_case is None:
					user_input_y = int(input("\nO: Choose 1-9: "))
				
				# We use the default test cases as user inputs
				else:
					user_input_y = test_case[i]
			except Exception as e:
				# The inputis not a number
				print("Invalid input. Please try again.")
				continue

			# Checks if the user input or the default input lies between 0-9
			if user_input_y > 0 and user_input_y < 10:
				# Updates the input on the grid
				success = tic_tac_toe.updateGrid(user_input_y, "O")

				# checks if the grid could add the new user input 
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


def main():
	tic_tac_toe = TicTacToe.TicTacToe()
	startGame(tic_tac_toe)
	run_code(tic_tac_toe, None)	
	

if __name__ == '__main__':
	main()









