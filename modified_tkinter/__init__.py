import tkinter as tk

class Tk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    def geometry(self, geometry=None):
        if geometry == None:
            return super().geometry(self)
        
        self.center_window(geometry)

    def center_window(self, geometry):
        # get width and height of the window from this format: 800x600+560+240
        width, height = map(int, geometry.split('+')[0].split('x'))
        
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate window position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # set the window position
        super().geometry(f'{width}x{height}+{x}+{y}')

class IntVar(tk.IntVar):
    def __init__(self, master=None, value=None, name=None):
        super().__init__(master, value, name)

class Entry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)