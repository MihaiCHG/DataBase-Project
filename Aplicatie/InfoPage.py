import tkinter as tk
import tkinter.ttk as ttk

class InfoPage(tk.Tk):
    def __init__(self, message, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("350x200")
        self.info = tk.Label(self, text=message)
        self.info.grid(row=0, column=1, columnspan=3)
        self.exit = tk.Button(self, text="Exit", command=quit)
        self.exit.grid(row=1, column = 3)

def createInfoPage(message):
    root = InfoPage(message)
    root.mainloop()
