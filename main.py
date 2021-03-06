from fastapi import FastAPI, HTTPException
import db
    
app = FastAPI()

@app.get("/registro/balance/{id}")
async def obtener_balance(id : int):
    registros = db.obtener_registros()
    lista_final = []
    ingresos = []
    egresos = []
    for i in range(len(registros)):
        if registros[i].id_usuario == id:
           lista_final.append(registros[i])
    
    for i in range(len(lista_final)):
        if lista_final[i].tipo == "ingreso":
            ingresos.append(lista_final[i].valor)
        else:
            egresos.append(lista_final[i].valor)

    return {"data":lista_final, "balance":sum(ingresos)-sum(egresos)}
