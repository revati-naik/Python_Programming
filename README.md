# Tic-Tac-Toe

Developing the famous Tic-Tac-Toe game.

## Introduction

This is the code repository for th tic-tac-toe game. It allows you to play this game with another human or with the computer (AI algorithm). It is tested for the win and the draw conditions and uses an interractive terminal and let's the user insert his/her choices of placing the "X's" and the "0's" on the board. 


## Two Player Game

  * **Human VS Human**

    Here, you play the game in the most traditional way, where after every player's move, the board is examined for any win conditions. When the gird's have been exhausted, the game is declared as Draw!


  * **Human VS Computer**
  
    Here, you play with the AI engine that runs in the backend. For this particular implementation, I have used the game tree approach. Here, different states of the game are mapped to the node of the tree. When the computer is given a chance, it will calculate the rollout all the possibilities of the given current board state/configuration until it reaches a win condiiton. The root node would be the current board configuration and the algorithm keeps building the child nodes in levels. The first level from the root node would be all the possible moves the computer/AI can take from the given state. The second level would be the moves the human would probably take for every node in the first level. This is continued untill the game is over i.e. the algorithm reaches it's leaf nodes. This condition could leave the player in three states i.e. win, loose or draw/tie.  


## Minimax Algorithm

Minimax is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as "maximin"—to maximize the minimum gain. Originally formulated for n-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty. 

The minimax algorithm is run recurrsively to find the optimal policy. In this case, the next move the computer should take to increase the chances of wining the game. If the human is in a win position, it would block that position. If the computer is in a win position it will take that move and win the games. In other situation it will take a move which is most optimal using the minimax algorithm. 

## Dependencies

  * Environment: Linux

  *  python > 3.0 [Download here](https://www.python.org/downloads/)
  * unittest 

    `pip3 install uniittest`

  * numpy

    `pip3 install numpy`
    

## Code Files
   

  * main.py: 
    
    Contains the main script for running the game 
  
  * TicTacToe.py: 
  
    Class file for the game
  
   
  * unit_test.py: 
  
    Class file for the unit tests
    
    
 

## Running the code

 1. Clone the repo on yout local system using the command
 
    `git clone https://gitlab.com/revati-naik/tic-tac-toe.git`

2. Run the code:

    `cd <path_to_repository>`

    `python3 main.py`

3. The software will ask you to choose certain play conditions using the interractive terminal

    `Choose the game size: ` This allows you to choose your grid size for the game (3X3, 5X5, etc.). This version can handle all types of grid sizes > 2. The implementation uses minimax algorithm (when you play vs computer) and this takes a while to run when the `game_size `is > 3. This works efficiently for `game_size `of 3. 

    `Do you want to play vs the computer?(y/n):` This allows you to choose if you want to play with another human or vs the computer. 

    `Choose X or O: ` This allows you to choose if you want to have the symbol X or 0. 

    `Do you want to start first?[y/n]:` This allows you to choose if you want to go first. 

A sample interractive terminal is as shown below:


## Unit Testing

`test_func_1()` : This unit test function tests for win condition accross row, column, diagonal and lose

`test_func_2` : This unit test function tests for the minimax algorithm to choose the correct next move in order to stop the other player from winning. 

## Run Unit Testing Code 
   
`cd <path_to_repository>`

`python3 unit_test.py`

   


## References

[Wikipedia: Minimax](https://en.wikipedia.org/wiki/Minimax)





    
    
    

