import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATA_FILE = "todos.json"

def load_todos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

class Todo(BaseModel):
    title: str
    done: bool = False

@app.get("/todos")
def get_todos(done: bool = None, limit: int = 10, offset: int = 0):
    todos = load_todos()
    if done is not None:
        todos = [t for t in todos if t["done"] == done]
    return {"todos": todos[offset : offset + limit]}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    return todos[todo_id - 1]

@app.post("/todos")
def create_todo(todo: Todo):
    todos = load_todos()
    todo_dict = todo.model_dump()
    todo_dict["id"] = len(todos) + 1
    todos.append(todo_dict)
    save_todos(todos)
    return {"message": "创建成功", "todo": todo_dict}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    todo_dict = todo.model_dump()
    todo_dict["id"] = todo_id
    todos[todo_id - 1] = todo_dict
    save_todos(todos)
    return {"message": "修改成功", "todo": todo_dict}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    deleted = todos.pop(todo_id - 1)
    for i, t in enumerate(todos):
        t["id"] = i + 1
    save_todos(todos)
    return {"message": "删除成功", "deleted": deleted}