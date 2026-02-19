from fastapi import FastAPI
from models import Review, MovieReview

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/health")
def check_health():
    return {"status": "FastAPI is live!"}

@app.get("/hello")
def hello(name: str = "Allan"):
    return {"message": f"Hello {name}"}

@app.get("/users")
def get_users():
    users = {"name": "Julien", "id": 1}
    id = users["id"]
    name = users["name"]
    
    return {"user_name": name, "user_id": id}

