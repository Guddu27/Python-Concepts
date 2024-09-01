
#* Class Method : A class method is bound to the class & recieves the class as an implicit first argment
#! Note : Statis method can't access or modify class state & generally for utility.

class Person:
    name = "Anonymous"

    # def change_name(self, name):
    #     self.__class__.name = "Sarthak Gatkal"
    #     #*self.__class__.

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Rohan")
print(p1.name)
print(Person.name)


#* @staticmethod
#* @classmethod(cls)
#* @instanemethod(self)

