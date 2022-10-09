# 数値の検証: より大きいか等しい
# 数値の検証: より大きいか小さいか等しい
# 数値の検証: 浮動小数点数、より大きい値と小さい値
from fastapi import FastAPI, Path, Query

app = FastAPI()


# item_id は 1 と同じかそれ以上
@app.get("/items/{item_id}")
async def read_items(
    *,
    # item_id: int = Path(title="The ID of the item to get", ge=1),
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
