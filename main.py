from rich.console import Console
from rich.table import Table

from src.tienda.producto import Producto
from src.tienda.gestionar_json import informacion_producto, vender_producto, mostrar_todos_productos

def main():
    #Tabla para el menú
    console = Console()
    tabla = Table(show_lines=True)
    tabla.add_column("Menú", justify="center")
    tabla.add_row("1.Agregar nuevo producto")
    tabla.add_row("2.Ver información de un producto")
    tabla.add_row("3.Mostrar todos los productos")
    tabla.add_row("4.Vender producto")
    console.print(tabla)

    while True:
        op = input("Ingrese la opción que desee realizar: ")
        if op not in ("1", "2", "3", "4"):
            print("La opción que ingresó no existe. Por favor ingrese una válida.")
            continue
        break

    if op == "1":
        nombre = input("Ingrese el nombre del producto: ")
        while True:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                cantidad = int(input("¿Cuántas unidades dispone del producto?: "))
                if precio < 1 or cantidad < 1:
                    print("Tanto el precio con la cantidad deben ser mayores a 0.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        producto = Producto(nombre, cantidad, precio)
        producto.nuevo_producto()
    elif op == "2":
        producto_buscar = input("Ingrese el nombre o el código del producto que desea buscar: ")
        informacion_producto(producto_buscar)
    elif op == "3":
        lista = mostrar_todos_productos()
        table = Table(show_lines=True)
        table.add_column("Código", justify="center")
        table.add_column("Nombre", justify="center")
        table.add_column("Precio", justify="center")
        table.add_column("Cantidad", justify="center")

        for i in lista:
            table.add_row(f"{i["codigo"]}", f"{i["nombre"]}", f"{i["precio"]}", f"{i["cantidad"]}")

        console.print(table)
    elif op == "4":
        producto = input("Ingrese el nombre o el código del producto que va a  vender: ")
        while True:
            try:
                cantidad = int(input("¿Cuántas unidades venderá del producto?: "))
                if cantidad < 1:
                    print("La cantidad debe ser mayor a 0.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        vender_producto(producto, cantidad)
        

if __name__ == "__main__":
    main()