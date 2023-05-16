class Menu_Base():
    def __init__(self, opciones):
        self._opciones = opciones

    
    #Getters y setters
    #Indicamos con el decorador @property que se trata de un getter
    #Para el Setter debemos indicar con @atributo.setter
    @property
    def opciones(self):
        return self._opciones
    @opciones.setter
    def opciones(self, opciones):
        self._opciones = opciones

    def __str__(self):
        return f"opciones: {self._opciones}"
    
    def opcion(self):
        if len(self._opciones) < 1:
            return 0
            print("")
        else:
            for i in range(0,len(self._opciones)):
                op = i+1
                print(str(op) + ":" + self._opciones[i])
            print("")

        flag = True
        while flag:
            opcion = int(input('Escribe la opción deseada:'))
            print("El num es:")
            print(opcion)
            if opcion <1 or opcion > len(self._opciones):
                flag = True
            else:
                flag = False

        return opcion




        

