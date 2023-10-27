from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World1", 'hobbies': ['sdfsdf', 'erthrty']}


items = [
    'item 0',
    'item 1',
    'item 2',
    'item 3'
]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
