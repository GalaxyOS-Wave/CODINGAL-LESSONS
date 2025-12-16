a=int(input("put your marks 1:"))
b=int(input("put your marks 2:"))
c=int(input("put your marks 3:"))
d=int(input("put your marks 4:"))
e=int(input("put your marks 5:"))

total = a+b+c+d+e 
avg = total/5
print("Your average is:",avg)

if avg>=91 :
    print("Your Grade is A1")

elif avg>=80 :
    print("Your Grade is A2")

elif avg>=70 :
    print("Your Grade is b1")
    
elif avg>=60 :
    print("Your Grade is b1")

else:
    print("you failed , better luck next time")