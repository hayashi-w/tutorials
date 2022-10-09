# Bodies of arbitrary dicts
from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

# {
#   "1": "2.3",
#   "2": "3"
# }