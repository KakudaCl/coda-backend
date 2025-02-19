from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routers import done, pdf_edit, task, user_account

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

app.include_router(task.router)
app.include_router(done.router)
app.include_router(pdf_edit.router)
app.include_router(user_account.router)


@app.get("/hello", tags=["FastAPI学習"])
async def hello():
    return {"message": "hello world!"}
