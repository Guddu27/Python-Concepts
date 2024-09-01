
#! Define a circle class to create a circle with radius 'r' using the constructor . Define Area() method of the class which calculates the area of the circle. Define Perimeter() method of the class which alows the user to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(34)
print(f"Area of the circle : {c1.Area()}")
print(f"Perimeter of the circle : {c1.Perimeter()}")