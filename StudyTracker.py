from store import disp_study_hours, save_studyhours
def add_studyhours():
    hours=disp_study_hours()
    date=input("Enter date (YYYY-MM-DD):").strip()
    try:
        h=float(input("Enter study hours:").strip())

    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return
    hours[date]=h
    save_studyhours(hours)
    print("Study hours recorded\n")
def summary():
    hours=disp_study_hours()
    if not hours:
        print("No study data available\n")
        return
    print("\nStudy Summary:")
    total=0
    for date,h in hours.items():
        print(f"{date}:{h} hours")
        total+=h

    print(f"\nTotal Hours: {total}\n")

def del_study_hours():
    hours=disp_study_hours()
    if not hours:
        print("No study hours to delete\n")
        return
    print("\nYour Study Hours:")
    for i,(date,h) in enumerate(hours.items(),1):
        print(f"{i}.{date}:{h}hours")
    num_str=input("Enter the numer to delete:").strip()
    try:
        num=int(num_str)
        if num<1 or num>len(hours):
            print("Invalid number\n")
            return
    except ValueError:
        print("Invalid input\n")
        return
    key_to_del=list(hours.keys())[num-1]
    hours.pop(key_to_del)
    save_studyhours(hours)
    print("Study hours entry deleted\n")
    
