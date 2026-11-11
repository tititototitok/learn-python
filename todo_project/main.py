from fastapi import FastAPI
from .router import router, register_exception_handlers
from .storage import load_todos

app = FastAPI()

register_exception_handlers(app)
app.include_router(router)


@app.get("/todos/debug")
def debug():
    return {"count": len(load_todos()), "todos": load_todos()}
