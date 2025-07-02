import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from modules.calcul import calcul_carre

## Base initialisation for Loguru and FastAPI
from api_base import setup_loguru, app, Request, HTTPException
logger = setup_loguru("logs/main_api.log")

class NumberRequest(BaseModel):
    number: int

@app.post("/calcul")
def calcul(req: NumberRequest):
    logger.info(f"Calcul du carré pour: {req.number}")
    result = calcul_carre(req.number)
    return {"result": result}
