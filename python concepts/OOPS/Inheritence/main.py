# Inheritence : When one class(chile/derived) derives the properties & methods of another class(parent/base).
# MUltilevel Inheritence

#* Parent class
class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

#* Child-Parent Class
class KiaCar(Car):
    def __init__(self, brand):
        self.brand = brand

#* Child CLass
class Sonet(KiaCar):
    def __init__(self,type):
        self.type = type

car1 = Sonet("Disel")
car1.start()

#//                                                 

#! Types of Inheritence : 

# Single Inheritence : (Base(Parent Class))-->(Derived(Child Class))
# Multi-level Inheritence : (Base(Parent Class))-->(Derived(Child.parent Class))-->(Derived(Child Class))
# Multiple Inheritence : 

