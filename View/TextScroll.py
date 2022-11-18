from tkinter import *
from tkinter import ttk

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(True)

    # create a Text widget
        self.txt = Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollbY = ttk.Scrollbar(self, orient = 'vertical', command=self.txt.yview)
        scrollbX = ttk.Scrollbar(self, orient = 'horizontal', command=self.txt.xview)
        scrollbX.grid(column = 0, row = 1, sticky = 'we')
        scrollbY.grid(column = 1, row = 0, sticky = 'ns')
        self.txt['yscrollcommand'] = scrollbY.set
        self.txt['xscrollcommand'] = scrollbX.set
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)