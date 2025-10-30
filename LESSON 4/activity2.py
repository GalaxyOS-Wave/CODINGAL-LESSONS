amount=int(input("please enter the amount:"))

note_1= amount//500
note_2=(amount%500)//100
note_3=((amount%500)%100)//50
note_4=(((amount%500)%100)%50)//10

print("Total number of 500 rupees note",note_1)
print("Total number of 100 rupees note",note_2)
print("Total number of 50 rupees note",note_3)
print("Total number of 10 rupees note",note_4)