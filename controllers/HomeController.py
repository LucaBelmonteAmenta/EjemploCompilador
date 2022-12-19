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
        FileAccess().CreateNewFile("Fichero de Lexico", salida)
        return salida

    def analisisSintaxis(self, entrada):
        salida = Sintaxis().run(entrada)
        FileAccess().CreateNewFile("Fichero de Tokens", salida["Tokens"])
        FileAccess().CreateNewFile("Fichero de Parse", salida["Parse"])
        FileAccess().CreateNewFile("Fichero de Errores", salida["Error"])
        return salida["Parse"]
    
    """
        @Override
    """
    def main(self):
        self.homeView.main()
