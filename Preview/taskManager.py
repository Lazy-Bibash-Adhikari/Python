tasks = []
nextTaskId = 1

def displayMenu():
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Complete")
    print("4. Delete a Task")
    print("5. Exit")

def addTask():
    global nextTaskId
    title = input("Enter the task title: ")
    task = {
        "id": nextTaskId,
        "title": title,
        "completed": False
    }

    task.append(task)
    nextTaskId += 1
    print(f"Task '{title}' added successfully!")

def viewTask():

    if not tasks:
        print("no task found.")
    else:
        print("\nTasks:")
        for task in tasks:
            status = "Completed" if task['complete'] else "Not Completed"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def markTestComplete():

    taskId = int(input("Enter the task ID to mark as complete: "))
    for task in tasks:
        if task["id"] == taskId:
            task['completed'] = True
            print(f"Task '{task['title']}' marked as complete!")
            return 
    print("Task Not Found")

def deleteTask():
    taskId = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task["id"] == taskId:
            tasks.remove(task)
            print(f"Task '{task['title']}' deleted Successfully!")
            return
        
    print("Task not found")


def main():

    while True: 
        displayMenu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            addTask()
        elif choice == '2':
            viewTask()
        elif choice == '3':
            markTestComplete()
        elif choice == '4':
            deleteTask()
        elif choice == '5':
            print("Exiting the Task Manager.")
        else:
            print("Invalid choice. Please do try again.")


if __name__ == "__main__":
    main()