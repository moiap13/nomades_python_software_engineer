from flask import abort, request
from flask.views import MethodView
from flask_smorest import Blueprint
import uuid
from datetime import datetime, timezone

from .dto.response.task_response import TaskResponse
from .dto.response.list_task_response import ListTaskResponse
from .dto.request.create_task import CreateTask
from .dto.request.update_task import UpdateTask

from .todo_service import TodoService
from .todo_exceptions import TodoNotFound, TodoEmpty

todos = Blueprint("todo", "todo", url_prefix="/todos", description="TODO API")

todo_service = TodoService()

@todos.route("/tasks") # /todos/tasks
class TasksCollection(MethodView):
  # @todos.response(status_code=200, schema=TaskResponse(many=True))
  @todos.response(status_code=200, schema=ListTaskResponse)
  def get(self):
    return {
      "tasks": todo_service.get_all()
    }

  @todos.arguments(CreateTask)
  @todos.response(status_code=201, schema=TaskResponse)
  def post(self, task):
    return todo_service.create_new_task(task)
  
@todos.route("/tasks/<uuid:task_id>") # /todos/tasks/{uuid:id}
class TaskItem(MethodView):
  @todos.response(status_code=200, schema=TaskResponse)
  @todos.response(status_code=404)
  def get(self, task_id):
    try:
      return todo_service.get_one(task_id)
    except TodoNotFound as e:
      return {"error": str(e)}, 404 
  
  @todos.arguments(UpdateTask)
  @todos.response(status_code=200, schema=TaskResponse)
  @todos.response(status_code=404)
  @todos.response(status_code=422)
  def put(self, updated_task, task_id):
    try:
      return todo_service.update_one(updated_task, task_id)
    except TodoNotFound as e:
      return {"error": str(e)}, 404
    except TodoEmpty as e:
      return {"error": str(e)}, 422


  @todos.response(status_code=204)
  @todos.response(status_code=404)
  def delete(self, task_id):
    try:
      return todo_service.delete_one(task_id), 204
    except TodoNotFound as e:
      return {"error": str(e)}, 404