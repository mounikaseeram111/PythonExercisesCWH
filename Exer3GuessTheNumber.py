Num = 19

No_of_Guess = 9
for i in range(0,9):
    Guss_Num = int(input("Enter your Guess"))
    if Guss_Num > Num:
        print("Reduce your input, Try ur Luck!!")

    elif Guss_Num < Num:
        print("Increase your input, Try ur Luck!!")

    elif Guss_Num == Num:
        print("Congratulations!!, your guess is right :-)")
        print("No of guesses you took to won",i+1)
        break
else:print("Your guess limit is over,Sorry!!")
