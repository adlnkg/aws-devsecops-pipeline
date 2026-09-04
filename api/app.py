from fastapi import FastAPI
import socket
import datetime

app = FastAPI(title="Cloud API")

@app.get("/")
def root():
    return {
        "message": "Service OP",
        "timestamp":datetime.datetime.utcnow().isoformat(),
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}