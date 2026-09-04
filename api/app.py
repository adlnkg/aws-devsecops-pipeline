import datetime
import socket
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Cloud API")

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "message": "Service OP",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "hostname": socket.gethostname(),
    }


@app.get("/health")
def health():
    return {"status": "healthy"}