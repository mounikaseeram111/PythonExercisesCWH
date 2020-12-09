def Pattern(choice,n):
    if choice == True :
        #do this
        for i in range(0,n+1):
            for j in range(0,i):
                print('*',end=" ")
            print("\n")

    else :
        #do this
        #print("In else")
        for i in range(n,0,-1):
            for j in range(0, i,):
                #print('in inner loop')
                print('*',end=" ")
            print("\n")

n = int(input("Enter N"))
choice = bool(int(input("Enter your choice [0,1] to print pattern")))
#print(choice)
Pattern(choice,n)
