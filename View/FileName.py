def direccion_carpeta_archivo(mismo_directorio, nombre1, nombre2 = None):
    
    ruta = __file__
    lista = ruta.split('\\')

    if (mismo_directorio):
        lista = lista[0:-1]
    else:
        lista = lista[0:-2]

    lista.append(nombre1)

    if (nombre2 is not None):
        lista.append(nombre2)

    direccion = '\\'.join(lista)

    return direccion