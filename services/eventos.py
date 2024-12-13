import os
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
import pymongo
from models.evento import Evento, EventoList, EventoQuery, EventoNew, EventoUpdate


load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

eventos_router = APIRouter(prefix="/eventos", tags=["eventos"])

# Configuración de MongoDB
client = pymongo.MongoClient(MONGO_URL)
db = client.Eventual
eventos = db.eventos

# GET /eventos
# GET /eventos
@eventos_router.get("/", response_model=EventoList)
def get_eventos(query: EventoQuery = Depends()):
    try:
        eventData = eventos.find(query.model_dump(exclude_none=True))
        if eventData is None:
            raise HTTPException(status_code=404, detail="No se encontraron eventos")
        eventosList = EventoList(eventos=[Evento(**evento) for evento in eventData])
        return eventosList
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error al buscar los eventos: {str(e)}"
        )
    
        
# GET /eventos/{id}
@eventos_router.get("/{id}")
def get_evento(id: str):
    try:
        evento = eventos.find_one({"_id": ObjectId(id)})
        if evento:
            evento["_id"] = str(evento["_id"])
            return evento
        else:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error al buscar el evento: {str(e)}"
        )
    
# POST /eventos
@eventos_router.post("/", response_model=Evento)
def create_evento(evento: EventoNew):
    try:
        event_dump = evento.model_dump()
        evento_id = eventos.insert_one(event_dump).inserted_id
        event = eventos.find_one({"_id": ObjectId(evento_id)})
        return event
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error al crear el usuario: {str(e)}"
        )
    
# PUT /eventos/{id}
@eventos_router.put("/{id}", response_model=Evento)
def update_evento(id: str, evento: EventoUpdate):
    try:
        event_dump = evento.model_dump(
            exclude_unset=True
        )  # Exclude fields that were not set
        event_dump = {
            k: v for k, v in event_dump.items() if v is not None
        }  # Remove fields with None values
        if not event_dump:
            raise HTTPException(status_code=400, detail="No se proporcionaron campos para actualizar")
        result = eventos.update_one({"_id": ObjectId(id)}, {"$set": event_dump})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        evento = eventos.find_one({"_id": ObjectId(id)})
        if evento:
            evento["_id"] = str(evento["_id"])
            return evento
        else:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error al actualizar el evento: {str(e)}"
        )
    
# DELETE /eventos/{id}
@eventos_router.delete("/{id}")
def delete_user(id: str):
    try:
        result = eventos.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        return {"message": "Evento eliminado correctamente"}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error al eliminar el evento: {str(e)}"
        )