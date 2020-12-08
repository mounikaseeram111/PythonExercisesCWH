a = input("Enter first num")
b = input("Enter Second num")
Op = input("Enter Operator of your choice")

new_ip = a+Op+b
if new_ip == '45*3':
    print('555')
elif new_ip == '56+9':
    print('77')
elif new_ip == '56/6':
    print('4')
elif Op=='+':
    print(int(a)+int(b))
elif Op == '-':
    print(int(a)-int(b))
elif Op == '*':
    print(int(a)*int(b))
elif Op == '/':
    print(int(a)/int(b))
elif Op == '%':
    print(int(a)%int(b))

