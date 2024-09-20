from datetime import datetime, timezone
import enum
from flask import abort
from flask_smorest import Blueprint
from flask.views import MethodView
import json
from marshmallow import Schema, fields
import uuid

from .dto.response.task_response import TaskResponse
from .dto.response.list_task_response import ListTaskResponse
from .dto.request.create_task import CreateTask

JSON_FILE = "todo.json"
todo_list = None

todo = Blueprint("todo", "todo", url_prefix="/todo", description="Todo operations")

with open(JSON_FILE, "r") as f:
  todo_list = json.load(f)


todo_list = [
  {
    "id": uuid.UUID("71844c4c-0cdb-4d55-afa8-a97744a6f4c0"),
    "created": datetime.now(timezone.utc),
    "completed": False,
    "task": "Create Flask API tutorial"
  }
]
print(todo_list)

class SortByEnum(enum.Enum):
  task = "task"
  completed = "completed"
  created = "created"

class SortDirectionEnum(enum.Enum):
  asc = "asc"
  desc = "desc"
class ListTasksParameters(Schema):
  order_by = fields.Enum(SortByEnum, load_default=SortByEnum.created)
  order = fields.Enum(SortDirectionEnum, load_default=SortDirectionEnum.asc) 

def jsonify(task):
  if isinstance(task, uuid.UUID):
    return str(task)
  if isinstance(task, datetime):
    return task.isoformat()
  return task

@todo.route("/tasks")
class TodoCollection(MethodView):
  @todo.arguments(ListTasksParameters, location="query")
  @todo.response(status_code=200, schema=TaskResponse(many=True))
  def get(self, parameters):
    print(parameters)
    todo_list.sort(key=lambda t: t[parameters["order_by"].value], reverse=parameters["order"].value == "desc")
    return todo_list
    # return {
    #   "tasks": todo_list
    # }
  
  @todo.arguments(CreateTask)
  @todo.response(status_code=201, schema=TaskResponse)
  def post(self, task):
    task["id"] = uuid.uuid4()
    task["completed"] = False
    task["created"] = datetime.now(timezone.utc)
    todo_list.append(task)
    with open(JSON_FILE, "w") as f:
      json.dump(todo_list, f, default=jsonify)
    return task
    

@todo.route("/tasks/<uuid:task_id>")
class TodoItem(MethodView):
  @todo.response(status_code=200, schema=TaskResponse)
  def get(self, task_id):
    for t in todo_list:
      if t["id"] == task_id:
        return t
      
    # abort(404, "Task not found")
    return "Task not found", 404
  
  @todo.response(status_code=204)
  def delete(self, task_id):
    for t in todo_list:
      if t["id"] == task_id:
        todo_list.remove(t)
        with open(JSON_FILE, "w") as f:
          json.dump(todo_list, f, default=jsonify)
        return
    return "Task not found", 404
  
  @todo.arguments(TaskResponse)
  @todo.response(status_code=200, schema=TaskResponse)
  def patch(self, task, task_id):
    for t in todo_list:
      if t["id"] == task_id:
        t.update(task)
        with open(JSON_FILE, "w") as f:
          json.dump(todo_list, f, default=jsonify)
        return t
    return "Task not found", 404