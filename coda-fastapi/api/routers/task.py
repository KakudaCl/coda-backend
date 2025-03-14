from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.task as task_crud
import api.schemas.task as task_schema
from api.db import get_db

router = APIRouter()


@router.get(
    "/tasks",
    response_model=list[task_schema.Task],
    tags=["FastAPI学習"]
)
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のToDoタスク")]


@router.post(
    "/tasks",
    response_model=task_schema.TaskCreateResponse,
    tags=["FastAPI学習"]
)
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", tags=["FastAPI学習"])
async def update_task():
    pass


@router.delete("/tasks/{task_id}", tags=["FastAPI学習"])
async def delete_task():
    pass
