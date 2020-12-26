'''
Author: Mounika Seeram
Date: 26/12/2020
Purpose: Practice Problem4 from CodeWithHarry
'''


def FindNxtPalindrome(num):
    while(True):
        num = num + 1
        temp = num
        rev = 0
        # palindrome check code

        while temp > 0:

            dig = temp % 10
            rev = rev*10 + dig
            temp = temp // 10
        if num == rev:
            break

    return num


def FindNextPalindromSimpleFun(num):
    num += 1
    while not is_palindrome(num):
        num = num + 1
    return num


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    size = int(input("Enter no of test cases u want to test"))
    TestCasesList = []
    for i in range(size):
        TestCasesList.append(int(input()))
    for i in range(size):
        result = FindNextPalindromSimpleFun(TestCasesList[i])
        print(f'Next palindrome for {TestCasesList[i]} is {result}')
