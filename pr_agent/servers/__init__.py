import os

import uvicorn
from fastapi import FastAPI

from pr_agent.config_loader import get_settings


def run(app: FastAPI) -> None:
    app_host: str = get_settings().get("config.host", "0.0.0.0")
    app_port: int = int(get_settings().get("config.port", "3000"))

    if os.environ.get("PORT") is not None:
        app_port = int(os.environ.get("PORT"))

    uvicorn.run(app, host=app_host, port=app_port)