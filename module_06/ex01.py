# Temperature Converter

def main():
    while True:
        print("\nTEMPERATURE CONVERTER")
        print("--------------------------")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("Choose 1 or 2: ")
        print("--------------------------")
        action = input("Action: ").strip().replace(".", "")

        if action == "1":
            celcius = float(input("Enter Temperature: "))
            celcius_to_fahrenheit(celcius)

        elif action == "2":
            fahrenheit = float(input("Enter Temperature: "))
            fahrenheit_to_celcius(fahrenheit)

        else:
            print("Quitting progam ...")
            exit()


def celcius_to_fahrenheit(celcius):
    fahrenheit = round((celcius * (9 / 5)) + 32, 2)
    print(f"{celcius}°C = {fahrenheit}°F")


def fahrenheit_to_celcius(fahrenheit):
    celcius = round((fahrenheit - 32) * (5 / 9), 2)
    print(f"{fahrenheit}°F = {celcius}°C")

main()