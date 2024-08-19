import os
import platform
import json

from laboratorio import ProductoElectronico, ProductoAlimenticio, GestionProductos  

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') 

def mostrar_menu():
    print("========== Menú de Gestión de Productos ==========")
    print('1. Agregar Producto Electrónico')
    print('2. Agregar Producto Alimenticio')
    print('3. Buscar Producto por Nombre')
    print('4. Actualizar Stock de Producto')
    print('5. Eliminar Producto por Nombre')
    print('6. Mostrar Todos los Productos')
    print('7. Salir')
    print('==================================================')

def agregar_producto(gestion, tipo_producto):
    try:
        nombre = input('Ingrese nombre del producto: ')
        precio = float(input('Ingrese precio del producto: '))
        cantidad_stock = int(input('Ingrese cantidad en stock del producto: '))
        descuento = input('¿El producto tiene descuento? (S/N): ').strip().lower() == 's'
        porcentaje_descuento = 0
        if descuento:
            porcentaje_descuento = float(input('Ingrese porcentaje de descuento: '))

        if tipo_producto == '1':
            garantia = input('Ingrese garantía del producto electrónico: ')
            voltaje = input('Ingrese voltaje del producto electrónico: ')
            producto = ProductoElectronico(nombre, precio, cantidad_stock, garantia, voltaje, descuento, porcentaje_descuento)
        elif tipo_producto == '2':
            fecha_vencimiento = input('Ingrese fecha de vencimiento del producto alimenticio: ')
            producto = ProductoAlimenticio(nombre, precio, cantidad_stock, fecha_vencimiento, descuento, porcentaje_descuento)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        print('Producto agregado con éxito.')
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_producto_por_nombre(gestion):
    nombre = input('Ingrese el nombre del producto a buscar: ')
    gestion.leer_producto(nombre)
    input('Presione enter para continuar...')

def actualizar_stock_producto(gestion):
    nombre = input('Ingrese el nombre del producto para actualizar el stock: ')
    nuevo_stock = int(input('Ingrese la nueva cantidad de stock: '))
    gestion.actualizar_producto(nombre, nuevo_stock)
    input('Presione enter para continuar...')

def eliminar_producto_por_nombre(gestion):
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    gestion.eliminar_producto(nombre)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('=============== Listado completo de Productos ==============')
    for producto in gestion.leer_todos_productos().values():
        print(producto)
    print('============================================================')
    input('Presione enter para continuar...')

if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion = GestionProductos(archivo_productos)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        
        elif opcion == '3':
            buscar_producto_por_nombre(gestion)

        elif opcion == '4':
            actualizar_stock_producto(gestion)

        elif opcion == '5':
            eliminar_producto_por_nombre(gestion)

        elif opcion == '6':
            mostrar_todos_los_productos(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
