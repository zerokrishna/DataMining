class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def description(self):
        print(f'Make : {self.make}\nModel : {self.model}\nYear : {self.year}')


car = Car('Tata','Nexa',2014)
car.description()

car2 = Car('Toyota','hiace',2020)
car2.description()