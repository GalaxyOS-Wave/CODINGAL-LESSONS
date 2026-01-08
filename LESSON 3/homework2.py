
def calculate_square_root(number):
  if number < 0:
    return "Error: Cannot calculate the square root of a negative number."
  else:
    
    result = number ** 0.5
    return result


num = float(input("Enter a number to find its square root: "))

squareresult = calculate_square_root(num)

print(f"The square root of {num} is: {squareresult}")
