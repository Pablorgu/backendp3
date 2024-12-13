import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from services.eventos import eventos_router
from services.mapas import mapas_bp
from services.usuarios import usuarios_router
from services.archivos import archivos_bp

load_dotenv()

port = int(os.getenv("PORT", 8000))

app = FastAPI()

app.include_router(usuarios_router)
app.include_router(mapas_bp)
app.include_router(eventos_router)
app.include_router(archivos_bp)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)