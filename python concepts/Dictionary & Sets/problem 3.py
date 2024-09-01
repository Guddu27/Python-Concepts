# Problem : take input from user and put in a dictionary

marks = {}

phy = int(input("Enter marks of Physics : "))
marks.update({"Physics" : phy})

chem = int(input("Enter marks of Chemistry : "))
marks.update({"Chemistry" : chem})

math = int(input("Enter marks of Mathematics : "))
marks.update({"Maths" : math})

print(marks)