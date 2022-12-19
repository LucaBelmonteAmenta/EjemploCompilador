import string
import tkinter as tk
from tkinter import ttk
from views.View import View
from tkinter import filedialog
import tkinter.scrolledtext as st



"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class HomeView(tk.Tk, View):
    
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
        self.title("Analizador Lexico")
        self.geometry("1220x600")
        self.resizable(width=False, height=False)

        self.cargarLabels()
        self.cargarTextsBox()
        self.cargarButtons()

        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    


    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)
    

    def cargarLabels(self):
      self.label_entrada = ttk.Label(self, text= "Texto de Entrada", font= ('Helvetica 10 bold'))
      self.label_entrada.place(x=20, y=20) 

      self.label_salida = ttk.Label(self, text= "Resultado del Analisis de Lexico", font= ('Helvetica 10 bold'))
      self.label_salida.place(x=420, y=20)

      self.label_salida = ttk.Label(self, text= "Resultado del Analisis de Sintactico", font= ('Helvetica 10 bold'))
      self.label_salida.place(x=820, y=20)


    def cargarTextsBox(self):

        # Text-Box de Entrada:

        self.TextBoxEntrada = tk.Text(self, wrap = tk.NONE)
        self.TextBoxEntrada.place(x=20, y=40, width=370, height=450)

        self.cargarScrolls(self.TextBoxEntrada)

        # Text-Box de Salida del Analisis de lexico:

        self.TextBoxSalidaLexico = tk.Text(self, wrap = tk.NONE)
        self.TextBoxSalidaLexico.place(x=420, y=40, width=380, height=450)

        self.cargarScrolls(self.TextBoxSalidaLexico)

        # Text-Box de Salida del Analisis de sintactico:

        self.TextBoxSalidaSintaxis= tk.Text(self, wrap = tk.NONE)
        self.TextBoxSalidaSintaxis.place(x=820, y=40, width=380, height=450)

        self.cargarScrolls(self.TextBoxSalidaSintaxis)


    def cargarScrolls(self, TextBox):

        ScrollY = tk.Scrollbar(TextBox)
        ScrollY.config(command = TextBox.yview)
        ScrollY.pack(side = tk.RIGHT, fill = tk.Y)

        ScrollX = tk.Scrollbar(TextBox, orient = tk.HORIZONTAL)
        ScrollX.config(command = TextBox.xview)
        ScrollX.pack(side = tk.BOTTOM , fill = tk.X)

        TextBox.config(yscrollcommand = ScrollY.set, xscrollcommand = ScrollX.set)

    
    def cargarButtons(self):

      estilo_boton = ttk.Style()
      estilo_boton.configure('my.TButton', font=('Helvetica 15 bold'))

      self.boton_cargar_archivo = ttk.Button(self)
      self.boton_cargar_archivo.configure(style = 'my.TButton', text = "Cargar Archivo", command = lambda : self.readEntry())
      self.boton_cargar_archivo.place(x=300, y=520, width=160, height=45)

      self.boton_tabla_simbolos = ttk.Button(self)
      self.boton_tabla_simbolos.configure(style = 'my.TButton', text = "Tabla de Simbolos", command = lambda : self.homeController.cargarTablaSimbolos())
      self.boton_tabla_simbolos.place(x=500, y=520, width=200, height=45)

      self.boton_analizar = ttk.Button(self)
      self.boton_analizar.configure(style = 'my.TButton', text = "Analizar", command = lambda : self.analisis())
      self.boton_analizar.place(x=740, y=520, width=160, height=45)


    def setTextBoxContent(self, texbox, contenido):
        
        texbox.delete("1.0","end")
        
        if type(contenido) == string:
            contenido = contenido.strip()
        
        for renglon in contenido:
                texbox.insert(tk.END, renglon)
                if len(renglon) > 1:
                    texbox.insert(tk.END, "\n")


    def getTextBoxContent(self, texbox, lista=True):
        
        contenido = texbox.get("1.0", tk.END)
        
        if lista:
            return contenido.split("\n")
        else:
            return contenido

        
    def readEntry(self):
        
        file = filedialog.askopenfile(mode='r', filetypes=[('Documento de texto', '*.txt')])

        if file:
            contenido_entrada = file.read()
            file.close()
            self.setTextBoxContent(self.TextBoxEntrada, contenido_entrada)


    def getEntry(self):
        return self.getTextBoxContent(self.TextBoxEntrada)


    def analisis(self):

        entrada = self.getEntry()

        resultadoLexico = self.homeController.analisisLexico(entrada)
        self.setTextBoxContent(self.TextBoxSalidaLexico, resultadoLexico)

        resultadosintaxis = self.homeController.analisisSintaxis(resultadoLexico)
        self.setTextBoxContent(self.TextBoxSalidaSintaxis, resultadosintaxis)

        pass



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