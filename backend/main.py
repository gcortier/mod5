import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI, Form
from pydantic import BaseModel
from loguru import logger
from modules.calcul import calcul_carre


from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from loguru import logger
import os
import psutil
from starlette.responses import Response


## Base initialisation for Loguru and FastAPI
from api_base import setup_loguru, app, Request, HTTPException
logger = setup_loguru("logs/main_api.log")

class NumberRequest(BaseModel):
    number: int

@app.post("/calcul")
def calcul(req: NumberRequest):
    result = calcul_carre(req.number)
    logger.info(f"Calcul du carré pour: {req.number} : result : {result}")
    return {"result": result}

@app.post("/data")
async def receive_color(data: str = Form(...)):
    logger.info(f"Received data: {data}")
    return {"message": f"data {data} received"}

@app.get("/metrics")
async def metrics():
    return "toto"