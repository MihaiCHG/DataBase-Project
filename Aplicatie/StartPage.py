import tkinter as tk
import tkinter.ttk as ttk


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Bun venit")
        self.label.pack(side="top", fill="x", pady=10)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)
        self.addProd = tk.Button(self, text="Adauga produs")
        self.addProd.place(x=40, y=50, width=120, height=30)
        self.addProd.config(command=self.showAddProdPage)
        self.addBrand = tk.Button(self, text="Adauga marci masini")
        self.addBrand.place(x=180, y=50, width=140, height=30)
        self.addBrand.config(command = lambda: controller.show_frame("AddBrandPage"))
        self.addModels = tk.Button(self, text="Adauga modele masini")
        self.addModels.place(x=340, y=50, width=140, height=30)
        self.addModels.config(command=self.showAddModelPage)
        self.removeProd = tk.Button(self, text="Adauga stock")
        self.removeProd.place(x=40, y=90, width=120, height=30)
        self.removeProd.config(command=self.showAddStockPage)
        self.removeBrands = tk.Button(self, text="Sterge marca masini")
        self.removeBrands.place(x=180, y=90, width=140, height=30)
        self.removeBrands.config(command=self.showRemoveBrandsPage)
        self.removeModels = tk.Button(self, text="Sterge model masini")
        self.removeModels.place(x=340, y=90, width=140, height=30)
        self.removeModels.config(command=self.showRemoveModelsPage)
        self.addCategory = tk.Button(self, text="Adauga categorie")
        self.addCategory.place(x=40, y=130, width=120, height=30)
        self.addCategory.config(command = lambda: controller.show_frame("AddCategoryPage"))
        self.showOrders = tk.Button(self, text="Afiseaza comenzi")
        self.showOrders.place(x=180, y=130, width=140, height=30)
        self.showOrders.config(command=self.showOrdersPage)
        self.createComand = tk.Button(self, text="Creaza comanda", bg="green", fg="white")
        self.createComand.place(x=180, y=170, width=140, height=30)
        self.createComand.config(command=self.showCreateOrderPage)
        self.removeCategory = tk.Button(self, text="Sterge categorie")
        self.removeCategory.place(x=340, y=130, width=140, height=30)
        self.removeCategory.config(command=self.showRemoveCategoryPage)
        self.goToCart = tk.Button(self, text="Cos de cumparaturi", command=lambda: self.controller.frames["CreateOrderPage"].showCart())
        self.goToCart.place(x=320, y=0, width=120, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)

    def showAddProdPage(self):
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Nume_Marca FROM Marci_Masini")
        brands = self.controller.bdapp.db.cursor.fetchall()
        for brand in brands:
            values += brand
        self.controller.frames["AddProdPage"].brands["value"]=values
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Denumire FROM categorie")
        categorys = self.controller.bdapp.db.cursor.fetchall()
        for cat in categorys:
            values += cat
        self.controller.frames["AddProdPage"].category["value"]=values
        self.controller.show_frame("AddProdPage")

    def showAddModelPage(self):
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Nume_Marca FROM Marci_Masini")
        brands = self.controller.bdapp.db.cursor.fetchall()
        for brand in brands:
            values += brand
        self.controller.frames["AddModelPage"].brandName["value"]=values
        self.controller.show_frame("AddModelPage")

    def showAddStockPage(self):
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Nume_Marca FROM Marci_Masini")
        brands = self.controller.bdapp.db.cursor.fetchall()
        for brand in brands:
            values += brand
        self.controller.frames["AddStockPage"].brands["value"]=values
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Denumire FROM categorie")
        categorys = self.controller.bdapp.db.cursor.fetchall()
        for cat in categorys:
            values += cat
        self.controller.frames["AddStockPage"].category["value"]=values
        self.controller.geometry("520x600")
        self.controller.show_frame("AddStockPage")

    def showRemoveCategoryPage(self):
        s = "SELECT ID_Categorie, Denumire FROM categorie"
        self.controller.bdapp.db.cursor.execute(s)
        res = self.controller.bdapp.db.cursor.fetchall()
        checkList = []
        y = 0
        frame = self.controller.frames["RemoveCategoryPage"]
        for cat in res:
            text = cat[1]
            label = tk.Label(frame.categoryFrame, text=text)
            label.grid(row=y, column=0)
            var = tk.IntVar()
            ckbutton = tk.Checkbutton(frame.categoryFrame, variable=var)
            ckbutton.grid(row=y, column=1)
            y += 1
            checkList.append(var)
        deleteButton = tk.Button(frame, text="Sterge categoriile bifate", command=lambda: frame.deleteCategory(res,checkList))
        deleteButton.place(x=200, y=440, width=150, height=30)
        self.controller.geometry("520x500")
        self.controller.show_frame("RemoveCategoryPage")

    def showRemoveBrandsPage(self):
        s = "SELECT * FROM Marci_Masini"
        self.controller.bdapp.db.cursor.execute(s)
        res = self.controller.bdapp.db.cursor.fetchall()
        checkList = []
        y = 0
        frame = self.controller.frames["RemoveBrandsPage"]
        for cat in res:
            text = cat[1]
            label = tk.Label(frame.brandsFrame, text=text)
            label.grid(row=y, column=0)
            var = tk.IntVar()
            ckbutton = tk.Checkbutton(frame.brandsFrame, variable=var)
            ckbutton.grid(row=y, column=1)
            y += 1
            checkList.append(var)
        deleteButton = tk.Button(frame, text="Sterge marcile bifate", command=lambda: frame.deleteBrands(res,checkList))
        deleteButton.place(x=200, y=440, width=150, height=30)
        self.controller.geometry("520x500")
        self.controller.show_frame("RemoveBrandsPage")

    def showRemoveModelsPage(self):
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Nume_Marca FROM Marci_Masini")
        brands = self.controller.bdapp.db.cursor.fetchall()
        for brand in brands:
            values += brand
        self.controller.frames["RemoveModelsPage"].brands["value"]=values
        self.controller.geometry("520x600")
        self.controller.show_frame("RemoveModelsPage")

    def showCreateOrderPage(self):
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Nume_Marca FROM Marci_Masini")
        brands = self.controller.bdapp.db.cursor.fetchall()
        for brand in brands:
            values += brand
        self.controller.frames["CreateOrderPage"].brands["value"]=values
        values = []
        self.controller.bdapp.db.cursor.execute("SELECT Denumire FROM categorie")
        categorys = self.controller.bdapp.db.cursor.fetchall()
        for cat in categorys:
            values += cat
        self.controller.frames["CreateOrderPage"].category["value"]=values
        self.controller.geometry("520x600")
        self.controller.show_frame("CreateOrderPage")

    def showOrdersPage(self):
        try:
            y = 0
            frame = self.controller.frames["ShowOrdersPage"]
            for widget in frame.ordersFrame.winfo_children():
                widget.destroy()
            s = "SELECT ID_Comanda, Total, ID_Angajat, ID_Client from Comenzi"
            self.controller.bdapp.db.cursor.execute(s)
            orders = self.controller.bdapp.db.cursor.fetchall()
            for i in range(len(orders)):
                s = "SELECT Nume, Serie, Nr_Serie, Telefon FROM Clienti WHERE ID_Client = " + str(orders[i][3])
                self.controller.bdapp.db.cursor.execute(s)
                client = self.controller.bdapp.db.cursor.fetchall()[0]
                s = "SELECT Nume,Data_angajare FROM Angajati WHERE ID_Angajat = " + str(orders[i][2])
                self.controller.bdapp.db.cursor.execute(s)
                employee = self.controller.bdapp.db.cursor.fetchall()[0]
                text = str(client[0]) + ", Telefon: " + str(client[3])+", Serie: " + str(client[1]+"("+str(client[2]+"), Total: "+str(orders[i][1])+" ron, Angajat: "+str(employee[0])))
                label = tk.Label(frame.ordersFrame, text=text)
                label.grid(row=y, column=0)
                s = "SELECT ID_Produs, Cantitate FROM Produse_Comenzi WHERE ID_Comanda = " + str(orders[i][0])
                self.controller.bdapp.db.cursor.execute(s)
                prods = self.controller.bdapp.db.cursor.fetchall()
                y += 1
                for j in range(len(prods)):
                    amount = prods[j][1]
                    s = "SELECT Denumire, Pret FROM produse WHERE ID_Produs = " + str(prods[j][0])
                    self.controller.bdapp.db.cursor.execute(s)
                    prod = self.controller.bdapp.db.cursor.fetchall()[0]
                    s = "SELECT ID_Produs, ID_Model FROM compatibilitati WHERE ID_Produs = " +str(prods[j][0])
                    self.controller.bdapp.db.cursor.execute(s)
                    idModel = self.controller.bdapp.db.cursor.fetchall()[0]
                    s = "SELECT Nume_Model, ID_Marca FROM Modele_Masini WHERE ID_Model = " +str(idModel[1])
                    self.controller.bdapp.db.cursor.execute(s)
                    model = self.controller.bdapp.db.cursor.fetchall()[0]
                    s = "SELECT Nume_Marca FROM Marci_Masini WHERE ID_Marca = " +str(model[1])
                    self.controller.bdapp.db.cursor.execute(s)
                    brand = self.controller.bdapp.db.cursor.fetchall()[0]
                    text = "-----"+str(prod[0]) + "("+str(brand[0])+","+str(model[0])+ "), Pret: " + str(prod[1]) + " ron, Cantite:" + str(amount)
                    label = tk.Label(frame.ordersFrame, text=text)
                    label.grid(row=y, column=0)
                    y += 1
                label = tk.Label(frame.ordersFrame, text="")
                label.grid(row=y, column=0)
                y += 1
            self.controller.geometry("520x600")
            self.controller.show_frame("ShowOrdersPage")
        except:
            pass