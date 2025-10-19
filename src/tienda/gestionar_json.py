import json

def leer_archivo(ruta = "data/productos.json"):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def escribir_archivo(nuevo_contenido, ruta = "data/productos.json"):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(nuevo_contenido, f, ensure_ascii=False, indent=4)
    

def informacion_producto(producto_buscar):
        productos = leer_archivo()

        for i in productos:
            if i["nombre"] == producto_buscar or str(i["codigo"]) == producto_buscar:
                print(f"Nombre: {i['nombre']}\nPrecio: {i['precio']}\nCantidad: {i['cantidad']}\nCódigo: {i['codigo']}")
                break
        else:
            print("El producto que desea buscar no existe.")

def vender_producto(producto, cantidad):
    productos = leer_archivo()

    for i in productos:
        if i["nombre"] == producto or str(i["codigo"]) == producto:
            if i["cantidad"] < cantidad:
                print(f"Solo contamos con {i['cantidad']} {i['nombre']}")
            elif i["cantidad"] == 0:
                print("Producto agotado")
            else:
                i["cantidad"] -= cantidad
                escribir_archivo(productos)
                print("Producto vendido")
            break
    else:
        print("No contamos con el producto que desea.")

def mostrar_todos_productos():
    productos = leer_archivo()
    return productos