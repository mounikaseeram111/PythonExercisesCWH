def DivideTheApples(n,mn,mx):
    if mn == mx :
        print(f'This is not range {mn} and {mx} are equal')
        if n % mx == 0:
            print(f'{n} is divisible by {mn}')
    else:
        for i in range(mn,mx+1):
            if n % i == 0:
                print(f'{i} is divisible by {n}')
            else:
                print(f'{i} is not divisible by {n}')

if __name__ == '__main__':
    try:
        n = int(input('Enter number of Apples Harry got ?'))
        mn = int(input('Enter the minimum of range Harry can get'))
        mx = int(input('Enter the maximum of range Harry can get'))
        DivideTheApples(n,mn,mx)
    except:
        print('Invalid input')


