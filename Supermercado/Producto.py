class Producto:
    def __init__(self, id, nombre, proveedor):
        self._id = id
        self._nombre = nombre
        self._proveedor = proveedor

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def proveedor(self):
        return self._proveedor
    @proveedor.setter
    def proveedor(self, proveedor):
        self._proveedor = proveedor

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        return f"Id: {self._id} Nombre: {self._nombre} Proveedor: {self._proveedor} "

    def guardar_En_Archivo(file):
        #algo
        print("otro gato")
