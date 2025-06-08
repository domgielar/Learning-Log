
tasks = {}

def main():
    while True:
        try:
            whatToDo = input("What would you like to do add/view/remove/end tasks: ").lower().strip()
            if whatToDo == "add":
                add()
            elif whatToDo == "view":
                view()
            elif whatToDo == "remove":
                remove()
            elif whatToDo == "end":
                print("Goodbye! ")
                break
            else:
                raise ValueError("Invalid option selected.")
        except ValueError as e:
            print(f"Error: {e}")

def add():
    nameOfTask = input("Enter the name you want for the task: ")
    descOfTask = input("Enter the description of the task: ")
    dueDate = input("Enter the amount of time you want alotted for the task: ")

    tasks[nameOfTask] = {
        "Description" : descOfTask,
        "Time Allotted" : dueDate
    }

def view():
    print(tasks)

def remove():
    desiredTask = input("which task would you like to remove? ")
    if desiredTask in tasks:
        del tasks[desiredTask]
        print(f'Tasks {desiredTask} removied.')
    else:
        print("task not found")

if __name__ == "__main__":
    main()
    
