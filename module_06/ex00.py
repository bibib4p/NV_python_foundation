def main():
    name = input("What is your name? ").strip().title()

    likes_art = ask_yes_no("Do you enjoy art?")
    likes_science = ask_yes_no("Do you enjoy science?")
    likes_coding = ask_yes_no("Do you enjoy coding?")
    likes_others = ask_yes_no("Do you enjoy working with others?")
    likes_projects = ask_yes_no("Do you enjoy building projects?")

    yes_count, themes = calculate_level(likes_art, likes_science, likes_coding, likes_others, likes_projects)
    show_summary(name, yes_count, themes)


def ask_yes_no(question):
    # if right side expression evaluates to true, return True
    return input(f"{question} (yes/no): ").strip().lower() == "yes"


def calculate_level(art, science, coding, others, projects):
    yes_count = 0
    themes = ""

    if art:
        yes_count += 1
        themes += "creativity, "
    if science:
        yes_count += 1
        themes += "curiosity, "
    if coding:
        yes_count += 1
        themes += "technology, "
    if others:
        yes_count += 1
        themes += "collaboration, "
    if projects:
        yes_count += 1
        themes += "projects, "

    themes = themes.rstrip(", ")
    return yes_count, themes


def show_summary(name, yes_count, themes):
    print("\nYOUR SUMMARY")

    if yes_count >= 4:
        print(f"{name}, you are a curious explorer! You seem to enjoy learning through {themes}.")
    elif yes_count >= 2:
        print(f"{name}, you are a developing explorer. You have several interests that you can continue exploring.")
    else:
        print(f"{name}, you are beginning your exploration. Try different activities and discover what interests you.")


main()
