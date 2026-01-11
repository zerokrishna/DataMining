
def string_frequency(string):
    words = string.split()
    d1 = {}
    for word in words:
        count = 0
        for ch in word:
            count+=1
        d1.update({word:count})
    return d1


string = input('Enter a string: ')
print(string_frequency(string))       