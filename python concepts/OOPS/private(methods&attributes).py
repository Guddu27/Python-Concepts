# PUBLIC & PRIVATE ATTRIBUTES AND METHODS

'''
Private attributes & methods : Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        #!(__) makes attribute private
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass) # Can be accessed within the class

acc1 = Account("12345", "AbCdE")
print(acc1.acc_no)
# print(acc1.__acc_pass) #! Cannot be accessed outside the class
print(acc1.reset_pass())

#!-----------------------------------------------------

class Person :
    __name = "Anonymous"

    def __hello(self):
        print("Hello everyone!")
    
    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name)
# print(p1.__hello)
print(p1.welcome())

