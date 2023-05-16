from  MenuPrincipal import Menu_Principal
from  MenuProductos import Menu_Productos
from  MenuDepartamentos import *
from MenuAsignacionProds import *
from MenuPrecios import *
from Producto import *
from utilerias import *
from Departamento import Departamento
import sys


class Supermercado():

    opciones = []

    def __init__(self,opciones):
        self.opciones=opciones
        
    def mostrar_Menu(self):
        menu = Menu_Principal(self.opciones)
        flag = True

        while flag:
            opcion = menu.opcion()

            if opcion == 1:
                print("Opción productos")
                self.productos()
            elif opcion ==2:
                print("Opción departamentos")
                self.departamentos()
            elif opcion ==3:
                print("Opción asignaciones")
                self.asignacion()
            elif opcion ==4:
                print("Opción precios")
                self.precio()
            elif opcion ==5:
                print("Opción salir")
                flag = self.salir()
                sys.exit()    
            else: 
                print("Opcion no valida")
    
    def productos(self):
        opciones = ["Alta producto", "Visualizar productos", "Baja Producto", "Regresar"]

        menu = Menu_Productos(opciones)


        while True:
            opcion = menu.opcion()

            if opcion == 1:
                print("Opción Alta producto")
                self.Alta_Producto()
            elif opcion ==2:
                print("Opción Visualizar productos")
                self.Ver_Producto()
            elif opcion ==3:
                print("Opción Baja productos")
                self.Baja_Producto()
            elif opcion ==4:
                print("Opción regresar")
                self.Regresar()
            else: 
                print("Opcion no valida")

    def Alta_Producto(self):
        print("Alta producto")
        archivo = Archivo("Productos.txt")
        id= archivo.genera_ID()
        nombre_producto = input("Ingresa el nombre del producto: ")
        proveedor = input("Ingresa el proveedor: ")
        print("Agregando producto al catálogo.")
        producto = Producto(id, nombre_producto, proveedor)
        archivo.add_Product(producto)

    def Baja_Producto(self):
        archivo = Archivo("Productos.txt")
        print("Baja producto")
        id = int(input("Ingresa el id a eliminar"))
        archivo.eliminar(id)

    def Ver_Producto(self):
        archivo = Archivo("Productos.txt")
        print("Ver productos")
        archivo.listar()

    def Regresar(self):
        print("Regresar")
        self.mostrar_Menu()

    def departamentos(self):
        opciones = ["Alta departamento", "Visualizar departamento", "Baja departamento", "Regresar"]

        menu = Menu_Departamentos(opciones)


        while True:
            opcion = menu.opcion()

            if opcion == 1:
                print("Opción Alta departamento")
                self.Alta_Departamento()
            elif opcion ==2:
                print("Opción Visualizar departamento")
                self.Ver_Departamento()
            elif opcion ==3:
                print("Opción Baja departamento")
                self.Baja_Departamento()
            elif opcion ==4:
                print("Opción regresar")
                self.Regresar()
            else: 
                print("Opcion no valida")
   
    def Alta_Departamento(self):
        print("Alta departamento")
        archivo = Archivo("Departamentos.txt")
        id= input("Ingresa el Id del departamento:")
        nombre_producto = input("Ingresa el nombre del departamento: ")
        jefe_depto = input("Ingresa el Jefe del departamento: ")
        print("Agregando departamento al catálogo.")
        depto = Departamento(id, nombre_producto, jefe_depto)
        archivo.add_Depto(depto)

    def Baja_Departamento(self):
        print("Baja departamento")
        archivo = Archivo("Departamentos.txt")
        id = input("Ingresa el id a eliminar")
        archivo.eliminar(id)
    def Ver_Departamento(self):
        print("Ver departamento")
        archivo = Archivo("Departamentos.txt")
        archivo.listar()

    def asignacion(self):
        opciones = ["Alta producto en departamento", "Baja producto en departamento", "Regresar"]

        menu = Menu_Asignacion(opciones)


        while True:
            opcion = menu.opcion()

            if opcion == 1:
                print("Opción Alta producto en  departamento")
                self.Alta_Producto_Departamento()

            elif opcion ==2:
                print("Opción Baja producto en  departamento")
                self.Baja_Producto_Departamento()
            elif opcion ==3:
                print("Opción regresar")
                self.Regresar()
            else: 
                print("Opcion no valida")
   
    def Alta_Producto_Departamento(self):
        print("Alta producto en departamento")

    def Baja_Producto_Departamento(self):
        print("Baja producto en  departamento")

    


    def precio(self):
        opciones = ["Asignar precio a un producto", "Consultar precios de productos por depto", "Regresar"]

        menu = Menu_Precios(opciones)


        while True:
            opcion = menu.opcion()

            if opcion == 1:
                print("Asignar precio a un producto")
                self.Asignar_Precio()

            elif opcion ==2:
                print("Consultar precios de productos por depto")
                self.Consultar_Precio()
            elif opcion ==3:
                print("Opción regresar")
                self.Regresar()
            else: 
                print("Opcion no valida")
   
    def Asignar_Precio(self):
        print("Asignar Precio")

    def Consultar_Precio(self):
        print("Consultar Precio")

    def salir(self):
        print("")
        print("Hasta pronto")
        return False


        
        






opc = ["Productos", "Departamentos", "Asignación de productos a un departamento", "Precios", "Salir"]
m = Supermercado(opc)
m.mostrar_Menu()
