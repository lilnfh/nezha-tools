from modified_tkinter import *
from modified_tkinter.ttk import *
from modified_tkinter import messagebox
import os
import time
import threading
    

class EeyGuard(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        
        # work_duration_minutes
        work_time_label = Label(self, text="Work Time (min):")
        work_time_label.grid(row=0, column=0, padx=10, pady=5)

        work_duration_minutes = IntVar(value=40)
        work_time_entry = Entry(self, textvariable=work_duration_minutes)
        work_time_entry.grid(row=0, column=1, padx=10, pady=5)

        # rest_duration_minutes
        rest_time_label = Label(self, text="Rest Time (min):")
        rest_time_label.grid(row=1, column=0, padx=10, pady=5)

        rest_duration_minutes = IntVar(value=10)
        rest_time_entry = Entry(self, textvariable=rest_duration_minutes)
        rest_time_entry.grid(row=1, column=1, padx=10, pady=5)
        
        thread = threading.Thread(target=self.start_timer, args=(work_duration_minutes.get(),  rest_duration_minutes.get()))
        thread.daemon = True  
        thread.start()
        
    def start_timer(self, work_duration_minutes, rest_duration_minutes):
        start = 0

        while start != -1:
            start += 1   
            if start >= work_duration_minutes*60:
                ret = messagebox.askyesno("Protect your eyes", "Do you want to protect your eyes?")
                if ret:
                    os.system('rundll32.exe user32.dll,LockWorkStation')
                    time.sleep(20)
                    messagebox.showinfo("Info", "Continue Working..." )
                    start = 0
                else:
                    time.sleep(rest_duration_minutes*60)
            time.sleep(1)