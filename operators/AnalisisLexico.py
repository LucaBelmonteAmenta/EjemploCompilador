from models.Simbolos import Simbolo
from core.FileAccess import FileAccess

import string

class Automata():

    letras = list(string.ascii_letters)	

    def isPalabraReservada(self, cadenaCaracteres):
        condicion = cadenaCaracteres in FileAccess().ReservedWordsList("lexema")
        return condicion
    
    def isIdentificador(self, cadenaCaracteres):
        
        codicion_1 = self.isPalabraReservada(cadenaCaracteres)
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
        self.palabras_reservadas = FileAccess().ReservedWordsList("all attributes", False)


    def separateLexemas(self, String):

        lista_elementos = []

        PrimeraDivicion = String.split()

        for elemento in PrimeraDivicion:

            condicion_HAY_palabra_reservada = any(palabra_reservada.lexema in elemento for palabra_reservada in self.palabras_reservadas)
            condicion_ES_palabra_reservada = Automata().isPalabraReservada(elemento)

            if (condicion_ES_palabra_reservada or not condicion_HAY_palabra_reservada):
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

            if (elemento == "'") or (elemento == "\""):
                
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


    def analyzeLexema(self, String, marca_string):

        if marca_string:
            token = "tex"
        elif (Automata().isPalabraReservada(String)):
            token = FileAccess().getSimbolo(String).token
        elif (Automata().isIdentificador(String)):
            token = "id"
        elif (Automata().isNumero(String)):
            token = "num"
        elif (Automata().isReal(String)):
            token = "Real"       
        else:
            token = "ERROR"

        simbolo = Simbolo(token, String, Automata().isPalabraReservada(String))

        return simbolo


    def run(self, entrada):
        
        result = []

        for indice, linea in enumerate(entrada):

            lineaAnalizada = {"Numero de Linea" : indice , "Linea" : linea , "Simbolos" : []}
            simbolosLinea = []

            lexemas = self.separateLexemas(linea)
            marca_string = False

            for lexema in lexemas:

                if (lexema == "'") or (lexema == "\""):
                    if marca_string:
                        marca_string = not marca_string
                        analisisUnitario = self.analyzeLexema(lexema, marca_string)
                    else:
                        analisisUnitario = self.analyzeLexema(lexema, marca_string)
                        marca_string = not marca_string                              
                else:
                    analisisUnitario = self.analyzeLexema(lexema, marca_string)
                
                simbolosLinea.append(analisisUnitario.diccionario())
            
            lineaAnalizada["Simbolos"] = simbolosLinea
            result.append(lineaAnalizada)

        return result




 