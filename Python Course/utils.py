
def find_max(numbers):
    max = 0 # declare max 
    for num in numbers:
        if max < num:
            max = num 
    return max
