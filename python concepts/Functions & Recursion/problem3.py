# Program to print list elements on same line

cities = ["Delhi", "Mumbai", "Kolkata", "Pune", "Nashik", "Chennai"]
heroes = ["Ironman", "Hulk", "Captain America", "Thor"]

# print(heroes[0], end=" ")
# print(heroes[1], end=" ")

def print_length(list):
    print(f"Lenght of list : {len(list)}")

def print_list(list):
    for item in list:
        print(item, end=" ")

print_length(cities)
print_list(cities)
