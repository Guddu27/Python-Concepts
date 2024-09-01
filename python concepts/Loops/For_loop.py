# For loops are used for sequential traversel 
'''
num = [1,2,3,4,5,6,7,8,9]
names = ["Sarthak", "Shubham", "Manas", "Siddhesh"]

for val in num:
    print(val)

for n in names:
    print(n)

str = "SarthakGatkal"

for char in str:
    print(char)

'''

# Optional else in for loops

str = "SarthakGatkal"

for char in str:
    if(char == 'h'):
        print("Char 'h' found")
        break
    print(char)
else:
    print("End")