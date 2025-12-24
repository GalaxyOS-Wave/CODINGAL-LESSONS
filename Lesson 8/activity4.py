a=int(input("ENTER SPEED1:"))
b=int(input("ENTER SPEED2:"))
c=int(input("ENTER SPEED3:"))

avg = (a+b+c)/3
print("average:",avg)

if (a < avg):
    print("Speed 1 is slower")
if (b < avg):
 print("Speed 2 is slower")
if (c < avg):
 print("Speed 3 is slower")
