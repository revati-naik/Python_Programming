import unittest 
import sattu_the_great


class TestAssertEqual(unittest.TestCase):
	def test_func_1(self):
		test_case = [[1,2,4,6,7], [2,1,5,6,8], [3,1,6,2,9], [1,4,2,5,3], [4,1,5,2,6], [7,1,8,2,9], 
					[1,2,5,7,9], [3,2,5,9,7], [2,1,6,4,8,7], [1,2,6,5,7,8], [2,3,5,6,7,9], [2,1,3,5,7,9],
		 			[2,3,9,5,8,7], [1,4,2,5,9,6], [1,7,2,8,5,9], [2,1,6,5,7,9],[2,3,9,5,4,7]]


		result = sattu_the_great.run_code(test_case)
		print("Result", result)
		self.assertEqual(result, True)

	def test_func_2(self):
		test_case = [[1,2,2,3,5,4,6,8,7,9], [1,2,4,6,7]]
		result = sattu_the_great.run_code(test_case)
		print("Result", result)
		self.assertEqual(result, "draw")

if __name__ == '__main__':
	unittest.main()