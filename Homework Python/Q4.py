year = int(input('Enter a year: '))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('It is Leap year')
        else:
            print('It is not a Leap Year')
    else:
        print('It is Leap Year')
else:
    print('It is not Leap Year')