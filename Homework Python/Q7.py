n = int(input('Enter a number: '))

a = 1
b = 0
c = 0
count = 0
while count < n:
    count+=1
    print(a)
    c = a + b
    b = a
    a = c