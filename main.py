from fastapi import FastAPI, HTTPException
import db
    
app = FastAPI()

@app.get("/registro/balance/")
async def obtener_balance():
    registros = db.obtener_registros()
    lista_final = []
    for i in range(len(registros)):
        if registros[i].id_usuario == 1:
           lista_final.append(registros[i])
    return lista_final