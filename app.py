from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1: {"task":"Write Hello World Program", "Summary":"Write the code using Python"},
    2: {"task":"Task 2", "Summary":"Writing task 2"},
    3: {"task":"Task 3", "Summary":"this is task 3"}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task description is required", required=True)
task_post_args.add_argument("summary", type=str, help="Task summary is required", required=True)

class ToDoList(Resource):
  def get(self):
      return todos
  
class ToDo(Resource):
  def get(self, todo_id):
      return todos[todo_id]
  
  def post(self, todo_id):
      args = task_post_args.parse_args()
      if todo_id in todos:
         abort(409, "Task Id already taken")
      todos[todo_id] = {"task": args["task"], "summary": args["summary"]}
      return todos[todo_id], 201

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)