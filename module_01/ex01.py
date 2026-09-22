# swapping values
# 1st solution: using temporary buffer location
a = 20
b = 10

temp = a
a = b
b = temp

print(a, b)

# 2nd solution: subtracting and adding to get desired values
a = 20
b = 10

a = a - b
b = b + b
print( a, b)

# 3rd solution: using tuples unpacking
# searched and learned method
a, b = 20, 10
a, b = b, a

print(a, b)
