# project/app/main.py
import os, logging
from fastapi import FastAPI, Depends
from app.config import Settings, get_settings
from app.api import ping, summaries
from app.db import init_db

from tortoise.contrib.fastapi import register_tortoise


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("starting up")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("shutting down")
