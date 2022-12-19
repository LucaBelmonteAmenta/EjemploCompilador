# -*- encoding:utf-8 -*-
from controllers.Controller import Controller
from core.FileAccess import FileAccess

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class TablaSimbolosController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    
    
    def __init__(self):
        self.homeView = self.loadView("TablaSimbolos")
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    

    def GetListSimbolos(self):
        accesoArchivos = FileAccess()
        listaSimbolos = accesoArchivos.ReservedWordsList("all attributes")
        return listaSimbolos



    """
        @Override
    """
    def main(self):
        self.homeView.main()
