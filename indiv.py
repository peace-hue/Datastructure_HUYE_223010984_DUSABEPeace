from collections import deque
class TaskScheduler:
    def __init__(self):
        self.undo_stack = [] 
        self.redo_stack = [] 
        self.pending_queue = deque() 
        self.completed_list = []

    def add_task(self, task):
        self.pending_queue.append(task)
        print(f"Task '{task}' added to pending tasks.")

    def complete_task(self):
        if self.pending_queue:
            task = self.pending_queue.popleft()
            self.completed_list.append(task)
            self.undo_stack.append(task)
            print(f"Task '{task}' completed.")
        else:
            print("No pending tasks to complete.")

    def undo(self):
        if self.undo_stack:
            task = self.undo_stack.pop()
            self.redo_stack.append(task)
            self.completed_list.remove(task)
            self.pending_queue.appendleft(task)
            print(f"Undo: Task '{task}' moved back to pending tasks.")
        else:
            print("No actions to undo.")

    def redo(self):
        if self.redo_stack:
            task = self.redo_stack.pop()
            self.pending_queue.appendleft(task)
            self.completed_list.append(task)
            self.undo_stack.append(task)
            print(f"Redo: Task '{task}' completed again.")
        else:
            print("No actions to redo.")

    def show_status(self):
        print(f"Pending tasks: {list(self.pending_queue)}")
        print(f"Completed tasks: {self.completed_list}")
        print(f"Undo stack: {self.undo_stack}")
        print(f"Redo stack: {self.redo_stack}")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Arranging files")
scheduler.add_task("Removing duplicates")
scheduler.complete_task()
scheduler.complete_task()
scheduler.undo()
scheduler.redo()
scheduler.show_status()




