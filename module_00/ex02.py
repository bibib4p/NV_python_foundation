# 1st Error - Missing Parathesis
# print("Hello, World"
# I omitted the closing parathesis

# File "C:\Users\bibi\Desktop\NV_python_foundation\module_00\ex02.py", line 1
#     print("Hello, World"
#          ^
# SyntaxError: '(' was never closed

# It means I forgot the closing parathesis for the correct syntax
# print("Hello, World");





# 2nd Error - Syntax Error
# print('My name's Kyar Phyu')
# I added a single quote between the single quotes

# File "C:\Users\bibi\Desktop\NV_python_foundation\module_00\ex02.py", line 14
#     print('My name's Kyar Phyu')
#                               ^
# SyntaxError: unterminated string literal (detected at line 14)

# Python thinks the string ended after I wrote the apostrophe but then there is more text and another single quote

# I can fix it by using double quotes or using the escape character backslash
# print("My name's Kyar Phyu")
# print('My name\'s Kyar Phyu')





# 3rd Error - Calliing a function that does not exist
# prnt("Hello, World")
# I omitted a i in print()

# File "C:\Users\bibi\Desktop\NV_python_foundation\module_00\ex02.py", line 37, in <module>
#     prnt("Hello, World")
#     ^^^^
# NameError: name 'prnt' is not defined. Did you mean: 'print'?

# Because I forgot the i in print, Python says a function called prnt 
# is not defined, and Python also guesses that I might have misspelled the
# function print()



