from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()  

    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task '{task}' added to the queue.")

    def process_next_task(self):
        if not self.task_queue:
            print("No tasks in the queue.")
            return

        task = self.task_queue.popleft()
        print(f"Processing task '{task}'...")
        print(f"Task '{task}' completed.")

scheduler = TaskScheduler()

scheduler.add_task("Send email")
scheduler.add_task("Generate report")
scheduler.add_task("Backup data")

scheduler.process_next_task()
scheduler.process_next_task()
scheduler.process_next_task()

scheduler.add_task("Update software")
scheduler.process_next_task()
