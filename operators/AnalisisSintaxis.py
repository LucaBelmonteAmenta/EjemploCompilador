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

        reglasAplicadas = [0]
        
        for hoja in arbol:
            if ("(" in hoja) and (hoja[1:] in self.NoTerminales):              
                for regla in self.ListaReglasDeProduccion:                   
                    if (regla["izquierda"] == hoja[1:]):
                        reglasAplicadas.append(regla["indice"]) 

        evolucionArbol = []

        for indice, regla in enumerate(reglasAplicadas):

            iteracionArbol = ""
            contadorReglasEncontradas = 0
            nivel = 0
            wantedRuleFlag = False

            for hoja in arbol:

                reglasAplicadas = indice + 1

                if ("(" in hoja):
                    nivel = nivel + 1
                elif (")" in hoja):    
                    nivel = nivel - 1

                if ("(" in hoja) and (hoja[1:] in self.NoTerminales):
                    contadorReglasEncontradas = contadorReglasEncontradas + 1
                    if (contadorReglasEncontradas == reglasAplicadas):
                        wantedRuleFlag = not wantedRuleFlag
                    if (wantedRuleFlag) and (nivel <= reglasAplicadas):
                        iteracionArbol = iteracionArbol + ' ' + hoja[1:]
                elif (nivel < (reglasAplicadas)):
                    if (")" in hoja):
                        iteracionArbol = iteracionArbol + ' ' + hoja[0:-1]
                    else:
                        iteracionArbol = iteracionArbol + ' ' + hoja
                
                print("nivel:", nivel, "        reglasAplicadas:", reglasAplicadas, "          hoja:", hoja,  "           iteracionArbol:", iteracionArbol)
            
            evolucionArbol.append(iteracionArbol[1:])

        print(evolucionArbol)
                    

    def run(self, entrada):

        tokens = []
        parse = []
        errores = []

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
                self.adaptTreeStyle(self.splitTree(arbolSintactico))
                parse.append(arbolSintactico["Data"])

        result = {"Tokens" : str(tokens) , "Parse" :  str(parse), "Error" : str(errores)}

        return result
