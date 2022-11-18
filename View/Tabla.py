from tkinter import *
from tkinter import ttk

class TableFrame(ttk.Frame):
    
    def __init__(self, tabla_simbolos, root = NONE):
        
        super().__init__(root)
        self.root = root
    
        self.config(width=700, height=1000)    
        self.grid(row=0)

        self.crear_tabla_simbolos()

        for simbolo in tabla_simbolos:
            lexema = simbolo["lexema"]
            token = simbolo["token"]
            if simbolo["palabra reservada"]:
                palabraReservada = "Si"
            else:
                palabraReservada = "No"
            self.cargar_simbolo_en_tabla(lexema, token, palabraReservada)

    def crear_tabla_simbolos(self):

        self.tabla = ttk.Treeview(self, columns=('#1','#2'))
        self.tabla.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 4)

        self.tabla.column("#0", anchor = CENTER, width=180)
        self.tabla.column("#1", anchor = CENTER, width=180)
        self.tabla.column("#2", anchor = CENTER, width=180)

        self.tabla.heading("#0", text = "Lexemas", anchor = CENTER)
        self.tabla.heading("#1", text = "Tokens", anchor = CENTER)
        self.tabla.heading("#2", text = "Es una palabra reservada", anchor = CENTER)

    def cargar_simbolo_en_tabla(self, lexema, token, palabraReservada):
        valores = (token, palabraReservada)
        self.tabla.insert(parent = "" , index = 'end', text = lexema, values = valores)