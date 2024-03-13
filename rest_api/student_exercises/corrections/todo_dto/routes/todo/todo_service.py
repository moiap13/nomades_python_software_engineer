from datetime import datetime, timezone
import uuid

class TodoService():
  def __init__(self):
    self.tasks = [
      {
        "id": uuid.UUID("35c034ed-8ef0-41db-b87e-5c61c21837e2"),
        "task": "Learn Rest API",
        "completed": False,
        "created": datetime.now(timezone.utc)
      }
    ]

  def get_all(self):
    return self.tasks
  
  def create_new_task(self, task):
    new_task = {
      "id": uuid.uuid4(),
      "created": datetime.now(timezone.utc),
      "completed": False
    }
    new_task.update(task)
    self.tasks.append(new_task)
    return new_task
  
  def get_one(self, task_id):
    for task in self.tasks:
      if task["id"] == task_id:
        return task
    raise Exception(f"Task with is {task_id} not found")