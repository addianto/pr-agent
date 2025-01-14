import os

import uvicorn
from fastapi import FastAPI

from pr_agent.config_loader import get_settings

DEFAULT_HOST: str = "0.0.0.0"
DEFAULT_PORT: int = 3000

def run(app: FastAPI) -> None:
    """Start the Qodo Merge (PR Agent) server."""
    host_address: str = get_settings().get("config.host", DEFAULT_HOST)
    port_number: int = int(get_settings().get("config.port", DEFAULT_PORT))

    if os.environ.get("PORT") is not None:
        port_number = int(os.environ.get("PORT"))

    uvicorn.run(app, host=host_address, port=port_number)