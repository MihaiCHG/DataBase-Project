import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class AddBrandPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Adauga marca de masina")
        self.page.place(x=50, y=20, width=200, height=30)
        self.brandLabel = tk.Label(self, text="Marca masina")
        self.brandLabel.place(x=50, y=90, width = 100, height = 30)
        self.brand = tk.Entry(self)
        self.brand.place(x=170, y=90, width=150, height=30)
        self.add = tk.Button(self, text="Adauga", command=lambda: self.addB(self.brand.get()))
        self.add.place(x=350, y=90, width=50, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)

    def gotoStartPage(self):
        self.brand.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def addB(self, brandName):
        if brandName is not None:
            try:
                s = "INSERT INTO Marci_Masini VALUES (\"brand_seq\".NEXTVAL,'"+brandName+"')"
                self.controller.bdapp.db.cursor.execute(s)
                self.controller.bdapp.db.conn.commit()
                self.brand.delete(0, 'end')
                self.controller.show_frame("StartPage")
                Thread(target=createInfoPage, args=("Marca adaugata cu succes!",)).start()
            except:
                pass
        else:
            pass