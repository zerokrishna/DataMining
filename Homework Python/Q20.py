class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length*self.width
        return area
    def perimeter(self):
        perimeter = 2*(self.length+self.width)
        return perimeter
        

rect = Rectangle(5,12)
rect.length = 6
rect.width = 8
print(rect.area())
print(rect.perimeter())