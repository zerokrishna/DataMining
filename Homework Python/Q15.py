
def hvk(d1):
    max = 0
    str = ''
    for key,value in d1.items():
        if value > max:
            max = value
            str = key
    return str


d1 = {"A":1,"B":12,"C":16,"D":8,"E":15}
print(hvk(d1))
        