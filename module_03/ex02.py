# Multiplication Table
multiplicand = int(input("Enter a whole number: "))
multiplier = int(input("Enter how many times to multiply: "))

for num in range(1, multiplier+1):
    print(f"{multiplicand} x {num} = {multiplicand*num}")