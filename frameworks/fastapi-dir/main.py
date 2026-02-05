from fastapi import FastAPI
from datetime import datetime
from .models import User
import random
import uvicorn


app = FastAPI(name="Fastapi App")

app.get("/health")
def get_health():
    return {"status":"ok"}

app.get("/users")
def get_users():
    users = ["Julien", "Chris","Mike"]
    return {"users": users}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)