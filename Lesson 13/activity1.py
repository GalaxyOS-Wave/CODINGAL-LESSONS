print("The triangle will be made up of *s")
a = int(input("Enter the number of ROWS:"))
for i in range (a):
    for j in range (i+1):
        print("*",end ="")
    print()
