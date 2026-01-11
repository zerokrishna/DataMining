
def key_checker(d1):
    list = []
    for key,value in d1.items():
        if value > 10:
            list.append(key)
    return list


d1 = {"A":1,"B":12,"C":16,"D":8,"E":15}
print(key_checker(d1))
        