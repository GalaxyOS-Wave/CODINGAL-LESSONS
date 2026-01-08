char = input("Enter a single character:")

if type(char) is str and len(char) == 1:
    print("Valid Input")
else:
    print("Please enter a valid input")

ascii_val = ord(char)

print(f"Character: {char}")
print(f"ASCII Value : {ascii_val} ")