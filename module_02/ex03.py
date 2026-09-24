# temperature advisor
temperature = int( input("What's the temperature in Celcius? "))

if temperature < 0:
    print("It is cold.")

elif 0 <= temperature <= 25:
    print("It is comfortable.")

else:
    print("It is hot")

# If one range ends at 20 and another starts at 20, what happens?
# Both the print statemnets would print out.