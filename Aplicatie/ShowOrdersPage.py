import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *


class ShowOrdersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Comenzi finalizate")
        self.page.place(x=30, y=10, width = 140, height = 30)
        self.frame = tk.Frame(self)
        self.frame.place(x=50, y=100, width=450, height=350)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.place(x=0, y=0)
        self.ordersFrame = tk.Frame(self.canvas)
        self.ordersFrame.pack()
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbarx = ttk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.config(xscrollcommand=self.scrollbarx.set)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)

    def gotoStartPage(self):
        for widget in self.ordersFrame.winfo_children():
            widget.destroy()
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")