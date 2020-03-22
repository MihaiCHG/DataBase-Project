import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class RemoveCategoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame(self)
        self.frame.place(x=50, y=20, width=450, height=350)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.place(x=0, y=0)
        self.categoryFrame = tk.Frame(self.canvas)
        self.categoryFrame.pack()
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=420, y=0, width=100, height=30)

    def gotoStartPage(self):
        for widget in self.categoryFrame.winfo_children():
            widget.destroy()
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def deleteCategory(self, category, checkList):
        nrCat = 0
        catWithProd = []
        msg = ""
        for i in range(len(checkList)):
            if checkList[i].get() == 1:
                idCat=category[i][0]
                s = "SELECT ID_Produs FROM produse WHERE ID_Categorie = " + str(idCat)
                self.controller.bdapp.db.cursor.execute(s)
                nrProd = len(self.controller.bdapp.db.cursor.fetchall())
                if nrProd > 0:
                    catWithProd.append(i)
        if len(catWithProd) == 0:
            for i in range(len(checkList)):
                if checkList[i].get() == 1:
                    idCat=category[i][0]
                    try:
                        s = "DELETE FROM categorie WHERE ID_Categorie = " +str(idCat)
                        self.controller.bdapp.db.cursor.execute(s)
                        self.controller.bdapp.db.conn.commit()
                        nrCat += 1
                    except:
                        pass

            self.controller.geometry("520x300")
            self.controller.show_frame("StartPage")
            msg += str(nrCat) + " categorii sterse cu succes!"
        else:
            for x in catWithProd:
                msg += category[x][1]+", "
            msg += " contin produse si nu pot fi sterse!"
            self.controller.geometry("520x300")
            self.controller.show_frame("StartPage")
        for widget in self.categoryFrame.winfo_children():
            widget.destroy()
        Thread(target=createInfoPage, args=(msg,)).start()