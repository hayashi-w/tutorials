# フォームデータ
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
# フォームフィールドとして送られる必要がある
# Formのパラメータの定義
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
