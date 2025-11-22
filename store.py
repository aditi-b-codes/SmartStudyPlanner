def load_task(filename="tasks.txt"):
    tasks=[]
    try:
        with open(filename, "r") as fn:
            for line in fn:
                line=line.strip()
                if line=="":
                    continue
                segments=line.split("|")
                task_name=segments[0]
                done=segments[1]=="True"
                deadline=segments[2]
                tasks.append({"task":task_name, "Done":done, "deadline":deadline})
    except FileNotFoundError:
            pass
    return tasks
def save_tasks(tasks,filename="tasks.txt"):
    with open(filename, "w") as fn:
        for t in tasks:
            line=t["task"] + "|" + str(t["Done"]) + "|" + t["deadline"] + "\n"
            fn.write(line)
def disp_study_hours(filename="study_hours.txt"):
    hours={}
    try:
        with open(filename, "r") as fn:
            for line in fn:
                line=line.strip()
                if line=="":
                    continue
                date,h=line.split("|")
                hours[date]=float(h)

    except FileNotFoundError:
            pass
    return hours
def save_studyhours(hours, filename="study_hours.txt"):
    with open(filename,"w")as fn:
        for date,h in hours.items():
            fn.write(f"{date}|{h}\n")
