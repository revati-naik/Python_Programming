## TIC-TAC-TOE Game

This game is designed using python3 as the coding platform.

## **Problem Statment:**

The game is a tic-tac-toe grid board of __3x3__. 

Take user inputs ("X" and "O") to be placed on the grid board and declares a winner if any of the win conditions occur. Check below for the win conditions. 


## **Approach:**


The game is played by two players with user inputs as __"x" and "O"__. 

The game allows alternate player to place their initials ("X" amd "O") on the board. 

After every move, the code checks if any of the player has reached the win condition. 

The code also checks for a __draw__ condition where no player wins and all the grids on the board have been exhausted or used. 


__EXCEPTIONS__

Meanwhile, the code is capable to even detect "Invalid Numbers" i.e. the grid number (box in which the input character needs to be placed) which does not lie between 1-9. In such condition, the code waits for another grid number which lies in the valid range. 

The code even throws an error if the input is a grid number which is already occupied by a character ("X" or "O") and waites for another input grid number. 


## **Code Files:**

1. main.py:

    The main.py file can be used to play the game with user inputs.
    

2. TicTacToe.py: 

    This is a class file which defines the class TicTacToe which consists of various class methods used to play the game.
    
3. defaulttest.py: 

    This file consists of few default cases to test the functionality of the code. It checks for the win conditions for both "X" and "O" along 3 rows, 3 columns and both the diagonals. It also checks for the "draw" condition. 
    
4. unittest.py:

    A unittest class has been created to check for few conditions using the in-built python module unittest.  


## **Dependencies:**

1. __numpy__:  Install numpy pacakge from python3 using the following command on the terminal `pip install numpy`

2. __cv2__:  Install cv2 pacakge from python3 using the following command on the terminal `pip install cv2`

3. __sys__:  Install sys pacakge from python3 using the following command on the terminal `pip install sys`


## **Running the Code:**

1. For letting two players play the game, run the following command on your terminal `python3 main.py`

    It will ask for user input from alternate players. 

    `X: Choose 1-9: `

    `Y: Choose 1-9: `

2. For running the default test cases, run the following command on your terminal `python3 defaulttest.py`

3. For runnign the unittest, run the following command on your terminal `python3 unittest.py`

## **HAPPY PLAYING!!!!**
