import random

you_won = 0
comp_won = 0
round = 0
print("You have total 10 rounds to win this game, Alright Let the fun begin!!")
while(round<10):
        print("Rounds left"+str(10-round))
        your_ch = int(input("Enter your choice\n Snake ==> 0 \n Water ==>1 \n Gun ==>2 \n"))
        comp_ch = random.randint(0, 2)
        if your_ch == 0 and comp_ch == 1 :
            you_won +=1
        elif your_ch == 0 and comp_ch == 2 :
            comp_won +=1
        elif your_ch == 1 and comp_ch == 0 :
            comp_won +=1
        elif your_ch == 1 and comp_ch == 2 :
            you_won +=1
        elif your_ch == 2 and comp_ch == 0 :
            you_won +=1
        elif your_ch == 2 and comp_ch == 1 :
            comp_won +=1
        else :
            pass
        round +=1
if(you_won > comp_won):
        print('Congratulations!! you won the game against computer \n your score is'+str(you_won)+'\n computer score is '+str(comp_won))
elif(you_won < comp_won):
        print('Opps!! You lost \n your score is'+str(you_won)+'\n computer score is '+str(comp_won))
else:
        print('you and computer scored same score, SO Draw :-) \n your score is'+str(you_won)+'\n computer score is '+str(comp_won))

