
#! Constructor : 

class student : 

    #! Default constructors : 
    def __init__(self):
        print("Adding new student in Database..")

    #! Parameterized constructors : 
    def __init__(self, fullname, marks): #calls itself
        self.name = fullname
        self.marks = marks
        # print(self)
        
    
s1 = student("Sarthak", 92)
s2 = student("Mahesh Dalle", 20)
print(s1.name, s1.marks)
print(s2.name, s2.marks)
