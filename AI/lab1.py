height = input('What is your height in cm ? ')
weight = input('What is your weight in Kg ? ')
bmi = float(weight)/(float(height)/100)**2
print(f'Your BMI is {round(bmi,2)}')
