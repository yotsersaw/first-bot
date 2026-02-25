import subprocess
import os
import threading
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import asyncio
import websockets

app = FastAPI()

def start_shadowsocks():
    password = os.environ.get("SS_PASSWORD", "warpgram123")
    subprocess.Popen([
        "ss-server",
        "-s", "0.0.0.0",
        "-p", "8388",
        "-k", password,
        "-m", "aes-256-gcm"
    ])

@app.on_event("startup")
async def startup():
    threading.Thread(target=start_shadowsocks, daemon=True).start()

@app.get("/")
async def root():
    return {"status": "working"}
