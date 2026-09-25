# load existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items

import json

file_name = "todo_list.json"


def load_tasks():
    try:
      with open(file_name, "r") as file:
        return json.load(file)
    except:
        return{"tasks": []}

def save_tasks(tasks):
    try:
       with open(file_name, "w") as file:
             json.dump(tasks,file)
    except:
        print("failed to save.")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To_do list: ")
        for idx, task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
          tasks["tasks"][task_number - 1]["complete"] = True
          save_tasks(tasks)
          print("Task marked as complete.")
        else:
           print("Invalid task number.")
    except:
        print("Enter a valid number.")



def main():
       tasks = load_tasks()


while True:
        print("\nTo-Do list manager")
        print("1.view Tasks")
        print("2. Add Task")
        print("3. complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
             view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
           mark_task_complete()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. please try again.")


main()
