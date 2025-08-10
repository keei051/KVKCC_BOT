# app/main.py
from fastapi import FastAPI

app = FastAPI(title="VK.cc Shortener — minimal API")

@app.get("/ping")
def ping():
    return {"ok": True}

# Подсказка:
# На Railway мы запустим так:
# uvicorn app.main:app --host 0.0.0.0 --port $PORT
