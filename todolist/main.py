class ToDoList:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        """Add a task:"""
        if task.strip() == "":
            print("task cant be empty!")
            return
        self.tasks[task] = False
        print(f"task added: {task}")
    
    def display_tasks(self):
        if not self.tasks:
            print("list is empty...")
            return

        print("\nTO DO LIST:")
        for idx, (task, completed) in enumerate(self.tasks.items(), start=1):
            status = "[✓]" if completed else "[ ]"
            print(f"{idx}. {status} {task}")
    
    def mark_completed(self, task_number):
        """Mark a task as completed"""
        if 1 <= task_number <= len(self.tasks):
            task = list(self.tasks.keys())[task_number - 1]
            self.tasks[task] = True
            print(f"task marked as completed: {task}")
    
    def run(self):
        """Main loop"""
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")
            
            choice = input("enter your choice: ").strip()
            
            if choice == "1":
                task = input("enter the task: ").strip()
                self.add_task(task)

            elif choice == "2":
                self.display_tasks()

            elif choice == "3":
                self.display_tasks()
                try:
                    task_number = int(input("enter the task number to mark as completed: "))
                    self.mark_completed(task_number)
                except ValueError:
                    print("please enter a valid number!")

            elif choice == "4":
                print("exiting the to-do list. Goodbye!")
                break

            else:
                print("invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()