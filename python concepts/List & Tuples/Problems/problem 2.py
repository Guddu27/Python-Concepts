# Check if a list contains a palindrome of elements

list = [1,2,3,2,1]

# Making copy for comparison

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("The given list is a palindrome")
else:
    print("Given list is not a palindrome")