from random import randint  

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length * self.length
    
shape = Shape()
print(shape.area())
          
square = Square(randint(1,50))
print(square.area())

    