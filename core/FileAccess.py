from config import APP_PATH
from models.Simbolos import Simbolo
import os
import json

if __name__ == "__main__":
    pass

class FileAccess():

    @staticmethod
    def openJson(nombreJson):
        
        response = None
        
        direcciónArchivo = APP_PATH + "/db/" + nombreJson + ".json"

        if os.path.exists(direcciónArchivo):
            archivo = open(direcciónArchivo, mode = "r")
            contenido = json.load(archivo)
            archivo.close()
            response = contenido

        return response


    def getSimbolo(self, lexema):

        if lexema in self.ReservedWordsList("lexema"):

            simbolos = self.ReservedWordsList("all attributes", False)

            puntero = 0
            simbolo = simbolos[puntero]

            while (simbolo.lexema != lexema):
                puntero += 1
                simbolo = simbolos[puntero]
 
        else:
            simbolo = Simbolo("?", lexema, False)

        return simbolo


    def ReservedWordsList(self, attributes, listadiccionarios = True, PalabraReservada = True):

        simbolos = self.openJson("Simbolos")

        listaSimbolos = []

        for simbolo in simbolos:

            lexema = simbolo["lexema"]
            token = simbolo["token"]
            palabraReservada = bool(simbolo["palabra reservada"])

            if listadiccionarios:
                listaSimbolos.append(Simbolo(token, lexema, palabraReservada).diccionario())
            else:
                listaSimbolos.append(Simbolo(token, lexema, palabraReservada))

        lista = []

        match attributes:
            case "lexema":
                if listadiccionarios:
                    lista = [simbolo["lexema"] for simbolo in simbolos if simbolo["palabra reservada"]]
                else:
                    lista = [simbolo.lexema for simbolo in simbolos if simbolo.palabraReservada]
            case "token":
                if listadiccionarios:
                    lista = [simbolo["token"] for simbolo in simbolos if simbolo["palabra reservada"]]
                else:
                    lista = [simbolo.token for simbolo in simbolos if simbolo.palabraReservada]
            case "all attributes":
                lista = listaSimbolos



        return lista
    

    def ProductionRules(self, lista=False):

        direccionArchivo = APP_PATH + "/db/Reglas de Producción.txt"
        reglasProduccion = self.TextFileAccess(direccionArchivo)

        if lista:

            response = []
            reglas = reglasProduccion.split("\n")

            contador = 0

            for regla in reglas:

                contador = contador + 1
                componentes = regla.split(" -> ")

                reglaUnitaria = {
                                "izquierda" : componentes[0],  
                                "derecha" : componentes[1], 
                                "indice" : contador
                                }

                response.append(reglaUnitaria)

        else:
            response = reglasProduccion

            
        return response


    def TextFileAccess(self, direcciónArchivo):
        
        if os.path.exists(direcciónArchivo):
            with open(direcciónArchivo, mode = 'r') as achivo:
                contenido = achivo.read()
        
        return contenido


    def CreateNewFile(self, nombreArchivo, contenido):
        direcciónArchivo = APP_PATH + "/db/" + nombreArchivo + ".txt"
        file = open(direcciónArchivo, 'w')
        file.writelines(str(contenido))
        file.close()
