
# Problem : Search for the number given by the usr

num = [1,4,9,16,25,36,49,64,81,100]

x = int(input("Enter number to search : "))

i = 0
while i < len(num):
    if(num[i] == x):
        print("Finding your Number...")
        print(f"Number found at index : {i}")
    i += 1