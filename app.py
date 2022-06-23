from modules.output import *
from modules.task_list import *

from modules.input import *

from_user = input("Do you want to load some tasks that are already loaded? Answer Y/y\n")
if ( from_user.lower() == 'y'):
    from data.task_list import *


while (True):
    print_menu()
    options = option()
    if (options.lower() == 'q'):
        break
    if options == '1':
        print_list(tasks)
    elif options == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif options == '3':
        print_list(get_completed_tasks(tasks))
    elif options == '4':
        descriptions = description()
        task = get_task_with_description(tasks, descriptions)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif options == '5':
        times = time()
        print_list(get_tasks_taking_at_least(tasks, times))
    elif options == '6':
        descriptions = description()
        print(get_task_with_description(tasks, descriptions))
    elif options == '7':
        descriptions = input("Enter description: ")
        times = int(input("Enter time taken: "))
        task = create_task(descriptions, times)
        tasks.append(task)
    elif options.lower() == 'm':
        print_menu()
    else:
        print("Invalid Input - choose another option")
