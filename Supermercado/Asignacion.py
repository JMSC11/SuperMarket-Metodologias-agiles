class Asignacion:
    def __init__(self, claveProd, precio, claveDepto):
        self._claveProd = claveProd
        self._precio = precio
        self._claveDepto = claveDepto
    @property
    def claveProd(self):
        return self._claveProd
    @claveProd.setter
    def claveProd(self, claveProd):
        self._claveProd = claveProd

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def claveDepto(self):
        return self._claveDepto
    @claveDepto.setter
    def claveDepto(self, claveDepto):
        self._claveDepto = claveDepto

    def __str__(self):
        return f"claveDepto: {self._claveDepto} clave producto: {self._claveProd} precio: {self._precio} "

