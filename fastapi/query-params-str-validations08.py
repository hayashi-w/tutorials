# デフォルト値を持つ、クエリパラメータのリスト / 複数の値
from typing import List

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# http://localhost:8000/items/
