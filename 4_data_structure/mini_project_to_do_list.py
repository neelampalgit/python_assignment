def todo_list_manager():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == 2:
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found.")
        elif choice == 3:
            print("Tasks:", tasks)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")


todo_list_manager()
