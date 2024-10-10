#Todo list
#Video Demo:  https://www.youtube.com/watch?v=k9xIiwcK1KU&t=3s
#Description:
#Welcome to the Todo list application! This Python-based command-line tool helps you to manage your tasks effectively. The program provides a menu where the user can create a Todo list and enter as many tasks as he wants. It can also delete the completed folder or replace it with other content.

#Modules and Functions used:
    *module imports*

    tabulate - to display menu and Todo list in a table format.

#functions:

#main():
#In the main function we have an empty list where user will add tasks later. Also in the main function we have a menu with 5 options:
Add Task: Calls add_task(task_list) to add a new task.
View Tasks: Calls view_tasks(task_list) to display the current list of tasks.
Remove Task: Calls remove_task(task_list) to remove a task based on user input.
Edit Task: Calls edit_task(task_list) to update the description of an existing task.
Exit: Ends the loop, prints an exit message, and terminates the application. The program will return the result according to the choice entered by the user. If the user enters an incorrect number, the program will write that it is a wrong number and ask the user to choose a number from the numbers in the menu. The function continuously loops until the user chooses to exit.

#view_tasks(task_list):
#The view_tasks() function displays the list of current tasks in a tabulated format. It provides users with an overview of their tasks, including their indices. If there is no any task in this list, the program will print that there is no tasks.

#add_task(task_list):
#In this function users can add tasks as much as they want. If the user has added all the desired tasks, he can press enter and return to the menu.

#remove_task(task_list):
#If the user has already done any of these tasks, he can select Remove task from the manu and the task will be removed. If the user enters a string instead of an integer, the program asks to enter the task number. And if the user enters a number that we do not have in the list, the program will return that it is a wrong number and show us the amount of the task.

#edit_task(task_list):
#If the user wants to change the content of task, he can select Edit task in the menu, then choose the task number which content he wants to change and change it with new description. If the user enters a number that is not in the list, the program asks to enter the correct number.

#finally, when the user is done with his work, he can select Exit from menu and the program will finish working.

#Error Handling
Each function includes basic error handling to manage incorrect inputs and ensure a smooth user experience:
Invalid Choices: Prompts users to enter valid menu options if their input does not match any listed option.
Non-numeric Inputs: Provides feedback when a numeric input is expected but not provided.
Out-of-range Values: Alerts users if they attempt to remove or edit a task number that does not exist in the current list.
