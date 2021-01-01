'''
Author: Mounika Seeram
Date: 01/01/2021
Purpose: Practice Problem7 from CodeWithHarry, Fake Multiplication
'''
import random

def RohanDasMulTable(number):
    table = []
    #hard coded wrong index
    # for i in range(1,11):
    #     if i == 5:
    #         table.append(number+14)
    #     else:
    #         table.append(number*i)

    # Random wrong index
    wrong = random.randint(0,9)
    table = [number*i for i in range(1,11)]
    table[wrong] = number*wrong + random.randint(0,9)

    return table


def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1]!=(number*i):
            print(f'RohanDas\'s table is giving inccorect result at index {i-1}')
            break
    else:
        print('RohanDas table is giving correct results')
        

if __name__ == "__main__":
    num = int(input("Enter Number to get the Table for that number\n"))
    table = RohanDasMulTable(num)
    print(table)
    print('Checking whether RohanDas\'s mutliplication table is correct or not\n')
    isCorrect(table,num)