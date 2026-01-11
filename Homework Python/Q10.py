
def is_prime(num):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag +=1
    
    if flag == 0:
        return True
    else:
        return False


num = int(input('Enter a number :'))
if num > 0:
    if is_prime(num):
        print('Number is prime')
    else:
        print('Number is composite')