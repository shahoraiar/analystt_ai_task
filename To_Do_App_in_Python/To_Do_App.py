class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"------------------{task} added successfully.------------------")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"------------------{deleted_task} deleted successfully.------------------")
        else:
            print("------------------Invalid task index.------------------")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            if "(Uncompleted)" in self.tasks[task_index]:
                self.tasks[task_index] = self.tasks[task_index].replace('(Uncompleted)', '(Completed)')
                print(f"------------------{self.tasks[task_index]} marked as completed.------------------")
            else:
                print(f"------------------{self.tasks[task_index]} is already completed.------------------")
        else:
            print("------------------Invalid task index.------------------")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"------------------{i + 1}. {task}------------------")
        else:
            print("------------------No tasks.------------------")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add task\n2. Delete task\n3. Mark task as completed\n4. Show tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task + ' (Uncompleted)')
        elif choice == '2':
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == '3':
            index = int(input("Enter index of task to mark as completed: "))
            todo_list.mark_task_completed(index - 1)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
