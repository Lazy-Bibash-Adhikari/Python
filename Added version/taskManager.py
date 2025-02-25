from task import Task 
from storage import saveTasks, loadTasks
from utils import getIntInput, getYesNoInput

tasks = loadTasks()
nextTaskId = max(task.id for task in tasks) + 1 if tasks else 1

def displayMenu():
    print("\nTask Manager Menu:")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Complete")
    print("4. Delete a Task")
    print("5. Save Tasks")
    print("6. Exit")

def addTask():
    global nextTaskId
    title = input("Enter the task title: ")
    task = Task(nextTaskId, title)
    tasks.append(task)
    nextTaskId += 1
    print(f"Task '{title}' added successfully!")

def viewTasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for task in tasks:
            print(task)

def markTaskComplete():
    taskId = getIntInput("Enter the task ID to mark as complete: ")
    for task in tasks:
        if task.id == taskId:
            task.markComplete()
            print(f"Task '{task.title}' marked as complete!")
            return
    print("Task not found.")

def deleteTask():
    taskId = getIntInput("Enter the task ID to delete: ")
    for task in tasks:
        if task.id == taskId:
            tasks.remove(task)
            print(f"Task '{task.title}' deleted successfully!")
            return
    print("Task not found.")

def saveTasksPrompt():
    if getYesNoInput("Do you want to save tasks? (y/n): "):
        saveTasks(tasks)

def main():
    while True:
        displayMenu()
        choice = getIntInput("Enter your choice (1-6): ")

        if choice == 1:
            addTask()
        elif choice == 2:
            viewTasks()
        elif choice == 3:
            markTaskComplete()
        elif choice == 4:
            deleteTask()
        elif choice == 5:
            saveTasks(tasks)
        elif choice == 6:
            saveTasksPrompt()
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()