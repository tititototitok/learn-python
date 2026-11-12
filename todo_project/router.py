from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from .schema import Todo, SubTodo
from .storage import load_todos, save_todos

router = APIRouter(prefix="/todos", tags=["待办"])

limiter = Limiter(key_func=get_remote_address)


def get_next_id(todos: list) -> int:
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1


def find_todo(todos: list, todo_id: int):
    for t in todos:
        if t["id"] == todo_id:
            return t
    return None


def register_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exc_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"code": exc.status_code, "message": exc.detail},
        )

    @app.exception_handler(Exception)
    async def unhandled_exc_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"code": 500, "message": "服务器内部错误"},
        )


@router.get("")
@limiter.limit("60/minute")
def list_todos(
    request: Request,
    skip: int = Query(0, ge=0, description="跳过前几条"),
    limit: int = Query(10, ge=1, le=100, description="返回几条"),
    completed: bool | None = Query(None, description="按完成状态过滤"),
):
    todos = load_todos()
    if completed is not None:
        todos = [t for t in todos if t["completed"] is completed]
    total = len(todos)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": todos[skip : skip + limit],
    }


@router.get("/{todo_id}")
def get_todo(todo_id: int):
    todos = load_todos()
    todo = find_todo(todos, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="待办不存在")
    return todo


@router.post("", status_code=201)
def create_todo(todo: Todo):
    todos = load_todos()
    new_todo = todo.model_dump()
    new_todo["id"] = get_next_id(todos)
    new_todo["completed"] = False
    todos.append(new_todo)
    save_todos(todos)
    return new_todo


@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    todos = load_todos()
    target = find_todo(todos, todo_id)
    if not target:
        raise HTTPException(status_code=404, detail="待办不存在")
    data = todo.model_dump()
    data["id"] = todo_id
    idx = todos.index(target)
    todos[idx] = data
    save_todos(todos)
    return data


@router.patch("/{todo_id}")
def patch_todo(todo_id: int, updates: dict):
    todos = load_todos()
    target = find_todo(todos, todo_id)
    if not target:
        raise HTTPException(status_code=404, detail="待办不存在")
    allowed = {"content", "completed"}
    for key, value in updates.items():
        if key in allowed:
            target[key] = value
    save_todos(todos)
    return target


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    todos = load_todos()
    target = find_todo(todos, todo_id)
    if not target:
        raise HTTPException(status_code=404, detail="待办不存在")
    todos.remove(target)
    save_todos(todos)
    return {"message": "已删除"}