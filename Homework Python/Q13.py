d1 = {"A":1,"B":2,"C":3}
d2 = {"D":5,"E":8,"F":6 , "A":4}
d3 = {}
for key,value in d2.items():
    if key in d1:
        d1[key] = value + d1.get(key)
    else:
        d1[key] = value 
print(d1)

    
    
