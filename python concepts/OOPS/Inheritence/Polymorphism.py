
#* Ploymorphism : Ploy == many & Morph == forms (many forms)

# When the same operator is allowed to have different meaning according to the context.

#! Operators and dunder : 

'''
a + b       __add__  
a - b       __sub__
a * b       __mul__
a / b       __truediv__
a % b       __mod__
'''

#! P L O Y M O P H I S M (Operator Overloading)
#-----------------------------------------------
class Complex : 
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_num(self):
        print(f"{self.real}i + {self.img}j")

    #! Dunder Function
    def __add__(self, num2):
        #! Logic to add two nums
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
    def __sub__(self, num2):
        #! Logic to sub two nums
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)

num1 = Complex(1,3)
num1.show_num()

num2 = Complex(4,6)
num2.show_num()

num3 = num1 + num2
num4 =num1 - num2
num3.show_num()
num4.show_num()