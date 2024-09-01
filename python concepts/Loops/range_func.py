# Range function returns a sequence of numbers, starting from 0 by default, and incremants by 1(by default), and stops before a specified number

# seq = range(11)

# for i in seq:
#     print(i)

# for i in range(2,51,2):
#     print(i) # Prints All even numbers 

# Multiplication table using for loop

n = int(input("Enter number : "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")