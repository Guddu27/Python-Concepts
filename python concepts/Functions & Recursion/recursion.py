 # Recursion : When a function itself repeatedly

def show(n):
    if(n == 0):
        return #--> Base case
    print(n)
    show(n-1) #--> Calling itself
    print("END")

show(3) # 4=n-1, 3=n-2, 2=n-3, 1=n-4

# Call Stack : when functions get called one by one they get stacked up




