import os
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
import pymongo

from models.archivo import ArchivoNew

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

usuarios_router = APIRouter(prefix="/usuarios", tags=["usuarios"])

# Configuración de MongoDB
client = pymongo.MongoClient(MONGO_URL)
db = client.Eventual
usuarios = db.usuarios