import main

# Test cases to check all combinations of win for "X" amnd "O" across row, column and diagonal
# Test case also includes draw condition (where no player wins) and  input grid number which 
# is already occupied by a character and also when the input is not in between 1-9
test_case = [[1,2,4,6,7], [2,1,5,6,8], [3,1,6,2,9], [1,4,2,5,3], [4,1,5,2,6], [7,1,8,2,9], 
			[1,2,5,7,9], [3,2,5,9,7], [2,1,6,4,8,7], [1,2,6,5,7,8], [2,3,5,6,7,9], [2,1,3,5,7,9], 
			[2,3,9,5,8,7], [1,4,2,5,9,6], [1,7,2,8,5,9], [2,1,6,5,7,9],[2,3,9,5,4,7], 
			[1,2,3,5,4,6,8,7,9], [1,2,3,2,5,4,6,8,7,9], [1,2,2,3,5,4,6,8,7,9], [1,12,2,3,5,4,6,8,7,9],
			[1,12,2,3,5,5,4,6,8,7,9]]

f = open("default_test_output.txt", "w+")

for test_case_i in test_case:
	main.tic_tac_toe.refreshGrid()
	result = main.run_code(test_case_i)

	test_case_str = " ".join(map(str, test_case_i))
	f.write(test_case_str + "\n")
	f.write(str(result) + "\n")
	f.write("--------------\n")

f.close()