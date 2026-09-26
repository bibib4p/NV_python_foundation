# Food Recommendation System

import time

Asian = [
    {"spice": "Sweet", "weight": "Light", "dish": "Ginger Salad"},
    {"spice": "Sweet", "weight": "Heavy", "dish": "Sushi"},
    {"spice": "Spicy", "weight": "Light", "dish": "Papaya Salad"},
    {"spice": "Spicy", "weight": "Heavy", "dish": "Yangnyeom Fried Chicken"},
]

Mediterranean = [
    {"spice": "Sweet", "weight": "Light", "dish": "Greek Salad"},
    {"spice": "Sweet", "weight": "Heavy", "dish": "Pepperoni and Cheese Pizza"},
    {"spice": "Spicy", "weight": "Light", "dish": "Spicy Herb Tabbouleh"},
    {"spice": "Spicy", "weight": "Heavy", "dish": "Bucatini all'Amatriciana"},
]


def main():
    food_type = get_food_type()
    spice = get_spice()
    weight = get_weight()

    dish = find_dish(food_type, spice, weight)

    if dish:
        print("Calculating recommendation", end=" ")
        # Slowly printing . . . for anticipation
        for i in range(3):
            print(".", end=" ", flush=True)
            time.sleep(1)

        print(f"\nBased on your choices, you should eat {dish}\n")

    else:
        print("Please enter a valid option.")


def get_food_type():
    while True:
        food_type = input("What kind of food are you craving Asian or Mediterranean? ").strip().title()
        if food_type == "Asian":
            return "Asian"
        
        # For when user spelt wrong
        elif food_type.startswith("Medi"):
            return "Mediterranean"
            
        print("Please choose Asian or Mediterranean.")


def get_spice():
    while True:
        spice = input("Are you in the mood for something sweet or spicy? ").strip().capitalize()
        if spice in ["Sweet", "Spicy"]:
            return spice
        print("Please enter sweet or spicy.")


def get_weight():
    while True:
        weight = input("Do you want something light or heavy to eat? ").strip().capitalize()
        if weight in ["Light", "Heavy"]:
            return weight
        print("Please enter light or heavy.")


def find_dish(food_type, spice, weight):
    if food_type == "Asian":
        menu = Asian
    else:
        menu = Mediterranean

    # food = each dictionary in menu list
    for food in menu:
        if food["spice"] == spice and food["weight"] == weight:
            return food["dish"]


main()
