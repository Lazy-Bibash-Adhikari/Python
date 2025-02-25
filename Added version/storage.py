import json
from task import Task 

def saveTasks(tasks, filename="tasks.json"):
    tasksData = []
    for task in tasks:
        tasksData.append({
            "id": task.id,
            "title": task.title,
            "completed":  task.completed
        })
    
    with open(filename, "w") as file:
        json.dump(tasksData, file)
        print(f"Tasks saved to {filename}.")
    
def loadTasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasksData = json.load(file)
        tasks = []
        for taskData in tasksData:
            task = Task(taskData['id'], taskData['title'], taskData["completed"])
            tasks.append(task)
        print(f"Tasks Loaded from {filename}.")
        return tasks
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
        return []
    