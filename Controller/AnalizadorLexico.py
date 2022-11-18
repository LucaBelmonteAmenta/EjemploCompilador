import sys
from FileName import direccion_carpeta_archivo as path
direccion_carpeta_Model = path(False, "Model")
sys.path.append(direccion_carpeta_Model)
from Simbolos import Simbolo
from FileAccess import FileAccess
import string
import re



class Automata():

    letras = list(string.ascii_letters)	

    def isPalabraReservada(self, cadenaCaracteres):
        return cadenaCaracteres in FileAccess().lista_palabras_reservadas()
    
    def isIdentificador(self, cadenaCaracteres):
        
        palabrasReservadas = FileAccess().lista_palabras_reservadas()
        codicion_1 = cadenaCaracteres in palabrasReservadas
        codicion_2 = self.isNumero(cadenaCaracteres) | self.isReal(cadenaCaracteres)
        codicion_3 = self.haveLetra(cadenaCaracteres)
        resultado = (not codicion_1) & (not codicion_2) & (codicion_3)

        return resultado


    def isNumero(self, cadenaCaracteres):
        return cadenaCaracteres.isnumeric()


    def isReal(self, cadenaCaracteres):
        try:
            float(cadenaCaracteres)
            return True
        except ValueError:
            return False


    def haveLetra(self, cadenaCaracteres):
        condicion = any(letra in cadenaCaracteres for letra in self.letras)
        return condicion



class Lexico():


    def __init__(self):
        self.palabras_reservadas = FileAccess().lista_palabras_reservadas()


    def obtener_lexemas(self, String):

        lista_elementos = []

        elementos = String.split()

        for elemento in elementos:

            condicion_hay_palabra_reservada = any(palabras_reservada in elemento for palabras_reservada in self.palabras_reservadas)

            if (not condicion_hay_palabra_reservada):
                lista_elementos.append(elemento)
            else:

                condicion_es_palabra_reservada = Automata().isPalabraReservada(elemento)

                if (condicion_es_palabra_reservada):
                    lista_elementos.append(elemento)
                else:

                    simbolo = ""

                    for caracter in elemento:
                        
                        if (Automata().isPalabraReservada(caracter)) :

                            if (len(simbolo) > 0):
                                lista_elementos.append(simbolo)
                                simbolo = ""

                            lista_elementos.append(caracter)

                        else:

                            simbolo += caracter


                    if (len(simbolo) > 0):
                        lista_elementos.append(simbolo)    

        lista_lexemas = []
        cadena_caracteres_string = []
        marca_string = False
                    
        for elemento in lista_elementos:

            if (elemento == "'"):
                
                if len(cadena_caracteres_string) > 0:
                    lista_lexemas.append(" ".join(cadena_caracteres_string))
                    cadena_caracteres_string = []

                marca_string = not marca_string
                lista_lexemas.append(elemento)

            elif (marca_string):
                cadena_caracteres_string.append(elemento)

            else:
                lista_lexemas.append(elemento)

        return lista_lexemas


    def analizarLinea(self, String, numero_linea):
        datosAnalizados = {"Numero de Linea" : numero_linea , "Linea" : String , "Simbolos" : []}
        lexemas = self.obtener_lexemas(String)
        lista_simbolos = []
        marca_string = False

        for lexema in lexemas:
            
            if (lexema == "'"):
                marca_string = not marca_string

            lista_simbolos.append(self.analizarLexema(lexema, marca_string).diccionario())

        datosAnalizados["Simbolos"] = lista_simbolos

        return datosAnalizados


    def analizarLexema(self, String, marca_string):

        if marca_string:
            token = "String"
        elif (Automata().isPalabraReservada(String)):
            token = FileAccess().obtenerSimbolo(String).token
        elif (Automata().isIdentificador(String)):
            token = "id"
        elif (Automata().isNumero(String)):
            token = "Integer"
        elif (Automata().isReal(String)):
            token = "Real"       
        else:
            token = "ERROR"

        simbolo = Simbolo(token, String, Automata().isPalabraReservada(String))

        return simbolo



if __name__ == "__main__":
    linea = "terminar;"    
    print(Lexico().analizarLinea(linea, 1))


 