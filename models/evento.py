import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

from models.baseMongo import MongoBase

class Evento(BaseModel, MongoBase):
    id: PydanticObjectId = Field(alias="_id")
    nombre: str
    fecha: datetime.datetime
    lugar: str
    lat: str
    long: str

class EventoNew(BaseModel, MongoBase):
    nombre: str
    fecha: datetime.datetime
    lugar: str
    lat: str
    long: str

class EventoUpdate(BaseModel, MongoBase):
    nombre: Optional[str] = None
    fecha: Optional[datetime.datetime] = None
    lugar: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    organizador: Optional[str] = None
    imagen: Optional[str] = None

class EventoQuery(BaseModel):
    nombre: Optional[str] = None
    fecha: Optional[datetime.datetime] = None
    lugar: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    organizador: Optional[str] = None
    imagen: Optional[str] = None

class EventoList(BaseModel):
    eventos: List[Evento]
