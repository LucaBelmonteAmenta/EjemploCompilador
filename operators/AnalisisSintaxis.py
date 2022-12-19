from models.Simbolos import Simbolo
from core.FileAccess import FileAccess
import nltk


class Sintaxis():


    def __init__(self):
        self.ReglasDeProduccion = FileAccess().ProductionRules()
        self.ListaReglasDeProduccion = FileAccess().ProductionRules(True)
        self.Terminales = FileAccess().ReservedWordsList("token")
        self.NoTerminales = [regla["izquierda"] for regla in self.ListaReglasDeProduccion]


    def generateSyntaxTree(self, sentencia):

        try:

            gramatica = nltk.CFG.fromstring(self.ReglasDeProduccion)
            analizador = nltk.ChartParser(gramatica)
            arbol = analizador.parse_one(sentencia)

            if (arbol is None):
                result = {"Error" : True, "Data" : "La estructura definida no pertenece al lenguaje."}
            else:
                arbolString = str(arbol)
                arbolString.replace('\n', '')
                result = {"Error" : False, "Data" : arbolString}

            return result

        except Exception as e:
            result = {"Error" : True, "Data" : str(e)}
            return result


    def getTokens(self, simbolos):
        tokens = [simbolo["token"] for simbolo in simbolos]
        return tokens
 

    def splitTree(self, arbol):

        arbolDividido = []

        cadena = ""

        for caracter in arbol:

            if (caracter == " ") or (caracter == ")"):
                if (len(cadena) > 0):
                    arbolDividido.append(cadena)
                if (caracter == ")"):
                    arbolDividido.append(caracter)
                cadena = ""
            elif (caracter != '\n'):
                cadena = cadena + caracter
        
        return arbolDividido


    def adaptTreeStyle(self, arbol):

        reglasAplicadas = []
        
        for hoja in arbol:
            if ("(" in hoja) and (hoja[1:] in self.NoTerminales):              
                for regla in self.ListaReglasDeProduccion:                   
                    if (regla["izquierda"] == hoja[1:]):
                        reglasAplicadas.append(regla) 

        evolucionArbol = []

        for indice, regla in enumerate(reglasAplicadas):
            
            iteracionArbol = ""
            contadorNoTerminalesEncontrados = 0
            nivel = 0
            wantedRuleFlag = False

            for hoja in arbol:

                reglasEjecutadas = indice + 1

                if ("(" in hoja):
                    nivel = nivel + 1
                elif (hoja == ")"):    
                    nivel = nivel - 1

                if ("(" in hoja) and (hoja[1:] in self.NoTerminales):
                    contadorNoTerminalesEncontrados = contadorNoTerminalesEncontrados + 1
                    if (contadorNoTerminalesEncontrados == reglasEjecutadas):
                        wantedRuleFlag = not wantedRuleFlag
                    if (wantedRuleFlag):
                        if (nivel <= reglasEjecutadas):
                            iteracionArbol = iteracionArbol + ' ' + hoja[1:]
                        
                elif (nivel < (reglasEjecutadas)):
                    if (contadorNoTerminalesEncontrados < reglasEjecutadas) and (hoja != ")"):
                        iteracionArbol = iteracionArbol + ' ' + hoja
                
                #print("nivel:", nivel, "        reglasAplicadas:", reglasEjecutadas, "          hoja:", hoja,  "           iteracionArbol:", iteracionArbol)
            
            evolucionArbol.append(iteracionArbol[1:])

        #print(evolucionArbol)

        return reglasAplicadas
                    

    def run(self, entrada):

        tokens = []
        parse = []
        errores = []
        arboles = []

        for linea in entrada:
            simbolos = linea["Simbolos"]
            tokensLinea = self.getTokens(simbolos)
            diccionarioToken = {"Numero de Linea" : linea["Numero de Linea"], "Linea" : linea["Linea"], "Tokens" : str(tokensLinea)}
            tokens.append(diccionarioToken)
            arbolSintactico = self.generateSyntaxTree(tokensLinea)
            if (arbolSintactico["Error"]):
                diccionarioError = {"Numero de Linea" : str(linea["Numero de Linea"]), "Linea" : str(linea["Linea"]), "Error" : str(arbolSintactico["Data"])}
                errores.append(str(diccionarioError))
            else:
                arbol = arbolSintactico["Data"]
                arboles.append(arbol)
                reglasAplicadas = self.adaptTreeStyle(self.splitTree(arbol))
                parse.append(reglasAplicadas)

        result = {"Tokens" : str(tokens) , "Parse" :  str(parse), "Error" : str(errores), "arbol" : arboles}

        return result
