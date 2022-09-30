# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    text: str


app = FastAPI()


@app.post("/log/stdout")
async def log_stdout(message: Message):
    now = datetime.now()
    sys.stdout.write(f"{now} - {message.text}\n")
    sys.stdout.flush()
    return 200


@app.post("/log/stderr")
async def log_stderr(message: Message):
    now = datetime.now()
    sys.stderr.write(f"{now} - {message.text}\n")
    sys.stderr.flush()
    return 200


@app.post("/log/file")
async def log_file(message: Message):
    now = datetime.now()
    with open("log.txt", 'a') as f:
        f.write(f"{now} - {message.text}\n")
        f.flush()
    return 200


@app.get("/environment")
async def environment():
    return dict(os.environ)
