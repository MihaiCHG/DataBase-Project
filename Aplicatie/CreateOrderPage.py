import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class CreateOrderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Creaza comanda")
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
        self.search = tk.Button(self, text="Search", command=self.updateListProd)
        self.search.place(x=360, y=80, width=50, height=30)
        self.frame = tk.Frame(self)
        self.frame.place(x=50, y=160, width=450, height=350)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.place(x=0, y=0)
        self.prodFrame = tk.Frame(self.canvas)
        self.prodFrame.pack()
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=220, y=0, width=100, height=30)
        self.goToCart = tk.Button(self, text="Cos de cumparaturi", command=self.showCart)
        self.goToCart.place(x=320, y=0, width=120, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)

    def gotoStartPage(self):
        for widget in self.prodFrame.winfo_children():
            widget.destroy()
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
        self.model["value"]=values

    def updateListProd(self):
        try:
            for widget in self.prodFrame.winfo_children():
                widget.destroy()
            brand = self.brands.get()
            model = self.model.get()
            category = self.category.get()
            if brand is not None and model is not None and category is not None:
                s = "SELECT ID_Marca FROM Marci_Masini WHERE Nume_Marca = '"+brand+"'"
                self.controller.bdapp.db.cursor.execute(s)
                idBrand = self.controller.bdapp.db.cursor.fetchall()[0][0]
                s = "SELECT ID_Model FROM Modele_Masini WHERE Nume_Model = '"+model+"' AND ID_Marca = "+str(idBrand)+""
                self.controller.bdapp.db.cursor.execute(s)
                idModel = self.controller.bdapp.db.cursor.fetchall()[0][0]
                self.controller.bdapp.db.cursor.execute("SELECT ID_Categorie FROM categorie WHERE Denumire = '"+category+"'")
                idCategory = self.controller.bdapp.db.cursor.fetchall()[0][0]
                y = 0
                s = "SELECT ID_Produs FROM compatibilitati WHERE ID_Model = "+str(idModel)+""
                self.controller.bdapp.db.cursor.execute(s)
                res = self.controller.bdapp.db.cursor.fetchall()
                list = []
                for prod in res:
                    list += prod
                res = []
                for x in list:
                    s = "SELECT ID_Produs, Denumire, Pret, Stock FROM produse WHERE ID_Produs = " + str(x) +" AND ID_Categorie = "+ str(idCategory)+""
                    self.controller.bdapp.db.cursor.execute(s)
                    res += self.controller.bdapp.db.cursor.fetchall()
                checkList = []
                amountList = []
                for prod in res:
                    text = prod[1]+", Pret: "+str(prod[2])+" ron, Stock: "+str(prod[3])
                    label = tk.Label(self.prodFrame, text=text)
                    label.grid(row=y, column=0)
                    var = tk.IntVar()
                    ckbutton = tk.Checkbutton(self.prodFrame, variable=var)
                    ckbutton.grid(row=y, column=1)
                    entry = tk.Entry(self.prodFrame)
                    entry.grid(row=y, column=2)
                    y += 1
                    amountList.append(entry)
                    checkList.append(var)
                addButton = tk.Button(self, text="Adauga produsele bifate", command=lambda: self.addProd(res,checkList, amountList))
                addButton.place(x=360, y=540, width=150, height=30)
        except:
            pass

    def addProd(self, prods, checkList, amountList):
        nrProd = 0
        isok = 1
        msg = ""
        for i in range(len(checkList)):
            if checkList[i].get() == 1:
                idProd=prods[i][0]
                try:
                    if amountList[i].get() != '' and int(amountList[i].get()) > 0:
                        self.controller.bdapp.products.append(idProd)
                        self.controller.bdapp.nrOfProducts.append(amountList[i].get())
                        nrProd += int(amountList[i].get())
                    else:
                        isok = 0
                except:
                    pass
        self.brands.delete(0, 'end')
        self.model.delete(0, 'end')
        self.category.delete(0, 'end')
        for widget in self.prodFrame.winfo_children():
            widget.destroy()
        if isok == 1:
            msg += str(nrProd) + " produse adaugate in cos cu succes!"
        else:
            msg += "Trebuie sa intruduci si cantitatea!"
        Thread(target=createInfoPage, args=(msg,)).start()

    def showCart(self):
        try:
            y = 0
            frame = self.controller.frames["CartPage"]
            prods = self.controller.bdapp.products
            for widget in frame.prodFrame.winfo_children():
                widget.destroy()
            for i in range(len(prods)):
                s = "SELECT * FROM produse WHERE ID_Produs = " + str(prods[i])
                self.controller.bdapp.db.cursor.execute(s)
                prod = self.controller.bdapp.db.cursor.fetchall()[0]
                amount = self.controller.bdapp.nrOfProducts
                text = str(prod[1]) + ", Pret: " + str(prod[2])+" ron, Cantite:" + str(amount[i])
                label = tk.Label(frame.prodFrame, text=text)
                label.grid(row=y, column=0)
                ckbutton = tk.Button(frame.prodFrame, text="Sterge", command=lambda: self.deleteProd(i))
                ckbutton.grid(row=y, column=1)
                y += 1
            self.controller.geometry("520x600")
            self.controller.show_frame("CartPage")
        except:
            pass

    def deleteProd(self, index):
        print(index)
        del self.controller.bdapp.products[index]
        del self.controller.bdapp.nrOfProducts[index]
        self.showCart()
