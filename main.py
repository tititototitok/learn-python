from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}
# 如果你写 @app.get("/hello")，那访问的就是 http://127.0.0.1:8000/hello
# pip就是以pip开头在终端输代码，后面接要下载的东西名字，下载别人做好的代码直接用，相当于一个应用商店
# venv就是创建虚拟环境，区分pip使用的版本，只是创建新文件夹并不能区分