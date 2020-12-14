def getdate():
    import datetime
    return datetime.datetime.now()

def DisplayData(name,type):
    if type == 'Food' :
        f = open(name+'FoodTracker.txt')
        print(f.readlines())
    elif type == 'Exercise':
        f = open(name+'ExerciseTracker.txt')
        print(f.readlines())
    f.close()

def LogData(name,type):
    if type == 'Food' :
        f = open(name+'FoodTracker.txt','a')
        items = input('Enter the food you have eaten')
        f.write('['+str(getdate())+'] \t'+items+'\n')
    elif type == 'Exercise':
        f = open(name+'ExerciseTracker.txt','a')
        items = input('Enter the exercises you have completed')
        f.write('[' + str(getdate()) + '] \t' +items+'\n')
    f.close()

choice = int(input("Please specify your choice \n 0 => Logging new Data \n 1 => Displaying logged old data"))
name = input("Please specify name of client : Trump / Modi / Putin")
type = input("Kindly let us know the type of data Food / Exercise ")
try:
    if(choice == 0):
        LogData(name,type)
    elif(choice == 1):
        DisplayData(name,type)
except:
    print("Invalid Input")







