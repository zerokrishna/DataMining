
height = float(input('Enter height in CM : '))
weight = float(input('Enter weight in kg: '))
bmi = weight / (height/100)**2
print(f'Your BMI is {round(bmi,2)}')