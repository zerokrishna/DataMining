def is_prime(num):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag +=1
    
    if flag == 0:
        return True
    else:
        return False


def find_factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact
        