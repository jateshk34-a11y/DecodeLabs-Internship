tasks = []

while True:
    print("==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. show Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter the Choice: ")

    if choice == "1":
        task = input("Enter the task ")
        tasks.append(task)
        print("Task Added! ")

    elif choice == "2":
        print("Your Tasks")
        for i in tasks:
            print(i)

    elif choice == "3": 
        print(tasks)
        choice1 = int(input("Enter task number to delete: "))

        if 1 <= choice1 <= len(tasks):
            del tasks[choice1 - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exit")
        break     

    else:
        print("Invalid")    



