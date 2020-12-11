from pydantic import BaseModel

class Registro(BaseModel):
    id: int
    tipo: str
    valor: int
    fecha: str
    etiqueta: str
    nota: str

Registros = {
  1: Registro(id=1, tipo:"egreso", valor=2600, fecha="10-12-20", etiqueta="comida", nota="pina"),
  2: Registro(id=2, tipo:"ingreso", valor=28000, fecha="10-12-20", etiqueta="venta", nota="galletas y torta")
}

def obtener_balance():
    return Registros