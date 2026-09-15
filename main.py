from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}
# 如果你写 @app.get("/hello")，那访问的就是 http://127.0.0.1:8000/hello
# pip就是以pip开头在终端输代码，后面接要下载的东西名字，下载别人做好的代码直接用，相当于一个应用商店
# venv就是创建虚拟环境，在这个venv里面创建一个虚拟环境，你需要用这种环境的时候，就激活一下拿来用

@app.get("/hello/{name}")
def hello_name(name: str):
    return{"message": f"Hello {name}"}


fake_db = [] # 全局假库


@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": fake_db[skip : skip+limit]}
# uvicorn main:app --reload的含义是用 uvicorn 启动 main.py 里的 app 实例，代码改了自动重启

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False



@app.post("/items")
def creat_item(item:Item):
    item_dict = item.model_dump()
    item_dict["id"] = len(fake_db) + 1
    fake_db.append(item_dict)
    return {"message": "创建成功", "item": item_dict}


