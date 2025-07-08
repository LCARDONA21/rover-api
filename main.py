from fastapi import FastAPI
from pydantic import BaseModel
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
    objetivo_esp_1: str
    objetivo_esp_2: str
    objetivo_esp_3: str
    justificacion: str
    descripcion: str
    duracion: str
    fechas: str
    presupuesto_transporte: str
    presupuesto_materiales: str
    presupuesto_refrigerios: str
    presupuesto_total: str
    poblacion: str
    finalidad: str
    indicador_1: str
    indicador_2: str
    indicador_3: str

@app.post("/generar_proyecto")
def generar(data: Proyecto):
    prompt = f"""
Redacta un proyecto scout con los siguientes datos:

Título: {data.titulo}
Grupo: {data.grupo}
Eje: {data.eje}
Objetivo General: {data.objetivo_general}
Objetivos Específicos:
- {data.objetivo_esp_1}
- {data.objetivo_esp_2}
- {data.objetivo_esp_3}
Justificación: {data.justificacion}
Descripción: {data.descripcion}
Duración: {data.duracion} ({data.fechas})
Presupuesto:
- Transporte: {data.presupuesto_transporte}
- Materiales: {data.presupuesto_materiales}
- Refrigerios: {data.presupuesto_refrigerios}
- Total: {data.presupuesto_total}
Población objetivo: {data.poblacion}
Finalidad: {data.finalidad}
Indicadores de éxito:
- {data.indicador_1}
- {data.indicador_2}
- {data.indicador_3}

Usa lenguaje scout, claro, estructurado y motivador.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"proyecto": response.choices[0].message.content}
