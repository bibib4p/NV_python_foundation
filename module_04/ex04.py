# 5 Useful Math Functions
def is_even(num):
    return True if num % 2 == 0 else False


def sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def average(num1, num2):
    return round((num1 + num2) / 2, 3)


def maximum(num1, num2, num3=None):
    if num3 is None:
        if num1 >= num2:
            return num1
        else:
            return num2
    else:
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num3:
            return num2
        else:
            return num3


def minimum(num1, num2, num3=None):
    if num3 is None:
        if num1 <= num2:
            return num1
        else:
            return num2
    else:
        if num1 <= num2 and num1 <= num3:
            return num1
        elif num2 <= num3:
            return num2
        else:
            return num3


print(is_even(27))
print(sign(-0.95))
print(average(5, 10))
print(maximum(25, 25))
print(minimum(13, -5, 0))