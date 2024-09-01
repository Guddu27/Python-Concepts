# Program to find the factorial of first n numbers
# Using for loop

n = int(input("Enter number : "))

fact = 1

for i in range(1,n+1):
    fact *= i
print(f"Factorial  = {fact}")