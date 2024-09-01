# Logic : 

# 5! = 1*2*3*4*5
# 4! = 1*2*3*4
# 3! = 1*2*3
# 2! = 1*2
# n! = (n-1)!*n

# fact(n) = fact(n-1) * n

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))