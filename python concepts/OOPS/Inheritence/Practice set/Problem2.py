
#! Define an Employee class with attributes , role ,department & salary. This class also has a shoeDetails() method.
#! Create an Engineer class which inherits properties of the Employee & has additional attributes : name & age


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"Role : {self.role}")
        print(f"Department : {self.dept}")
        print(f"Salary : {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Data Scientist", "IT", "86000")

    def showInfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


eng1 = Engineer("Sarthak Gatkal", 20)
eng1.showInfo()
eng1.showDetails()
