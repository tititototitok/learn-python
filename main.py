import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# JSON 文件持久化
DATA_FILE = "todos.json"

def load_todos():
    try