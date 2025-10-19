import json
from .gestionar_json import leer_archivo, escribir_archivo

class Producto:
    def __init__(self, nombre, cantidad, precio, ruta = "data/productos.json"):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.ruta = ruta

    def nuevo_producto(self):
        productos = leer_archivo(self.ruta)
        nuevo = {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "codigo": len(productos) + 1
        }
        
        for i in productos:
            if i["nombre"] == self.nombre:
                print(f"El producto '{self.nombre}' ya existe.")
                break
        else:
            productos.append(nuevo)
            escribir_archivo(productos)
            print("Producto agregado.")