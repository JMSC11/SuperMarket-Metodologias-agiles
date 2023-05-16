class Departamento:
    def __init__(self, id, nombre, jefe_depto):
        self._id = id
        self._nombre = nombre
        self._jefe_depto = jefe_depto

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def jefe_depto(self):
        return self._jefe_depto
    @jefe_depto.setter
    def jefe_depto(self, jefe_depto):
        self._jefe_depto = jefe_depto

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        return f"Id: {self._id} Nombre: {self._nombre} Proveedor: {self._jefe_depto} "

