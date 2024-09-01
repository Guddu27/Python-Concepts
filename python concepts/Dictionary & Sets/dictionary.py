'''
Dictionaries in Python are mutable
Dictionaries are unordered
Cannot create duplicate keys

---------------------------------------------------

dict = {
    "Name" : "Sarthak Gatkal",
    "Subjects" : ['Python', 'C', 'Data Science'],
    "Topics" : ('Dict', 'Tuples', 'Strings'),
    "Class" : "Second Year",
    "CGPA" : 8.16,
    "Age" : 19,
    "Is_Adult" : True
}
print(dict)

---------------------------------------------------

# Changing Values using keys

dict["Name"] = "Guddu Bhaiya"
dict["Class"] = "First Year"
dict["Aim"] = "Data Scientist"
print(f"\n{dict}")

Null dictionary

null_dict = {}
null_dict["Name"] = "Sarthak Gatkal"

---------------------------------------------------

[NESTED DICTIONARY]

student = {
    "name" : "Sarthak Gatkal",
    "subject" : {
        "phy": 97,
        "maths": 87,
        "eng": 99
    }
}

print(student["subject"])

---------------------------------------------------

Dictionary Methods
 
print(student.keys()) 

TypeCasting

print(list(student.keys()))
print(len(list(student.keys())))
print(list(student.values()))

pairs = list(student.items())
print(pairs[1])

print(student["name2"]) # Gives error
print(student.get("name2")) # No error will be shown 

updt = {
    "City" : "Pune",
    "Village" : "Bhosari",
    "Age" : 19
}
student.update(updt)
print(student)

'''