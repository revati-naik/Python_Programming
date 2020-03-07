

class TicTacToe:

	def __init__(self):
		self.input_grid = [None, "-", "-", "-",
							"-", "-", "-",
							"-", "-", "-"]


	def displayGrid(self):
		print(" | %s  | %s | %s |" %(self.input_grid[1], self.input_grid[2], self.input_grid[3]))
		print("---------------")
		print(" | %s  | %s | %s |" %(self.input_grid[4], self.input_grid[5], self.input_grid[6]))
		print("---------------")
		print(" | %s  | %s | %s |" %(self.input_grid[7], self.input_grid[8], self.input_grid[9]))
		print("---------------\n")

		
	def updateGrid(self,  grid_no, user):
		if self.input_grid[grid_no] == "-":
			self.input_grid[grid_no] = user
			return True

		else:
			print("Invalid Move...Choose another position")
			return False


	def countEmptyPositions(self):
		return (self.input_grid.count("-"))


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

	def refreshGrid(self):
		self.input_grid = [None, "-", "-", "-",
							"-", "-", "-",
							"-", "-", "-"]