# Simple To-Do List Program (Beginner Friendly)

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

while True:
    print("====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!\n")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if tasks:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Task '{removed}' deleted!\n")
            else:
                print("⚠️ Invalid number!\n")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("Please enter a valid option (1-4).\n")

