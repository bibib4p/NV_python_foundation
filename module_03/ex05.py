# Find the largest number

# Out put:
# numbers = [14, 52, 8, 91, 37, 65]
# The largest number in the collection is: 91

"""
1) Ask the user to choose a number between 2 to 6
2) Ask for that many numbers
3) Store them in a list
4) Store the first number in the container
5) Go thru them 1 by 1
6) compare the first number in container with the second number
7) if second number is bigger, separate it in the container (or verce versa)
8) compare the number in container with the next number
9) if smaller do nothing, if bigger replace in container and repeat ...
10) print out the number list and max number
"""

length = int(input("Choose a number between 2 to 6: ").strip())
while length not in range(2, 7):
    print("\nPlease choose a valid number")
    length = int(input("Choose a number between 2 to 6: ").strip())

number_list = []

for num in range(0, length):
    number_list.append(int(input(f"Please type in any {length} numbers:\n")))

max_number = number_list[0]

for num in range(length):
    if number_list[num] > max_number:
        max_number = number_list[num]

print(f"Output:\nnumbers = {number_list}\nThe largest number in the collection is: {max_number}")

"""
Algorithm
An algorithm is a set of step by step instructions designed to solve a problem or complete a task.

Python Code 
a set of instructions, written in a Python, that forms part of a program.

An algorithm is the logical steps to solve a problem written in plain English, whereas Python code is the implementation
of those steps written in code Python can understand.
"""

