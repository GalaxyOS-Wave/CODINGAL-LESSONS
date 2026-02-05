print("The triangle will be represented using numbers")
a = int(input("Enter number of rows"))
number = 1
for i in range (a):
    for j in range (i+1):
        print(number, end =' ')
        number = number + 1
    print()