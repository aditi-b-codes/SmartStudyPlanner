from store import load_task
from TaskManager import add_tasks, disp_tasks, mark_completed, del_task
from StudyTracker import add_studyhours, summary, del_study_hours
def main():
    tasks=load_task()
    while True:
        print("\n===SMART STUDY PLANNER===\n")
        print("1.Add Tasks")
        print("2.View Tasks")
        print("3.Mark Task as Completed")
        print("4.Delete Task")
        print("5.Add Study Hours")
        print("6.View Study Summary")
        print("7.Delete Study Hours")
        print("8.Exit")
        choice=input("Enter your choice-:").strip()
        if choice=="1":
            add_tasks(tasks)
        elif choice=="2":
            disp_tasks(tasks)
        elif choice=="3":
            mark_completed(tasks)
        elif choice=="4":
            del_task(tasks)
        elif choice=="5":
            add_studyhours()
        elif choice=="6":
            summary()
        elif choice=="7":
            del_study_hours()
        elif choice=="8":
            print("Exiting program..")
            break
        else:
            print("Invalid choice. Please enter 1-8 \n")
if __name__=="__main__":
    main()
