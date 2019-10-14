#guessing the number of items to win the game

import random

random_number=random.randint(1,25)
print(random_number)

for guess_number in range (1,4):
    print('Please guess the number of items: ')
    guess_number = int(input())
    
    if guess_number==random_number:
        print('You guessed the right number of items!')
        break

if guess_number==random_number:
    print('Thank You')
else:
    print('Hard Luck')
    
       


    


