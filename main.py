from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import openai
import os
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Proyecto(BaseModel):
    titulo: str
    grupo: str
    eje: str
    objetivo_general: str
    objetivo_esp_1: Optional[str] = None
    objetivo_esp_2: Optional[str] = None
    objetivo_esp_3: Optional[str] = None
    justificacion: Optional[str] = None
    descripcion: Optional[str] = None
    duracion: Optional[str] = None
    fechas: Optional[str] = None
    presupuesto_transporte: Optional[str] = None
    presupuesto_materiales: Optional[str] = None
    presupuesto_refrigerios: Optional[str] = None
    presupuesto_total: Optional[str] = None
    poblacion: Optional[str] = None
    finalidad: Optional[str] = None
    indicador_1: Optional[str] = None
    indicador_2: Optional[str] = None
    indicador_3: Optional[str] = None

@app.post("/generar_proyecto")
def generar(data: Proyecto):
    prompt = f"""
Redacta un proyecto scout con los siguientes datos:

Título: {data.titulo}
Grupo: {data.grupo}
Eje: {data.eje}
Objetivo General: {data.objetivo_general}
Objetivos Específicos:
- {data.objetivo_esp_1 or ""}
- {data.objetivo_esp_2 or ""}
- {data.objetivo_esp_3 or ""}
Justificación: {data.justificacion or ""}
Descripción: {data.descripcion or ""}
Duración: {data.duracion or ""} ({data.fechas or ""})
Presupuesto:
- Transporte: {data.presupuesto_transporte or ""}
- Materiales: {data.presupuesto_materiales or ""}
- Refrigerios: {data.presupuesto_refrigerios or ""}
- Total: {data.presupuesto_total or ""}
Población objetivo: {data.poblacion or ""}
Finalidad: {data.finalidad or ""}
Indicadores de éxito:
- {data.indicador_1 or ""}
- {data.indicador_2 or ""}
- {data.indicador_3 or ""}

Usa lenguaje scout, claro, estructurado y motivador.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"proyecto": response.choices[0].message.content}
