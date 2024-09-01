# Sets in Python

'''
~ Set is collection of the unordered items
~ Each element in the set must be unique & immutable

'''
#---------------------------------------------------

'''

collection = {1,2,3,4}
print((collection))

null_dict= {} #empty dictionary

null_set = set() #empty set

print(type(null_set))

---------------------------------------------------

Set Methods

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add("Sarthak Gatkal")
collection.remove(3)

print(collection.pop())

---------------------------------------------------

'''

# UNION & INTERSECTION

'''
 >> set.union(set2) combines both set values & returns new
 >> set.intersection(set2) combines common values & returns new
'''

'''

# UNION : 
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))

#INTERSECTION : 

seta = {1,2,3}
setb = {2,3,4}
print(seta.intersection(setb))

'''