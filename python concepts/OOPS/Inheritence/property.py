
#! Property
#* We use property decorator on any metod in th class to use the method as a property.

class  Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        

    # def cal_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


stud1 = Student(98, 87, 97)
print(stud1.percentage)
stud1.phy = 65
print(stud1.percentage)