# クエリパラメータのリスト / 複数の値
from typing import List, Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items


# http://localhost:8000/items/?q=foo&q=bar
