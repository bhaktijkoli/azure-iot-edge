import os
import pathlib
import uvicorn
from src.main import app

if __name__ == "__main__":
    ssl_certfile = (
        pathlib.Path(__file__).parent.joinpath(
            "certs", "CA.crt").resolve()
    )
    ssl_keyfile = (
        pathlib.Path(__file__).parent.joinpath(
            "certs", "private.key").resolve()
    )
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
        ssl_certfile=ssl_certfile,
        ssl_keyfile=ssl_keyfile,
    )
