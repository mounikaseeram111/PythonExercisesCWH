def whenUreach100(ip,current_year):
    num = int(ip)
    #dob = {'age':0,'birth_year':0}
    age = 0
    birth_year = 0
    if num < 100:
        age = num
        birth_year = current_year - age
        print('you will be 100 years old in ' + str(birth_year + 100))
    elif (num > 100 and num <= 1920):
        print("Invalid Input,You seem to be oldest person Alive")
    elif (num > 1920 and num <= 2020) :
        birth_year = num
        age = current_year- birth_year
        print('you will be 100 years old in ' + str(birth_year + 100))
    else:
        print('You are not yet born,Age or birth year cannot be in future')

    return age , birth_year

def KnowUrAge(ch_year,birth_year):
    ageAtch_year = ch_year - birth_year
    if(ageAtch_year < 0):
        print(f'you are not yet born in {ch_year}')
    else:
        print(f'you are {ageAtch_year} years old in {ch_year}')

if __name__ == '__main__':
    CURRENT_YEAR = 2020
    ip = input('Enter Age or your birth year')
    AGE,birth_year = whenUreach100(ip,CURRENT_YEAR)
    print(f'your age is {AGE} and your birth year is {birth_year}')
    print('Do want to continue, Kindly press y for Yes and n for No')
    choice = input()
    if choice == 'y' or choice == 'Y':
        ch_year = int(input('Kindly enter in which year you want to know your age'))
        KnowUrAge(ch_year,birth_year)
    else:
        exit()













