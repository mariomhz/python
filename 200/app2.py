tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['desc']} [{status}]")

def add_task():
    inp = input("enter a task: ").strip()
    tasks.append({"desc": inp, "done": False})
    print("task added!")

def mark_task():
    show_tasks()
    try:
        i = int(input("enter task number to mark as completed:"))
        tasks[i - 1]["done"] = True
        print("task marked as completed")
    except (ValueError, IndexError):
        print("invalid task number...")

def delete_task():
    show_tasks()
    try:
        i = int(input("enter task number to delete:"))
        removed = tasks.pop(i - 1)
        print(f"deleted: {removed['desc']}")
    except (ValueError, IndexError):
        print("invalid task number...")

def move_task():
    show_tasks()
    try:
        i = int(input("enter task number to delete:")) - 1
        new_pos = int(input("enter new position:")) - 1
        task = tasks.pop(i)
        tasks.insert(new_pos, task)
        print("task moved!")
    except (ValueError, IndexError):
        print("invalid input...")
        
while True:
    print("\nOptions: [1] view [2] add [3] complete [4] delete [5] move [6] exit")
    choice = input("choose an option: ").strip()
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        move_task()
    elif choice == "6":
        print("goodbye! exiting program now...")
        break
    else: print("invalid option! try again!")
    