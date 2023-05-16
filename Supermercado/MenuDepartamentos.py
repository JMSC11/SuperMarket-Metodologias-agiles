from menu import Menu_Base

class Menu_Departamentos(Menu_Base):

    #Dado que Menu_Departamentos es subclase de Menu_Base, el método dunder __init__ debe 
    #sobreescribir al método __init__ de Menu_Base. Esto se hace con super()
    def __init__(self, opciones):
        super().__init__(opciones)

    def __str__(self):
        return f"{super().__str__()}"
    
