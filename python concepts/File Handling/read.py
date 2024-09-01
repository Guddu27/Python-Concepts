# File handling 

with open("main.txt", 'r') as f:
    line1 = f.readline()
    print(line1)

    line2 = f.readline()
    print(line2)

    line3 = f.readline()
    print(line3)

    line4 = f.readline()
    print(line4)

f.close()



















# ! Modes of handling a file : 
'''
'r' = Open in reading mode
'w' = Open for writing mode
'x' = create new file and open for writing
'a' = open for writing appending to end of the file
'b' = binary mode
't' = text mode
'+' = open a disk file for updating(reading or writing)
'''



