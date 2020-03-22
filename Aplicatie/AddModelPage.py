import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class AddModelPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Adauga model de masina")
        self.page.place(x=50, y=20, width=200, height=30)
        self.brandLabel = tk.Label(self, text="Marca masina")
        self.brandLabel.place(x=50, y=90, width = 100, height = 30)
        self.brandName = ttk.Combobox(self)
        self.brandName.place(x=170, y=90, width=150, height=30)
        self.modelLabel = tk.Label(self, text="Model masina")
        self.modelLabel.place(x=50, y=130, width = 100, height = 30)
        self.modelName = tk.Entry(self)
        self.modelName.place(x=170, y=130, width=150, height=30)
        self.add = tk.Button(self, text="Adauga", command=lambda: self.addM(self.modelName.get(), self.brandName.get()))
        self.add.place(x=350, y=90, width=50, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)

    def gotoStartPage(self):
        self.brandName.delete(0, 'end')
        self.modelName.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def addM(self, modelName, brandName):
        if modelName is not None:
            try:
                s = "SELECT ID_Marca FROM Marci_Masini WHERE Nume_Marca = '"+brandName+"'"
                self.controller.bdapp.db.cursor.execute(s)
                idBrand = self.controller.bdapp.db.cursor.fetchall()
                s = "INSERT INTO Modele_Masini VALUES (\"model_seq\".NEXTVAL,'"+modelName+"', "+str(idBrand[0][0])+")"
                self.controller.bdapp.db.cursor.execute(s)
                self.controller.bdapp.db.conn.commit()
                self.brandName.delete(0, 'end')
                self.modelName.delete(0, 'end')
                self.controller.show_frame("StartPage")
                Thread(target=createInfoPage, args=("Model adaugat cu succes!",)).start()
            except:
                pass
        else:
            pass