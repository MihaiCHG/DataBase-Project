import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class AddCategoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Adauga categorie de produse")
        self.page.place(x=50, y=20, width=200, height=30)
        self.categoryLabel = tk.Label(self, text="Denumire categorie")
        self.categoryLabel.place(x=50, y=90, width=140, height=30)
        self.category = tk.Entry(self)
        self.category.place(x=200, y=90, width=150, height=30)
        self.add = tk.Button(self, text="Adauga", command=lambda: self.addC(self.category.get()))
        self.add.place(x=370, y=90, width=50, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)

    def gotoStartPage(self):
        self.category.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def addC(self, categoryName):
        try:
            s = "INSERT INTO categorie VALUES (\"category_seq\".NEXTVAL,'"+categoryName+"')"
            self.controller.bdapp.db.cursor.execute(s)
            self.controller.bdapp.db.conn.commit()
            self.category.delete(0, 'end')
            self.controller.show_frame("StartPage")
            Thread(target=createInfoPage, args=("Categorie adaugata cu succes!",)).start()
        except:
            print("Error")