# Calculator

# MISSION
# Ask for two numbers. Display addition, subtraction, multiplication, and division.
# CHALLENGE
# ● Remainder
# ● Exponentiation
# EDGE CASE
# What happens when the second number is 0? Do not ignore the problem — investigate it.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"addition: {num1 + num2}")
print(f"subtraction: {num1 - num2}")
print(f"multiplication: {num1 * num2}")
print(f"division: {num1 / num2}")
print(f"remainder: {num1 % num2}")
print(f"exponentiation: {num1 ** num2}")

# What happens when the second number is 0? Do not ignore the problem — investigate it.
r"""
  File "C:\Users\bibi\Desktop\NV_python_foundation\module_01\ex03.py", line 17, in <module>
    print(f"division: {num1 / num2}")
                       ~~~~~^~~~~~
ZeroDivisionError: division by zero
"""
r"""
    File "C:\Users\bibi\Desktop\NV_python_foundation\module_01\ex03.py", line 18, in <module>
        print(f"remainder: {num1 % num2}")
                            ~~~~~^~~~~~
    ZeroDivisionError: division by zero
"""

# Python throws a ZeroDivisionError since mathematically you can't divide a number by 0