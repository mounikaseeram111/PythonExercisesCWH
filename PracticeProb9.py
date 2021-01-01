'''
Author: Mounika Seeram
Date: 01/01/2021
Purpose: Practice Problem7 from CodeWithHarry, Funny Names
'''
import random

n = int(input('Enter the no of friends\n'))
print(f'Enter the names of {n} friends\n')
namesList = [input() for i in range(n)]
print(namesList)
frstNames = []
lstNames = []
for name in namesList :
    temp = name.split(" ")
    if len(temp) > 2 :
        frstNames.append(temp[0])
        lstNames.append(temp[1]+" "+temp[2])
    else:
        frstNames.append(temp[0])
        lstNames.append(temp[1])
#print(frstLstNames)

funnyNames = []
for i in range(len(namesList)):
    funnyName = frstNames[i] + " " + random.choice(lstNames)
    funnyNames.append(funnyName)

print(funnyNames)