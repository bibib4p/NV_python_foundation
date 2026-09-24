# 1st Approach: Using a for loop and conditional statement if
# Even Numbers between 0 and 100
print("Even Numbers")
for num in range(0, 101):
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd Numbers")
for num in range(0, 101):
    if num % 2 != 0:
        print(num, end=" ")

print("\n")

# 2nd Approach: Using step in range
print("Even Numbers")
for num in range(0, 101, 2):
    print(num, end=" ")

print("\nOdd Numbers")
for num in range(1, 101, 2):
    print(num, end=" ")

print("\n")

# 3rd Approach: Using Reassignment and only 1 loop
even_numbers = ""
odd_numbers = ""

for num in range(0, 101):
    if num % 2 == 0:
        even_numbers += str(num) + " "
    else:
        odd_numbers += str(num) + " "


print(f"Even Numbers\n{even_numbers}")
print(f"Odd Numbers\n{odd_numbers}")
