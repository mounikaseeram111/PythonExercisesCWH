'''
Author: Mounika Seeram
Date: 01/01/2021
Purpose: Practice Problem6 from CodeWithHarry Guess the Number Game
'''

import random
def GuessNum(n):
    Num = n
    count = 0
    #No_of_Guess = 9
    while(True):
        Guss_Num = int(input("Enter your Guess\n"))
        count +=1
        if Guss_Num > Num:
            print("Reduce your input, Try ur Luck!!\n")

        elif Guss_Num < Num:
            print("Increase your input, Try ur Luck!!\n")

        elif Guss_Num == Num:
            print(f"Congratulations!!, your guess is right :-) you took {count} trails to guess the number")
            break
        
    return count

if __name__ == "__main__":
    a = int(input('Enter first Num for range\n'))
    b = int(input('Enter second Num for range\n'))
    n1 = random.randint(a,b)
    print('Player1:')
    print(f'Please guess the number between {a} and {b}')
    player1_score = GuessNum(n1)
    print('Player2:')
    print(f'Please guess the number between {a} and {b}')
    n2 = random.randint(a,b)
    player2_score = GuessNum(n2)
    if player1_score > player2_score:
        print('Player2 won the Game')
    elif player1_score < player2_score:
        print('Player1 won the Game')
    else:
        print('Player1 and Player2 both wins and took the same no of guesses')
    print(f'Player1 actual number is {n1} and player2 actual number is {n2}')