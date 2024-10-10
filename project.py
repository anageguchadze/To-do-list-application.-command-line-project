from tabulate import tabulate

#In the main function, there is a menu where the user can choose the desired option.
def main():
    task_list = []
    while True:
        menu = ["Add task", "View tasks", "Remove task", "Edit task", "Exit"]

        headers = ["\nChoose an option:"]
        menu = [[count, item] for count, item in enumerate(menu, start=1)]
        print(tabulate(menu, headers=headers, tablefmt="rst"))

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            remove_task(task_list)
        elif choice == "4":
            edit_task(task_list)
        elif choice == "5":
            print("Exiting. Tasks saved.")
            break
        else:
            print("Invalid choice, please select number from menu. ")

#The view_tasks function allows us to view our Todo list if it has already been filled.
def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks in list.")
    else:
        headers = ["\nYour","\ntasks:"]
        task_list = [[count, item] for count, item in enumerate(task_list, start=1)]
        print(tabulate(task_list, headers=headers, tablefmt="simple"))

#In this function we can add tasks into our Todo list.
#if we don't write anything and press enter the program will take us to the menu.
def add_task(task_list):
    while True:
        task = input("Enter a task or press ENTER to return to menu: ")
        if len(task) != 0:
            task_list.append(task)
            continue
        else:
            print("Tasks have been added.")
            break

#In this function we can choose the task which we have already done and remove it.
def remove_task(task_list):
    while True:
        num = input("Enter task number to remove, or press ENTER to return to menu: ").strip()
        if len(num) == 0:
            break
        if num.isalpha():
            print("Wrong input. Please enter task number.")
            continue
        num = int(num)
        if num >= 1 and num <= len(task_list):
            del task_list[num-1]
            headers = ["\nYour","\ntasks:"]
            task_list = [[count, item] for count, item in enumerate(task_list, start=1)]
            print(tabulate(task_list, headers=headers, tablefmt="simple"))
            continue
        else:
            print(f"Invalid input. You have {len(task_list)} tasks in your list.")

#In the function edit_task we can choose our task from Todo list and change description.
def edit_task(task_list):
    while True:
        view_tasks(task_list)
        if len(task_list) == 0:
            break
        try:
            task_number = int(input("Enter the number of the task you want to edit: "))
            if 1 <= task_number <= len(task_list):
                new_task = input("Enter the new task description: ")
                task_list[task_number-1] = new_task
                print("Task updated successfully.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()



