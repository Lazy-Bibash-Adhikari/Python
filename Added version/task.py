class Task:
    def __init__(self, taskId, title, completed=False):
        self.id = taskId
        self.title = title
        self.completed = completed

    
    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id}, Title: {self.title}, Status: {status}"
    

    def markComplete(self):
        self.completed = True
