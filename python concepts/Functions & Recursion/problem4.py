# Program to find factorial 

# Logic ---->
'''
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
'''

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(8)
    