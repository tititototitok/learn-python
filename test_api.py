import requests

base = "http://127.0.0.1:8000"

print("获取全部待办：")
print(requests.get(f"{base}/todos").json())

print("\n筛选已完成：")
print(requests.get(f"{base}/todos", params={"done": "true"}).json())