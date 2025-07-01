from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from modules.calcul import calcul_carre

app = FastAPI()

class NumberRequest(BaseModel):
    number: int

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Bienvenue sur l'API de calcul de carré."}

@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.post("/calcul")
def calcul(req: NumberRequest):
    logger.info(f"Calcul du carré pour: {req.number}")
    result = calcul_carre(req.number)
    return {"result": result}
