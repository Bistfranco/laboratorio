##############################

# Desafío 1: Sistema de Gestión de Productos
# Objetivo: Desarrollar un sistema para manejar productos en un inventario.

# Requisitos:

# Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
# Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
# Implementar operaciones CRUD para gestionar productos del inventario.
# Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
# Persistir los datos en archivo JSON.

##############################

import json

class Producto:
    def __init__(self, nombre, precio, cantidad_stock, descuento=False, porcentaje_descuento=0):
        self.__nombre = nombre
        self.__precio = self.chequeo_precio(precio)
        self.__cantidad_stock = self.chequeo_precio(cantidad_stock)
        self.__descuento = self.chequeo_descuento(descuento)
        self.__porcentaje_descuento = self.porcentaje(porcentaje_descuento)

    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def cantidad_stock(self):
        return self.__cantidad_stock
    
    @property
    def descuento(self):
        return self.__descuento
    
    @property
    def porcentaje_descuento(self):
        return self.__porcentaje_descuento
    
    @cantidad_stock.setter
    def cantidad_stock(self, stock):
        self.__cantidad_stock = self.chequeo_precio(stock)

    
    @precio.setter
    def precio(self, precio_nuevo):
        self.__precio = self.chequeo_precio(precio_nuevo)


    def chequeo_precio(self, precio):
        try:
            precio_num = float(precio)
            if precio_num < 0:
                raise ValueError('El precio debe ser un numero positivo')
            return precio_num

        except ValueError:
            raise ValueError ('El precio debe ser un numero')
        
    @descuento.setter
    def descuento(self, descuento_nuevo):
        self.__descuento = self.chequeo_descuento(descuento_nuevo) 

    def chequeo_descuento(self, descuento):
        if not isinstance(descuento, bool):
            raise ValueError('El valor debe ser un bool')
        return descuento
        
    @porcentaje_descuento.setter
    def porcentaje(self, porcentaje_descuento_nuevo):
        self.__porcentaje_descuento = self.validar_porcentaje_descuento(porcentaje_descuento_nuevo)


    def validar_porcentaje_descuento(self, porcentaje):
        if self.__descuento:
            try: 
                porcentaje_num = float(porcentaje)
                if porcentaje_num <= 0:
                    raise ValueError('El descuento debe ser mayor a 0')
                return porcentaje_num
            except ValueError:
                raise ValueError('El descuento debe de un numero positivo')
        else:
            return 0
    
    def to_dict(self):
        return {
            'nombre' : self.nombre,
            'precio' : self.precio,
            'cantidad_stock' : self.cantidad_stock,
            'descuento' : self.descuento,
            'porcentaje_descuento' : self.porcentaje_descuento
        }
    
    def __str__(self):
        return f'{self.nombre} {self.precio} {self.cantidad_stock}'
    
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad_stock, garantia, voltaje, descuento=False, porcentaje_descuento=0, ):
        super().__init__(nombre, precio, cantidad_stock, descuento, porcentaje_descuento)
        self.__garantia = garantia,
        self.__voltaje = voltaje

    @property
    def garantia(self):
        return self.__garantia
    
    @property
    def voltaje(self):
        return self.__voltaje

    def to_dict(self):
        data = super().to_dict()
        data['garantia'], data['voltaje'] = self.garantia, self.voltaje
        return data
    
    def __str__(self):
        return f'{super().__str__()} voltaje: {self.voltaje} garantia: {self.garantia}'

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad_stock, fecha_vencimiento, descuento=False, porcentaje_descuento=0):
        super().__init__(nombre, precio, cantidad_stock, descuento, porcentaje_descuento)
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento

    def to_dict(self):
        data = super().to_dict() 
        data['fecha_vencimiento'] = self.fecha_vencimiento
        return data
    
    def __str__(self):
        return f'{super().__str__()} fecha de vencimiento: {self.fecha_vencimiento}'

class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)

        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception (f'Error al leer el archivo: {error}')
        else:
            return datos


    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump
        except IOError as error:
            print(f'Error al guardar el archivo: {self.archivo}: {error}')
        except Exception as error:
            print(error)

    def crear_productos(self, productos):
        try:
            datos = self.leer_datos()
            nombre = productos.nombre
            if not nombre in datos.keys():
                datos[nombre] = productos.to_dict()
                self.guardar_datos(datos)
                print(f'Guardado Exitoso')
        except Exception as error:
            print(f'Error: {error}')

    def leer_producto(self, nombre_producto):
        try:
            datos = self.leer_datos()
            producto = datos.get(nombre_producto)
            if producto:
                return producto
            else:
                print(f'Producto {nombre_producto} no encontrado.')
                return None
        except Exception as error:
            print(f'Error al leer el producto {nombre_producto}: {error}')
            return None

    def actualizar_producto(self, producto_actualizado):
        try:
            datos = self.leer_datos()
            nombre = producto_actualizado.nombre
            if nombre in datos:
                datos[nombre] = producto_actualizado.to_dict()
                self.guardar_datos(datos)
                print(f'Producto {nombre} actualizado exitosamente.')
            else:
                print(f'Producto {nombre} no encontrado.')
        except Exception as error:
            print(f'Error al actualizar el producto {nombre}: {error}')

    def eliminar_producto(self, nombre_producto):
        try:
            datos = self.leer_datos()
            if nombre_producto in datos:
                del datos[nombre_producto]
                self.guardar_datos(datos)
                print(f'Producto {nombre_producto} eliminado exitosamente.')
            else:
                print(f'Producto {nombre_producto} no encontrado.')
        except Exception as error:
            print(f'Error al eliminar el producto {nombre_producto}: {error}')