
# ! -------------------------------------------------------
# ! Problem 1

# with open("Practice.txt", "w") as f:
#     f.write("Hello everyone\ni am learning file i/o\n")
#     f.write("using Java.\nI like programming in Java")
    
# ! -------------------------------------------------------
# ! Problem 2

# with open("Practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("Practice.txt", "w") as f:
#     f.write(new_data)

# ! -------------------------------------------------------
# ! Problem 3

# word = "learning"
# with open("Practice.txt","r") as f:
#     data =  f.read()
#     if(data.find(word) != -1):
#         print("Found!!")
#     else:
#         print("Not Found")

# ! -------------------------------------------------------

# ! Problem 4

# def check_for_line():
#     word = input("Enter the word to search : ")
#     data = True
#     line_no = 1
#     with open("Practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(f"Word Found at line no : {line_no}")
#                 return
#             line_no += 1

#     return -1

# check_for_line()

# ! -------------------------------------------------------

# ! Problem 5

# WAP to find the even numbers fo the txt file 
count = 0
with open("num.txt") as f:
    data = f.read()

    num = data.split(",")
    for val in num : 
        if(int(val)%2 == 0):
            count += 1 
    print(count)