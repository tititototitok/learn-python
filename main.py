import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATA_FILE = "todos.json"

def load_todos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f) # model_dump() 是 Python→字典，json.load() 是文件JSON→Python
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

class Todo(BaseModel):
    title: str
    done: bool = False # 这一行只是单纯的在收集信息，完成/未完成，并不是什么代码层面的内容

@app.get("/todos")
def get_todos():
    return {"todos": load_todos()}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):   # 路径参数比如/todos/3 → todo_id=3
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    return todos[todo_id - 1]  #  用户看到的 id 从 1 开始，但 Python 列表下标从 0 开始。id=1 对应 todos[0]，所以要减 1

@app.post("/todos")
def create_todo(todo: Todo):
    todos = load_todos()
    todo_dict = todo.model_dump()
    todo_dict["id"] = len(todos) + 1
    todos.append(todo_dict)
    save_todos(todos)
    return {"message": "创建成功", "todo": todo_dict}

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