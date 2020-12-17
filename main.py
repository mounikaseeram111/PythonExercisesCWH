import requests
#import time
#from functools import lru_cache
# This is main file empty for now

# while(True):
#        i = int(input("Enter Number"))
#        print(i)
#        if i > 100:
#               print("Num is greater than 100")
#               break;
#        else :
#               print("Try Again!!")
#
# n = int(input("Enter size of your input"))
# ipList = []
# for i in range(n):
#        ipList.append(int(input()))
# print("Kindly enter your choice\n 1.List Comprehension \n 2.Dictnory Comprehension \n 3.Set Comprehension")
# choice = int(input())
#
# if choice == 1 :
#        opList = [i for i in ipList]
#        print(opList)
# elif choice == 2 :
#        #opDict = {f'item {i}':i for i in ipList}
#        #print(opDict)
#        L3 = {f"{index} item": value for index, value in enumerate(ipList)}
#        print(L3)
# elif choice == 3 :
#        opSet = {i for i in ipList}
# #        print(opSet)
# @lru_cache(maxsize=3)
# def somework(n):
#        time.sleep(n)
#        return n
# if __name__ == '__main__':
#     print("Now running some work")
#     somework(3)
#     print('after calling some work')
#     somework(3)
#     print('called again')

r = requests.get("https://newsapi.org/docs/client-libraries/python")
print(r.text)