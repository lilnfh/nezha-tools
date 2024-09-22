import config
from modified_tkinter import *
from modified_tkinter.ttk import *
from components import HomepageFrame
import time
from tools.eye_guard import EeyGuard


def top(root):
    root.iconify()

def main(): 
    root = Tk()
    root.title('nezha-tools')
    root.config(bg='#eee8d5')
    root.geometry(f"{config.WIDTH}x{config.HEIGHT}")
    
    notebook = Notebook(root)
    homepage = HomepageFrame()
    eyeguard =  EeyGuard()
    notebook.add(homepage, text='Homepage')
    notebook.add(eyeguard, text='EyeGuard')
    notebook.pack(expand=True, fill='both', padx=10, pady=10)

    button1 = Button(homepage, text="Button 1", command=lambda: top(root))
    button1.grid(row=0, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()