# Digital Person
person = {"name": "Felix", "age": 30, "city": "Quebec City", "interests": ["games", "music", "drama"]}

print(f"Name: {person["name"]}\nAge: {person.get("age")}\nCity: {person["city"]}\nInterests:")
for interest in person["interests"]:
    print(f"- {interest}")


# Why might a dictionary be better than a list here?
# A dictionary is better because it is more readable and organized
