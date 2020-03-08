k
#
# Class TicTacToe to execute the logic for the game
#
class TicTacToe:

	def __init__(self):
		self.input_grid = [None, "-", "-", "-",
							"-", "-", "-",
							"-", "-", "-"]

	##
	## Function to display the grid with the updated values from the user
	##
	def displayGrid(self):
		print(" | %s  | %s | %s |" %(self.input_grid[1], self.input_grid[2], self.input_grid[3]))
		print("---------------")
		print(" | %s  | %s | %s |" %(self.input_grid[4], self.input_grid[5], self.input_grid[6]))
		print("---------------")
		print(" | %s  | %s | %s |" %(self.input_grid[7], self.input_grid[8], self.input_grid[9]))
		print("---------------\n")

	##
	## Updates the grid with trhe current input. Either "X" or "O"
	##
	## :param      grid_no:  The grid number to be updated with either "X" or "O"
	## :type       grid_no:  int
	## :param      user:     The user name "X" or "O" i.e 
	## :type       user:     string
	##
	## :returns:   True if thye grid gets updated with the input. False otherwise
	## :rtype:     boolean
	##
	def updateGrid(self,  grid_no, user):
		if self.input_grid[grid_no] == "-":
			self.input_grid[grid_no] = user
			return True

		else:
			print("Invalid Move...Choose another position")
			return False

	##
	## Counts the number of empty positions available on the grid.
	##
	## :returns:   Number of empty positions on the grid.
	## :rtype:     int
	##
	def countEmptyPositions(self):
		return (self.input_grid.count("-"))


	##
	## Determines whether the specified user is winner. COnsists of 8 conditions which can cause 
	## a player to win
	##
	## :param      user:  The user name. Either "X" or "O"
	## :type       user:  string
	##
	## :returns:   True if the specified user is winner, False otherwise.
	## :rtype:     boolean
	##
	def isWinner(self, user):
		if self.input_grid[1] == user and self.input_grid[2] == user and self.input_grid[3] == user:
			return True

		if self.input_grid[4] == user and self.input_grid[5] == user and self.input_grid[6] == user:
			return True
	
		if self.input_grid[7] == user and self.input_grid[8] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[1] == user and self.input_grid[4] == user and self.input_grid[7] == user:
			return True

		if self.input_grid[2] == user and self.input_grid[5] == user and self.input_grid[8] == user:
			return True

		if self.input_grid[3] == user and self.input_grid[6] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[1] == user and self.input_grid[5] == user and self.input_grid[9] == user:
			return True

		if self.input_grid[3] == user and self.input_grid[5] == user and self.input_grid[7] == user:
			return True

	
	##
	## Used to refresh the grid after every game. 
	##
	def refreshGrid(self):
		self.input_grid = [None, "-", "-", "-",
							"-", "-", "-",
							"-", "-", "-"]