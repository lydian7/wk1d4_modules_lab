from modules.output import *
from modules.task_list import *
from modules.input import *

tasks = [
]

task_check =  input("Do you want to load existing tasks? (y/n) ")
if task_check.lower() == "y":
    from data.task_list import tasks



print_menu()
while (True):
    option = get_option()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = description() 
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = time()
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description = description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time = time_taken()
        task = create_task(description, time)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
