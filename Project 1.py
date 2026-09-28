# To-Do List App - DecodeLabs Project 1

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"'{task}' added!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    print(f"'{removed}' removed!")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye! Tasks saved.")
        break

    else:
        print("Invalid choice! Try again.")
