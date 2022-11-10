import json

class Simbolo():
    
    # token -> String   lexema -> String   lexema -> boolena
    def __init__(self, token, lexema, palabraReservada):
        self.token = token
        self.lexema = lexema
        self.palabraReservada = palabraReservada

    def __str__(self):
        return f"Simbolo: Lexema = {self.lexema}  ||  Token = {self.token}  ||  Palabra Reservada = {self.palabraReservada}"


def direccion_archivos():
    
    ruta = __file__
    lista = ruta.split('\\')
    lista = lista[0:-1]

    return '\\'.join(lista)

def obtener_lista_simbolos():
    direcciónArchivo = direccion_archivos() + "\Simbolos.json"
    archivo = open(direcciónArchivo)
    simbolos = json.load(archivo)
    archivo.close()

    listaSimbolos = []

    for simbolo in simbolos:
        lexema = simbolo["lexema"]
        token = simbolo["token"]
        palabraReservada = bool(simbolo["palabra reservada"])
        listaSimbolos.append(Simbolo(lexema, token, palabraReservada))

    return listaSimbolos


if __name__ == "__main__":
    listaSimbolos = obtener_lista_simbolos()

    for simbolo in listaSimbolos:
        print(simbolo)

