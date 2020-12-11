from pydantic import BaseModel

class Registro(BaseModel):
    id_usuario: int
    id: int
    tipo: str
    valor: int
    fecha: str
    etiqueta: str
    nota: str

registros = {
  1: Registro(id_usuario=1, id=1, tipo="egreso", valor= 2600, fecha= "10-12-20", etiqueta="comida", nota="pina"),
  2: Registro(id_usuario=1, id=2, tipo="ingreso", valor=28000, fecha="10-12-20", etiqueta="venta", nota="galletas y torta"),
  3: Registro(id_usuario=2, id=1, tipo="egreso", valor=4000, fecha="10-12-20", etiqueta="comida", nota="pina"),
  4: Registro(id_usuario=2, id=2, tipo="ingreso", valor=28000, fecha="10-12-20", etiqueta="venta", nota="galletas y torta")
}

def obtener_registros():
    lista_datos = []
    for e in registros:
      lista_datos.append(registros[e])
        #for i in range lista_datos.len():
    return lista_datos