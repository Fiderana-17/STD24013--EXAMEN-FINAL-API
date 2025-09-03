from fastapi import FastAPI


app = FastAPI()

# a. GET /health
@app.get("/health")
def health():
    return "Ok"