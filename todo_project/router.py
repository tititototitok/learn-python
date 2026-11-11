from fastapi import APIRouter, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .schema import Todo
from .storage import load_todos, save_todos

router = APIRouter(prefix="/todos", tags=["待办"])

# --- Day21: 统一异常处理 ---
def register_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exc_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"code": exc.status_code, "message": exc.detail}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exc_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"code": 422, "message": "参数校验失败", "errors": exc.errors()}
        )

# --- 路由（逻辑和你旧版一致，路径去掉 /todos 前缀）---
@router.get("")
def get_todos():
    return load_todos()

@router.get("/{todo_id}")
def get_todo(todo_id: int):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    return todos[todo_id - 1]

@router.post("")
def create_todo(todo: Todo):
    todos = load_todos()
    todo_dict = todo.model_dump()
    todo_dict["id"] = len(todos) + 1
    todos.append(todo_dict)
    save_todos(todos)
    return {"message": "创建成功", "todo": todo_dict}

@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    todo_dict = todo.model_dump()
    todo_dict["id"] = todo_id
    todos[todo_id - 1] = todo_dict
    save_todos(todos)
    return {"message": "修改成功", "todo": todo_dict}

@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    todos = load_todos()
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="待办不存在")
    deleted = todos.pop(todo_id - 1)
    for i, t in enumerate(todos):
        t["id"] = i + 1
    save_todos(todos)
    return {"message": "删除成功", "deleted": deleted}