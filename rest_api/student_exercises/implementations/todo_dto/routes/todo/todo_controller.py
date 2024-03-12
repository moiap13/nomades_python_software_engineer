from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
import uuid
from datetime import datetime, timezone

from .dto.response.task_response import TaskResponse
from .dto.response.list_task_response import ListTaskResponse
from .dto.request.create_task import CreateTask

todos = Blueprint("todo", "todo", url_prefix="/todos", description="TODO API")

tasks = [
  {
    "id": uuid.UUID("35c034ed-8ef0-41db-b87e-5c61c21837e2"),
    "task": "Learn Rest API",
    "completed": False,
    "created": datetime.now(timezone.utc)
  }
]

@todos.route("/tasks")
class TasksCollection(MethodView):
  # @todos.response(status_code=200, schema=TaskResponse(many=True))
  @todos.response(status_code=200, schema=ListTaskResponse)
  def get(self):
    return {
      "tasks": tasks
    }

  @todos.arguments(CreateTask)
  @todos.response(status_code=201, schema=TaskResponse)
  def post(self, task):
    new_task = {
      "id": uuid.uuid4(),
      "created": datetime.now(timezone.utc),
      "completed": False
    }
    new_task.update(task)
    tasks.append(new_task)
    return new_task
  
@todos.route("/tasks/<uuid:task_id>")
class TaskItem(MethodView):
  @todos.response(status_code=200, schema=TaskResponse)
  def get(self, task_id):
    for task in tasks:
      if task["id"] == task_id:
        return task
      
    # abort(404, f"Task with id {task_id} not found")
    return {"error": f"Task with id {task_id} not found"}, 404
  
  def put(self):
    # TODO: create put function to modify a task given the id
    # PUT should receive an update task as input
    # PUT should return the new updated task (think about response :))
    pass

  def delete(self):
    # TODO: create put function to delete a task given the id
    # delte should only return a status_code 204
    pass