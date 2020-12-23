n = int(input('enter size of list'))
print('Enter calories list elements')
ipList = []
for i in range(n):
    ipList.append(int(input()))


opList1 = ipList.copy()
opList1.reverse()
print(opList1)


opList2= ipList[::-1]
print(opList2)

opList3 = ipList.copy()
# left = 0
# right = n-1
# while (left < right):
#         temp = opList3[left]
#         opList3[left]= opList3[right]
#         opList3[right]  = temp
#         left +=1
#         right -=1
# print(opList3)

for i in range(n//2):
    opList3[i],opList3[n-i-1] = opList3[n-i-1],opList3[i]
print(opList3)

if opList1 == opList2 == opList3 :
    print('Three methods return same result')

