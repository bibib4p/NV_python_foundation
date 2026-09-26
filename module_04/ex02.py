# Calculator Functions

def main():
    num1 = int(input("Enter a number: ").strip())
    num2 = int(input("Enter another number: ").strip())
    operator = input("Enter an operator ( + , - , * , / ): ").strip()
    result = calculate(num1, operator, num2)

    if result != "Invalid":
        print(f"The result: {result}")
    else:
        print(f"{result} Operator")


def calculate(num1, operator, num2):
    if operator not in ["+", "-", "*", "/"]:
        return "Invalid"

    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


main()

# Why can this be better than putting input() inside every function?
# Every function does whatever expected the operation and the code 
# is organized.