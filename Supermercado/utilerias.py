import os
from Producto import Producto
from Departamento import Departamento
class Archivo:

    def __init__(self, ruta):
        self.ruta_archivo = ruta

    def add_Product(self, producto):
        with open(self.ruta_archivo, "a", encoding="UTF8") as archivo:
            archivo.write(f"{producto.id},{producto.nombre},{producto.proveedor}\n")

    def add_Product_Depto(self, claveProducto, precio, claveDepto):
        with open(self.ruta_archivo, "a", encoding="UTF8") as archivo:
            archivo.write(f"{claveProducto},{precio},{claveDepto}\n")

    def add_Depto(self, depto):
        with open(self.ruta_archivo, "a", encoding="UTF8") as archivo:
            archivo.write(f"{depto.id},{depto.nombre},{depto.jefe_depto}\n")
        
        file = depto.id + "ProductosSepto.txt"
        self.genera_Archivo(file)


    def listar(self):
        with open(self.ruta_archivo, "r", encoding = "utf8") as archivo:
            print("Catálogo".center(50, "-"))
            print(archivo.read())

    def buscar(self,id):
        with open(self.ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for registro in lineas:
                if registro.startswith(str(id)):
                    return True
                
        return False
        
                

    def eliminar(self,id):
        # Leer el contenido del archivo y almacenarlo en una lista de diccionarios
        with open(self.ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        # Buscar el diccionario que corresponde al ID que deseas eliminar
        for registro in lineas:
            if registro.startswith(str(id)):
                lineas.remove(registro)
                break

        with open(self.ruta_archivo, "w") as archivo:
            archivo.writelines(lineas)


    def genera_ID(self):
        with open(self.ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
            num_filas = len(lineas)
            registros = lineas[num_filas-1].strip().split(",")
            id=int(registros[0])
            return id+1
        
    def genera_Archivo(self, file):
        with open(file, "w") as archivo:
            archivo.close()


