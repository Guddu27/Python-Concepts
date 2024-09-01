# Program to find the sum of n natural numbers : 

n = int(input("Enter number : "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(f"Total sum from 1 to {n} is : {sum}")