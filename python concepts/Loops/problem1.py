# Create table of number given by user 

n = int(input("Enter the number for the table : "))

i = 1
while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1 