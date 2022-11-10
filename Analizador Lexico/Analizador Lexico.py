from Simbolos import Simbolo, obtener_lista_simbolos

class Automata():

    simbolos = obtener_lista_simbolos()
    
    def sIdentificador(self, cadenaCaracteres):
        palabrasReservadas = [simbolo.lexema for simbolo in self.simbolos if simbolo.palabraReservada ]
        codicion_1 = cadenaCaracteres in palabrasReservadas
        codicion_2 = self.isNumero(cadenaCaracteres) | self.isReal(cadenaCaracteres)
        
        codicion_3 = any(cadenaCaracteres in letra for letra in letras)

        return (not codicion_1) & (not codicion_2) & (not codicion_3)

    def isNumero(self, cadenaCaracteres):
        return cadenaCaracteres.isnumeric()

    def isReal(self, cadenaCaracteres):
        try:
            float(cadenaCaracteres)
            return True
        except ValueError:
            return False


class Lexico():
    
    def analizarLinea(String):
        pass

    def analizarLexema(String):
        pass

