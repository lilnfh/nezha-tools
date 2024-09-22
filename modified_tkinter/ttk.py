from tkinter import ttk

class Notebook(ttk.Notebook):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


class Frame(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

class Button(ttk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

class Label(ttk.Label):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)