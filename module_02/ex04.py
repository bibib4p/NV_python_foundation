# Food Recommender
"""
Asian Food
sweet, light -> Sushi
sweet, heavy -> Sushi

spicy, light -> Papaya Salad
spicy, heavy -> Yangnyeom Fried Chicken
--------------------------------------------
Mediterrnean Food
sweet, light -> Greek Salad
sweet, heavy -> Pepperoni and Cheese Pizza

spicy,light -> Spicy Herb Tabbouleh
spicy, heavy -> Bucatini all'Amatriciana
"""

import sys

japanese = "Sushi"
thai = "Papaya Salad"
korean = "Yangnyeom Fried Chicken"

greek = "Greek Salad"
turkish = "Spicy Herb Tabbouleh"
italian_sweet = "Pepperoni and Cheese Pizza"
italian_spicy = "Bucatini all'Amatriciana"


user_food_type = input("What kind of food are you craving Asian or Mediterranean? ").strip().title()

if not user_food_type.startswith("Asian") and not user_food_type.startswith("Medi"):
    print("Please chose Asian or Mediterranean.")
    sys.exit()

spice = input("Are you in the mood for something sweet or spicy? ").strip().capitalize()
weight = input("Do you want something light or heavy to eat? ").strip().capitalize()

if user_food_type == "Asian":

    if spice == "Sweet" and weight == "Light" or weight == "Heavy":
        print(f"Calculating recommendation...\nBased on your choices, you should eat {japanese}")

    elif spice == "Spicy":
        if weight == "Light":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {thai}")

        elif weight == "Heavy":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {korean}")
    else:
        print("Please enter a valid option.")

elif user_food_type.startswith("Me"):

    if spice == "Sweet":
        if weight == "Light":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {greek}")

        elif weight == "Heavy":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {italian_sweet}")

    elif spice == "Spicy":
        if weight == "Light":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {turkish}")

        elif weight == "Heavy":
            print(f"Calculating recommendation...\nBased on your choices, you should eat {italian_spicy}")

    else:
        print("Please enter a valid option.")
