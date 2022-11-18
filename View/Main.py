import sys
from FileName import direccion_carpeta_archivo as path
direccion_carpeta_Model = path(False, "Controller")
sys.path.append(direccion_carpeta_Model)

from AnalizadorLexico import Lexico
from FileAccess import FileAccess


from tkinter import filedialog
from tkinter import ttk
from tkinter import *

from TextScroll import TextScrollCombo
from Tabla import TableFrame


class AnalizadorLexicoUI():

   def __init__(self):
      
      self.ventana_principal = Tk()
      self.ventana_principal.title("Analizador Lexico")
      self.ventana_principal.geometry("820x600")
      self.ventana_principal.resizable(width=False, height=False)

      self.cargarLabels()
      self.cargarTextScrolls()
      self.cargarButtons()



   def run(self):
      self.ventana_principal.mainloop()

   
   def cargarButtons(self):

      estilo_boton = ttk.Style()
      estilo_boton.configure('my.TButton', font=('Helvetica 15 bold'))

      self.boton_cargar_archivo = ttk.Button(self.ventana_principal)
      self.boton_cargar_archivo.configure(style = 'my.TButton', text = "Cargar Archivo", command = self.buscar_archivo_entrada)
      self.boton_cargar_archivo.place(x=100, y=520, width=160, height=45)

      self.boton_tabla_simbolos = ttk.Button(self.ventana_principal)
      self.boton_tabla_simbolos.configure(style = 'my.TButton', text = "Tabla de Simbolos", command = self.abrir_tabla_simbolos)
      self.boton_tabla_simbolos.place(x=300, y=520, width=200, height=45)

      self.boton_analizar = ttk.Button(self.ventana_principal)
      self.boton_analizar.configure(style = 'my.TButton', text = "Analizar", command = self.analizarEntrada)
      self.boton_analizar.place(x=540, y=520, width=160, height=45)


   def cargarLabels(self):
      
      self.label_entrada = ttk.Label(self.ventana_principal, text= "Texto de Entrada", font= ('Helvetica 10 bold'))
      self.label_entrada.place(x=20, y=20)

      self.label_salida = ttk.Label(self.ventana_principal, text= "Texto de Salida", font= ('Helvetica 10 bold'))
      self.label_salida.place(x=420, y=20)


   def cargarTextScrolls(self):
      
      self.text_entrada = TextScrollCombo(self.ventana_principal)
      self.text_entrada.place(x=20, y=40, width=380, height=450)
      self.text_entrada.txt.config(font=("consolas", 12), undo=True, wrap='word')
      self.text_entrada.txt.config(borderwidth=3, relief="sunken")

      self.text_salida = TextScrollCombo(self.ventana_principal)
      self.text_salida.place(x=420, y=40, width=380, height=450)
      self.text_salida.txt.config(font=("consolas", 12), undo=True, wrap='word')
      self.text_salida.txt.config(borderwidth=3, relief="sunken")


   def abrir_tabla_simbolos(self):
      self.ventana_tabla_simbolos = Toplevel(self.ventana_principal)
      self.ventana_tabla_simbolos.resizable(width=False, height=False)
      self.ventana_tabla_simbolos.title("Tabla de Simbolos")
      simbolos = FileAccess().lista_simbolos_json(True)
      self.frameTabla = TableFrame(simbolos, self.ventana_tabla_simbolos)


   def buscar_archivo_entrada(self):
      file = filedialog.askopenfile(mode='r', filetypes=[('Documento de texto', '*.txt')])
      self.direccion_archivo = file
      if file:
         contenido_entrada = file.read()
         file.close()
         self.text_entrada.txt.delete("1.0","end")
         self.text_entrada.txt.insert(END, contenido_entrada.strip())


   def analizarEntrada(self):
      self.codigo_entrada = self.text_entrada.txt.get("1.0", END)
      self.codigo_entrada = self.codigo_entrada.split("\n")
      contador_lineas = 0
      self.text_salida.txt.delete("1.0","end")

       

      analisis_lineas = []

      for linea in self.codigo_entrada:

         contador_lineas += 1
         analisis_linea = Lexico().analizarLinea(linea, contador_lineas)
         print(analisis_linea)
         analisis_lineas.append(str(analisis_linea))
         self.text_salida.txt.insert(END, str(analisis_linea).strip())

      direccion_nuevo_archivo = path(False, "\Salida.txt")
      file = open(direccion_nuevo_archivo, 'w')
      file.writelines(analisis_lineas)
      file.close()
      
      




if __name__ == "__main__":
   AnalizadorLexicoUI([]).run()