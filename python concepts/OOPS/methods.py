# Methods are functions that belongs to the Class

class Student :

    college_name ="RJSPM College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Hello", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Sarthak Gatkal", 98)
s1.hello()
print(s1.get_marks()) 