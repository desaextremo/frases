import random
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a los orígenes que desees permitir
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/getFrase/")
def get_frase():
    archivo_frases = open("frases.txt", "r",encoding="utf8")
    frases = archivo_frases.readlines()

    return random.choice(frases)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
