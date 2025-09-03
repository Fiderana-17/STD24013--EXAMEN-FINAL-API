from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []

# a. GET /health
@app.get("/health")
def health():
    return "Ok"

# b. POST /phones
@app.post("/phones", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone

# c. GET /phones
@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db

# d. GET /phones/{id}
@app.get("/phones/{id}", response_model=Phone)
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with id '{id}' not found")

# e. BONUS : PUT /phones/{id}/characteristics
@app.put("/phones/{id}/characteristics", response_model=Phone)
def update_characteristics(id: str, new_characteristics: Characteristic):
    for phone in phones_db:
        if phone.identifier == id:
            phone.characteristics = new_characteristics
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with id '{id}' not found")
