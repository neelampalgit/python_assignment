import json


class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def to_dict(self):
        return {"title": self.title, "description": self.description, "status": self.status}


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task.to_dict())
        self.save_tasks()

    def update_task(self, title, status):
        for task in self.tasks:
            if task["title"] == title:
                task["status"] = status
                self.save_tasks()
                return
        print("Task not found!")

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task["title"] != title]
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(f"Title: {task['title']}, Status: {task['status']}")


def task_manager():
    manager = TaskManager()

    while True:
        print("\n1. Create Task")
        print("2. Update Task Status")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)
        elif choice == 2:
            title = input("Enter task title to update: ")
            status = input("Enter new status (Pending/Completed): ")
            manager.update_task(title, status)
        elif choice == 3:
            title = input("Enter task title to delete: ")
            manager.delete_task(title)
        elif choice == 4:
            manager.list_tasks()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


task_manager()
