import unittest 
import main


class TestAssertEqual(unittest.TestCase):

	def test_func_1(self):
		# Test cases to check all combinations of win for "X" amnd "O" across row, column and diagonal
		test_case = [[1,2,4,6,7], [2,1,5,6,8], [3,1,6,2,9], [1,4,2,5,3], [4,1,5,2,6], [7,1,8,2,9], 
					[1,2,5,7,9], [3,2,5,9,7], [2,1,6,4,8,7], [1,2,6,5,7,8], [2,3,5,6,7,9], [2,1,3,5,7,9],
		 			[2,3,9,5,8,7], [1,4,2,5,9,6], [1,7,2,8,5,9], [2,1,6,5,7,9],[2,3,9,5,4,7]]

		for test_case_i in test_case:
			tic_tac_toe.refreshGrid()
			i = 0
			result = main.run_code(test_case_i)
			print("Result", result)

			# Check if the reuslt value is "True"
			self.assertEqual(result, True)

	def test_func_2(self):
		# Test case includes draw condition (where no player wins) and a case which gives an error 
		# for not being a draw. 
		test_case = [[1,2,2,3,5,4,6,8,7,9], [1,2,4,6,7]]
		result = main.run_code(test_case)
		print("Result", result)

		# Check if the value id=s "draw"
		self.assertEqual(result, "draw")

if __name__ == '__main__':
	unittest.main()