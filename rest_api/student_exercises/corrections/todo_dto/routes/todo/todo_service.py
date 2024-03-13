from datetime import datetime, timezone
import uuid
import json

from .todo_exceptions import TodoNotFound, TodoEmpty

def jsonify(task):
  if isinstance(task, uuid.UUID):
    return str(task)
  if isinstance(task, datetime):
    return task.isoformat()
  return task

class TodoService():
  def __init__(self):
    self.json_file = "tasks.json"
    self.tasks = [
      {
        "id": uuid.UUID("35c034ed-8ef0-41db-b87e-5c61c21837e2"),
        "task": "Learn Rest API",
        "completed": False,
        "created": datetime.now(timezone.utc)
      }
    ]

  def write_file(self):
    with open(self.json_file, "w") as f:
      json.dump(self.tasks, f, default=jsonify)

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
    self.write_file()
    return new_task
  
  def get_one(self, task_id):
    for task in self.tasks:
      if task["id"] == task_id:
        return task
    raise TodoNotFound(f"Task with is {task_id} not found")
  
  def update_one(self, updated_task, task_id):
    if updated_task == {}:
      raise TodoEmpty("Please specify at least a key ['task', 'completed']")
    
    for task in self.tasks:
      if task["id"] == task_id:
        task.update(updated_task)
        self.write_file()
        return task
    raise TodoNotFound(f"Task with id {task_id} not found")
  
  def delete_one(self, task_id):
    for task in self.tasks:
      if task["id"] == task_id:
        self.tasks.remove(task)
        self.write_file()
        return {}
    raise TodoNotFound(f"Task with id {task_id} not found") 