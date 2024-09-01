# Write a recursive function to print first n natural numbers

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n 

sum = cal_sum(6)
print(sum)
