tasks = []

def add_task(task: dict):
    tasks.append(task)


def del_task(name):
    for i in range(len(tasks)):
        if tasks[i].get("task_name") == name:
            tasks.pop(i)
            return False
    return True


def check_task(task_name):
    for i in tasks:
        if i.get("task_name") == task_name:
            return False
    return True


running = True
while running:
    menu = """
    (--TODO--):
    1. Add task
    2. Display tasks
    3. Delete task
    4. Exit
    >>> """
    key = input(menu)
    if not key.isdigit() or not 1 <= int(key) <= 4:
        print("Key invalid !!!")
        continue

    match key:
        case "1":
            task = {
                "task_name": input("Task name: "),
                "added_time": input("Time: "),
                "task_content": input("Content: ")
            }
            isvalid = check_task(task.get("task_name"))
            if isvalid:
                add_task(task)
            else:
                print("Task already exists!")
                continue
        case "2":
            print(tasks)
        case "3":
            name = input("Name of task for deletion: ")
            del_task(name)
            if del_task(name):
                print(f"{name} succesfully deleted!")
            else:
                print(f"There is no task called {name}!")
        case "4":
            break