flag = True
while flag:
    opcion = int(input('Escribe la opción deseada:'))
    print("El num es:")
    print(opcion)
    if opcion <1 or opcion > 5:
        flag = True
    else:
        flag = False

        
