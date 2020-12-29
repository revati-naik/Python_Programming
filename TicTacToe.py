from math import inf 
import numpy as np 
import platform
import sys
from os import system
sys.dont_write_bytecode = True


class TicTacToe:

	def __init__(self, grid_size=3, player_2=None, game_depth=0, board=np.zeros((3, 3))):
		
		self.human = -1
		self.computer = +1

		# self.computer_choice = player_2

		self.grid_size = grid_size

		self.input_grid = board
		# self.input_grid = np.zeros((self.grid_size, self.grid_size))

	##
	## Initial display of the board with the grid numbering
	##
	def initialGridDisplay(self):
		initial_grid = np.arange(start=0, stop=self.grid_size*self.grid_size, step=1)
		initial_grid = np.reshape(initial_grid, (self.grid_size, self.grid_size))

		for i in range(0, initial_grid.shape[0]):
			print(" "),
			for j in range(0, initial_grid.shape[1]):
				print(' |   ',initial_grid[i][j], sep=' ', end=' ',flush=True)
			print("\n"),

	##
	## Prints the cuurent state of the board
	##
	## :param      computer_choice:  The computer choice ("X" or "0")
	## :type       computer_choice:  { char }
	## :param      human_choice:     The human choice ("X" or "0")
	## :type       human_choice:     { char }
	##
	def printGrid(self, computer_choice, human_choice):
		
		chars = {
		-1: human_choice,
		+1: computer_choice,
		0: ' '}
		
		str_line = '---------------'

		print('\n' + str_line)
		for row in self.input_grid:
			for cell in row:
				symbol = chars[cell]
				print(f'| {symbol} |', end='')
			print('\n' + str_line)



	##
	## Checks if the cell choosen by the user is empty or not
	##
	## :param      i:    Row number
	## :type       i:    { int }
	## :param      j:    Column number
	## :type       j:    { int }
	##
	## :returns:   True if valid move, False otherwise.
	## :rtype:     boolean
	##
	def isValidMove(self, i,j):

		if self.input_grid[i][j] == 0:
			return True
		else:
			return False


	##
	## Updates the grid with the current input. Either "X" or "O"
	##
	## :param      grid_no:  The grid number to be updated with either "X" or "O"
	## :type       grid_no:  int
	## :param      user:     The user name "X" or "O" i.e 
	## :type       user:     string
	##
	## :returns:   True if thye grid gets updated with the input. False otherwise
	## :rtype:     boolean
	##
	def updateGrid(self, i, j, user):

		if self.isValidMove(i,j):
			self.input_grid[i][j] = user
			return True
		else:
			print("Already Occupied...Choose another position")
			return False

	##
	## Creates a list of coordinates of empty grid cells
	##
	## :returns:   List of coordinates of empty grid cells on the board
	## :rtype:     { list }
	##
	def emptyGrid(self):
		self.empty_grid = []

		for x, row in enumerate(self.input_grid):
			for y, cell in enumerate(row):
				if cell == 0:
					self.empty_grid.append([x,y])
		return self.empty_grid

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

		# comp = 1
		# human = -1

		# across diagonal
		input_grid_diag_0 = np.diagonal(self.input_grid)
		input_grid_diag_1 = np.fliplr(self.input_grid).diagonal()

		if (np.sum(input_grid_diag_0) == user*self.grid_size):
			return True

		if (np.sum(input_grid_diag_1) == user*self.grid_size):
			return True

		val_rows = np.sum(self.input_grid, axis=1) # for comp
		arr_rows = np.where(val_rows == user*self.grid_size)[0] #for human
		if len(arr_rows) != 0:
			return True

		val_col = np.sum(self.input_grid, axis=0)
		arr_col = np.where(val_col == user*self.grid_size)[0]
		if len(arr_col) != 0:
			return True
		
		return False

	##
	## Calculates hurestic value of the current board state
	##
	## :returns:   score of the board (0 or -1 or +1)
	## :rtype:     { int }
	##
	def evaluateScore(self):
		if self.isWinner(self.computer):
			score = self.computer
		elif self.isWinner(self.human):
			score = self.human
		else:
			score = 0

		return score

	## Checks is any of the player is in a win state
	##
	## :returns:   True if game over, False otherwise.
	## :rtype:     boolean
	##
	def isGameOver(self):
		return self.isWinner(user=self.human) or self.isWinner(user=self.computer)


	##
	## AI function that makes the best move towards a win
	##
	## :param      game_depth:  depthof the node in the game tree
	## :type       game_depth:  { int }
	## :param      player:      The player (+1 or -1)
	## :type       player:      { int }
	##
	## :returns:   { best move [best_row_no, best_col_no, best score] }
	## :rtype:     { list }
	##
	def minimaxAlgorithm(self, game_depth, player):
		if player == self.computer:
			best = [-1, -1, -inf]
		else:
			best = [-1, -1, +inf]

		if game_depth == 0 or self.isGameOver():
			score = self.evaluateScore()
			return [-1, -1, score]


		for cell in self.emptyGrid():
			x, y = cell[0], cell[1]

			self.input_grid[x][y] = player
			score = self.minimaxAlgorithm(game_depth - 1, -player)
			self.input_grid[x][y] = 0
			score[0], score[1] = x, y

			if player == self.computer:
				if score[2] > best[2]:
					best = score

			else:
				if score[2] < best[2]:
					best = score
	
		return best


	##
	## Clears the screen
	##
	def clean(self):
		os_name = platform.system().lower()
		if 'windows' in os_name:
			system('cls')
		else:
			system('clear')


