units =int(input("Please enter Number of Units you consumed:"))
if(units<50):
    amount =units * 2.60
    sumcharge = 25
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    sumcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200)) * 8.45
    sumcharge = 25

total = amount + sumcharge
print("\nElectricity Bill = %2f" %total)