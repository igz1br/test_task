#TODO: add server
from fastapi import FastAPI
from endpoints.lumos import router as lumos_router

app_test = FastAPI() 

app_test.include_router(lumos_router)