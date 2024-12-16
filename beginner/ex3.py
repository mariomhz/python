# to do list
tasks = []

def display_menu():
    print("\nTo-do list: ")
    print("1. view tasks")
    print("2. add a task")
    print("3. exit")
    
def view_tasks():
    if not tasks:
        print("\nto-do list is empty!")
    else:
        print("\nyour to-do list: ")
        for task in tasks:
            print(f"- {task}")

def add_task():
    task_name = input("enter the task to add: ").strip()
    tasks.append(task_name)
    print(f"the task '{task_name}' has been added.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1": view_tasks()
        if choice == "2": add_task()
        elif choice == "3":
            print("exiting the to-do list application. Bye!")
            break
    else:
        print("invalid choice please try again.")

if __name__ == "__main__":
    main()
