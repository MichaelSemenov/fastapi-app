from fastapi import APIRouter, Depends
from schemas import STaskAdd
from repository import TaskRepository
from typing import Annotated
from schemas import STask, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=['Таски']
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": "True", "task_id": task_id}

@router.get("")
async def get_task() -> STask:
    result = await TaskRepository.find_all()
    return {"tasks_list": result}