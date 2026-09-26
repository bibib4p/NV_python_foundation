# Temperature Converter
def celcius_to_fahrenheit(celcius):
    fahrenheit = round((celcius * (9 / 5)) + 32, 2)
    print(f"Fahrenheit: {fahrenheit}°F")


def fahrenheit_to_celcius(fahrenheit):
    celcius = round((fahrenheit - 32) * (5 / 9), 2)
    print(f"Celcius: {celcius}°C")


celcius_to_fahrenheit(0)
celcius_to_fahrenheit(-6.67)
celcius_to_fahrenheit(-40.00)

fahrenheit_to_celcius(212)
fahrenheit_to_celcius(160)
fahrenheit_to_celcius(0)
