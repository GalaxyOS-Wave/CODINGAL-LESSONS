a=int(input("CP:"))
b=int(input("SP:"))
if b>a:
    print("You are in profit")
    amount=b-a
    print("your amount is:",amount)
else:
    print("You are in loss")
    amount=b-a
    print("your amount is:",amount)