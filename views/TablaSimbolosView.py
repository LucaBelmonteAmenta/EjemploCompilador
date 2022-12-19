from views.View import View
from tkinter import ttk
import tkinter as tk


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class TablaSimbolosView(tk.Tk, View):
    
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    
    PAD = 10
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------


    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        
        super().__init__()
        self.homeController = controller
        self.title("Tabla de simbolos")
        self.resizable(width=False, height=False)
        
        self.NewTable()
        self.LoadScroll(self.tabla)
        simbolos = self.homeController.GetListSimbolos()
        self.SetSimbolos(simbolos)

    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------


    def NewTable(self):

        self.tabla = ttk.Treeview(self, columns=('#1','#2'))
        
        
        self.tabla.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 4, rowspan = 1)
        self.tabla.config(height=20)

        self.tabla.column("#0", anchor = tk.CENTER, width=180)
        self.tabla.column("#1", anchor = tk.CENTER, width=180)
        self.tabla.column("#2", anchor = tk.CENTER, width=180)

        self.tabla.heading("#0", text = "Lexemas", anchor = tk.CENTER)
        self.tabla.heading("#1", text = "Tokens", anchor = tk.CENTER)
        self.tabla.heading("#2", text = "Es una palabra reservada", anchor = tk.CENTER)


    def LoadScroll(self, tabla):

        ScrollY = tk.Scrollbar(self)
        ScrollY.config(command = tabla.yview)
        ScrollY.grid(column=4, row=0, sticky='NS')
        tabla.config(height=100, yscrollcommand= ScrollY.set)


    def SetSimbolos(self, simbolos):

        for simbolo in simbolos:
            lexema = simbolo["lexema"]
            token = simbolo["token"]
            if simbolo["palabra reservada"]:
                palabraReservada = "Si"
            else:
                palabraReservada = "No"
            self.SetSimbolo(lexema, token, palabraReservada)


    def SetSimbolo(self, lexema, token, palabraReservada):
        
        valores = (token, palabraReservada)
        self.tabla.insert(parent = "" , index = 'end', text = lexema, values = valores)



    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return

