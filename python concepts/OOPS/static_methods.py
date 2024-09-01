
#? Static Methods : They don't use the self parameter.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #! DECORATOR 
    def hello():
        print("Hello StaticMethod here!")

#! To calculate average marks of the student : 
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name}, Your average : {sum/3}")

s1 = Student("Sarthak Gatkal", [99,98,90])
s1.get_avg()

s1.name = "Purushottam Patil"
s1.get_avg()
s1.hello()
 
 



