# Study Task Manager
tasks = []

def main():
    while True:
        print("--- To Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose 1-4: ").strip().replace(".", "")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            exit()
        else:
            print("\nPlease enter a valid choice!")

        print("---------------------------------")


def add_task():
    add_another_task = "y"
    while add_another_task == "y":
        task = input("\nEnter a new task: ").strip()
        tasks.append(task)
        print("Task added!")
        add_another_task = input("Do you wish to add another task(y/n)? ").strip().lower()
        while add_another_task != "y" and add_another_task != "n":
            print("Please enter y or n")
            add_another_task = input("Do you wish to add another task(y/n)? ").strip().lower()


def view_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("There are no tasks")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1} - {tasks[i]}")
    print()


def remove_task():
    view_tasks()
    if tasks:
        task_number = int(input("Enter task number to remove: ").strip().replace(".", ""))
        while task_number < 1 or task_number > len(tasks):
            print(f"There is only {len(tasks)} task(s)")
            task_number = int(input("Enter task number to remove: ").strip())
        tasks.pop(task_number - 1)

main()
