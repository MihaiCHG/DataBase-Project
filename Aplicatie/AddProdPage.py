import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *

class AddProdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Adauga produs")
        self.page.place(x=50, y=10, width=200, height=30)
        self.brandLabel = tk.Label(self, text="Marca")
        self.brandLabel.place(x=50, y=40, width = 100, height = 30)
        self.brands = ttk.Combobox(self)
        self.brands.place(x=170, y=40, width=150, height=30)
        self.brands.bind('<<ComboboxSelected>>', self.updateModels)
        self.modelLabel = tk.Label(self, text="Model")
        self.modelLabel.place(x=50, y=80, width = 100, height = 30)
        self.model = ttk.Combobox(self)
        self.model.place(x=170, y=80, width=150, height=30)
        self.categoryLabel = tk.Label(self, text="Categorie")
        self.categoryLabel.place(x=50, y=120, width = 100, height = 30)
        self.category = ttk.Combobox(self)
        self.category.place(x=170, y=120, width=150, height=30)
        self.nameLabel = tk.Label(self, text="Denumire produs")
        self.nameLabel.place(x=50, y=160, width = 100, height = 30)
        self.nameProd = tk.Entry(self)
        self.nameProd.place(x=170, y=160, width=150, height=30)
        self.priceLabel = tk.Label(self, text="Pret")
        self.priceLabel.place(x=50, y=200, width=80, height=30)
        self.price = tk.Entry(self)
        self.price.place(x=170, y=200, width=150, height=30)
        self.stockLabel = tk.Label(self, text="Stock")
        self.stockLabel.place(x=50, y=240, width=80, height=30)
        self.stock = tk.Entry(self)
        self.stock.place(x=170, y=240, width=150, height=30)
        self.add = tk.Button(self, text="Adauga", command=self.addP)
        self.add.place(x=350, y=160, width=50, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)

    def gotoStartPage(self):
        self.nameProd.delete(0, 'end')
        self.price.delete(0, 'end')
        self.stock.delete(0, 'end')
        self.brands.delete(0, 'end')
        self.model.delete(0, 'end')
        self.category.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def updateModels(self, event=None):
        values = []
        brand = self.brands.get()
        s = "SELECT mod.Nume_Model FROM Modele_Masini mod, Marci_Masini brand  WHERE "
        s += "mod.ID_Marca=brand.ID_Marca AND brand.Nume_Marca='"+brand+"'"
        self.controller.bdapp.db.cursor.execute(s)
        models = self.controller.bdapp.db.cursor.fetchall()
        for model in models:
            values += model
        self.controller.frames["AddProdPage"].model["value"]=values

    def addP(self):
        brand = self.brands.get()
        model = self.model.get()
        prodName = self.nameProd.get()
        price = self.price.get()
        stock = self.stock.get()
        category = self.category.get()
        if float(price) > 0.0 and int(stock) > 0 and brand is not None and model is not None:
            try:
                s = "SELECT ID_Marca FROM Marci_Masini WHERE Nume_Marca = '"+brand+"'"
                self.controller.bdapp.db.cursor.execute(s)
                idBrand = self.controller.bdapp.db.cursor.fetchall()
                s = "SELECT ID_Model FROM Modele_Masini WHERE Nume_Model = '"+model+"' AND ID_Marca = "+str(idBrand[0][0])+""
                self.controller.bdapp.db.cursor.execute(s)
                idModel = self.controller.bdapp.db.cursor.fetchall()
                self.controller.bdapp.db.cursor.execute("SELECT ID_Categorie FROM categorie WHERE Denumire = '"+category+"'")
                idCategory = self.controller.bdapp.db.cursor.fetchall()
                s = "INSERT INTO produse VALUES (\"product_seq\".NEXTVAL, '"+prodName+"',"
                s += str(price)+","+str(stock)+","+str(idCategory[0][0])+")"
                self.controller.bdapp.db.cursor.execute(s)
                self.controller.bdapp.db.conn.commit()
                s = "SELECT ID_Produs FROM Produse WHERE Denumire = '"+prodName+"'"
                self.controller.bdapp.db.cursor.execute(s)
                idProd = self.controller.bdapp.db.cursor.fetchall()
                s = "INSERT INTO compatibilitati VALUES("+str(idModel[0][0])+","+str(idProd[0][0])+")"
                self.controller.bdapp.db.cursor.execute(s)
                self.controller.bdapp.db.conn.commit()
                self.brands.delete(0, 'end')
                self.model.delete(0, 'end')
                self.nameProd.delete(0, 'end')
                self.price.delete(0, 'end')
                self.stock.delete(0, 'end')
                self.category.delete(0, 'end')
                self.controller.show_frame("StartPage")
                Thread(target=createInfoPage, args=("Produs adaugat cu succes!",)).start()
            except:
                pass
        else:
            pass
