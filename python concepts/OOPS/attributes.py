'''
Attributes : 
1. Class attributes --> common for all objects
2. Instance attributes
'''

#! A data which is different for different object we write them as self.""


class Student:
    college_name = "RJSPM College" #! Class Attribute
    name = "Anonymous"
    def __init__(self):
        print("Adding new student in Database..")

    def __init__(self, name, marks):
        self.name = name #! object attribute > class attribute
        self.marks = marks
        
s1 = Student("Sarthak Gatkal", 97) #! Object Attribute
print(s1.name, s1.marks, s1.college_name)
s2 = Student("Purushottam Patil", 12)
print(s2.name, s2.marks, s2.college_name)
