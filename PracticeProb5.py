'''
Author: Mounika Seeram
Date: 26/12/2020
Purpose: Practice Problem5 from CodeWithHarry
'''


def FindNextPalindromSimpleFun(num):
    if num < 10:
        return num
    else:
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
    print(f"Input List {TestCasesList}")

    for i in range(size):
        TestCasesList[i] = FindNextPalindromSimpleFun(TestCasesList[i])
        #print(f'Next palindrome for {TestCasesList[i]} is {result}')
    print(f"Next Palindrome list {TestCasesList}")
