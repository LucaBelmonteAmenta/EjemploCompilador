import sys
from FileName import direccion_carpeta_archivo as path
direccion_carpeta_Model = path(False, "Model")
sys.path.append(direccion_carpeta_Model)
from Simbolos import Simbolo
import json 

class FileAccess():

    def obtenerSimbolo(self, lexema):

        simbolos = self.lista_simbolos_json()
            
        x = 0
        simbolo = simbolos[x]
        while (simbolo.lexema != lexema) and (x < len(simbolos) - 1):
            x += 1
            simbolo = simbolos[x]


        if (simbolo.lexema == lexema):
            simbolo = simbolo
        else:
            simbolo = Simbolo("?", lexema, False)

        return simbolo

    def lista_simbolos_json(self, retornar_Diccionario = False):

        direcciónArchivo = path(False, "Model", "\Simbolos.json")
        archivo = open(direcciónArchivo, mode = "r")
        simbolos = json.load(archivo)
        archivo.close()

        listaSimbolos = []

        if not retornar_Diccionario:
            
            for simbolo in simbolos:
                lexema = simbolo["lexema"]
                token = simbolo["token"]
                palabraReservada = bool(simbolo["palabra reservada"])
                listaSimbolos.append(Simbolo(token, lexema, palabraReservada))

            return listaSimbolos

        else:

            return simbolos

    def lista_palabras_reservadas(self):
        simbolos = self.lista_simbolos_json()
        lista = [simbolo.lexema for simbolo in simbolos if simbolo.palabraReservada]
        return lista

    def codigo_texto_entrada(self, direcciónArchivo):

        lista_codigo = []
        
        with open(direcciónArchivo, mode = 'r') as achivo:
            for linea in achivo:
                lista_codigo.append(linea)
        
        return lista_codigo


