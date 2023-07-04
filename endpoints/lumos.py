from fastapi import APIRouter
from schemas.server import ServerRequest
from utils.commands import commands
from utils.lantern import Lantern

router = APIRouter()

@router.post("/update/")
async def update(*, data: ServerRequest):
    commands[data.command](data.metadata)

@router.get("/status/")
async def status():
    return {
            "status" : "Включен" if Lantern.status else "Выключен",
            "color": Lantern.color.name
            }
