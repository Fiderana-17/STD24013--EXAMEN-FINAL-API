from fastapi import FastAPI

app = FastAPI()

# Q1 : GET /hello
@app.get("/hello")
def hello():
    return {"message": "Hello world"}

# Q2 : GET /welcome?name=xxx
@app.get("/welcome")
def welcome(name: str):
    return {"message": f"Welcome {name}"}
