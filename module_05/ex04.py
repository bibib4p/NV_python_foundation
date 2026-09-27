# Student Scores
student_records = {}


def main():
    while True:
        print("--------------------------")
        print("Choose an action:")
        print("1. Add Student Records")
        print("2. Show Student Records")
        print("3. Show Class Summary")
        print("4. Quit")
        print("--------------------------")
        action = input("Action: ").strip().replace(".", "")

        if action == "1":
            add_student_records()
        elif action == "2":
            if student_records:
                show_student_records()
            else:
                print("There are no records yet")
        elif action == "3":
            if student_records:
                show_class_summary()
            else:
                print("Please fill in student records first!")
        elif action == "4":
            exit()
        else:
            print("Please enter valid action!")


def add_student_records():
    add_another_record = "y"
    while add_another_record == "y":
        name = input("Enter new student name: ").strip().title()
        score = int(input("Enter student score: ").strip())
        student_records[name] = score
        add_another_record = input("Do you wish to add another record(y/n)? ").strip().lower()
        while add_another_record != "y" and add_another_record != "n":
            print("Please enter y or n")
            add_another_record = input("Do you wish to add another record(y/n)? ").strip().lower()


def show_student_records():
    for students in student_records:
        print(f"{students}: {student_records[students]}")


def show_class_summary():
    print(f"Highest score: {get_highest()}")
    print(f"Lowest score: {get_lowest()}")
    print(f"Class average: {get_average()}")


def get_highest():
    score_list = student_records.values()
    return max(score_list)


def get_lowest():
    score_list = student_records.values()
    return min(score_list)


def get_average():
    score_list = student_records.values()
    return sum(score_list) / len(score_list)


main()
