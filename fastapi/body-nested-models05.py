# サブモデルのリストを持つ属性
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    # Image のリスト
    images: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": [
#         "rock",
#         "metal",
#         "bar"
#     ],
#     "images": [
#         {
#             "url": "http://example.com/baz.jpg",
#             "name": "The Foo live"
#         },
#         {
#             "url": "http://example.com/dave.jpg",
#             "name": "The Baz"
#         }
#     ]
# }