def display_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.append(task)
            print(f"'{task}' has been added to your to-do list.")

        elif choice == "2":
            if todo_list:
                print("\nYour Tasks:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if todo_list:
                print("\nYour Tasks:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")
                try:
                    task_number = int(input("Enter the number of the task to delete: "))
                    removed_task = todo_list.pop(task_number - 1)
                    print(f"'{removed_task}' has been removed.")
                except (ValueError, IndexError):
                    print("Invalid task number.")
            else:
                print("Your to-do list is empty.")

        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
