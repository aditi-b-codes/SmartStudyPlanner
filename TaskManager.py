from store import load_task, save_tasks
def add_tasks(tasks):
    task_name=input("Enter the task-:").strip()
    if task_name=="":
        print("Task cannot be empty")
        return
    deadline=input("Enter deadline (YYYY-MM-DD): ").strip()
    if deadline=="":
        deadline="No deadline"
    tasks.append({"task": task_name, "Done": False, "deadline": deadline})
    save_tasks(tasks)
    print("Task added successfully\n")
def disp_tasks(tasks):
    if len(tasks)==0:
        print("No tasks available\n")
        return
    print("\nYour Tasks:")
    for i,t in enumerate(tasks,1):
        status="Done" if t["Done"] else "Not Done"
        print(f"{i}. {t['task']} | Status:{status} | Deadline: {t['deadline']}")
    print()
def mark_completed(tasks):
    if len(tasks)==0:
        print("No tasks to complete\n")
        return
    disp_tasks(tasks)
    num_str=input("Enter the task number to mark completed-:").strip()
    try:
        num= int(num_str)
        if num <1 or num>len(tasks):
            print("Invalid task number \n")
            return
    except ValueError:
        print("Invalid input\n")
        return
    tasks[num-1]["Done"]=True
    save_tasks(tasks)
    print("Task marked as completed!\n")

def del_task(tasks):
    if len(tasks)==0:
        print("No task to delete \n")
        return
    disp_tasks(tasks)
    num_str=input("Enter the task number to delete-:").strip()
    try:
        num=int(num_str)
        if num<1 or num>len(tasks):
            print("Invalid task number\n")
    except ValueError:
        print("Invalid input \n")
        return
    tasks.pop(num-1)
    save_tasks(tasks)
    print("Task deleted\n")
