from controllers.Controller import Controller
from operators.AnalisisLexico import Lexico
from operators.AnalisisSintaxis import Sintaxis
from core.FileAccess import FileAccess
from core.Core import Core

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    
    def __init__(self):
        self.homeView = self.loadView("Home")
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    
    def cargarTablaSimbolos(self):
        c = Core.openController("TablaSimbolos")
        c.main()
    
    def analisisLexico(self, entrada):
        salida = Lexico().run(entrada)
        FileAccess().CreateNewFile("Fichero de Lexico", str(salida).replace("{", "{ \n"))
        return salida

    def analisisSintaxis(self, entrada):
        
        salida = Sintaxis().run(entrada)
        
        FileAccess().CreateNewFile("Fichero de Tokens", salida["Tokens"].replace("},", "}, \n"))
        FileAccess().CreateNewFile("Fichero de Parse", salida["Parse"].replace("},", "}, \n"))
        FileAccess().CreateNewFile("Fichero de Errores", salida["Error"].replace("},", "}, \n"))
        
        simbolos = FileAccess().ReservedWordsList("all attributes")
        lexemas = FileAccess().ReservedWordsList("lexema")
        nuevosLexemas = []
        
        for linea in entrada:
            for simbolo in linea["Simbolos"]:
                if (simbolo["lexema"] not in lexemas) and (simbolo["lexema"] not in nuevosLexemas):
                    simbolos.append(simbolo)
                    nuevosLexemas.append(simbolo["lexema"])

        resultParse = str(simbolos)
        resultParse.replace("},", "}, \n")
        resultParse.replace("[{", "[{ \n")
        resultParse.replace("[{", "[{ \n")
        resultParse.replace("[{", "[{ \n")

        FileAccess().CreateNewFile("Fichero de Tabla de Símbolos", resultParse)

        return salida["arbol"]
    
    """
        @Override
    """
    def main(self):
        self.homeView.main()
