import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *


class CartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame(self)
        self.page = tk.Label(self, text="Cos de cumparaturi")
        self.page.place(x=30, y=10, width = 140, height = 30)
        self.clientLabel = tk.Label(self, text="Nume Client")
        self.clientLabel.place(x=50, y=40, width = 100, height = 30)
        self.clientName = tk.Entry(self)
        self.clientName.place(x=200, y=40, width=150, height=30)
        self.phoneLabel = tk.Label(self, text="Telefon")
        self.phoneLabel.place(x=50, y=80, width = 100, height = 30)
        self.phoneNumber = tk.Entry(self)
        self.phoneNumber.place(x=200, y=80, width=150, height=30)
        self.seriesLabel = tk.Label(self, text="Serie buletin(ex. XT)")
        self.seriesLabel.place(x=50, y=120, width = 130, height = 30)
        self.series = tk.Entry(self)
        self.series.place(x=200, y=120, width=150, height=30)
        self.nrSeriesLabel = tk.Label(self, text="Numar serie")
        self.nrSeriesLabel.place(x=50, y=160, width = 100, height = 30)
        self.nrSeries = tk.Entry(self)
        self.nrSeries.place(x=200, y=160, width=150, height=30)
        self.frame.place(x=50, y=200, width=450, height=350)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.place(x=0, y=0)
        self.prodFrame = tk.Frame(self.canvas)
        self.prodFrame.pack()
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.placeOrder = tk.Button(self, text="Plaseaza Comanda", command=self.createOrder)
        self.placeOrder.place(x=220, y=0, width=120, height=30)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=340, y=0, width=100, height=30)
        self.disconnectB = tk.Button(self, text="Disconnect", command=lambda: controller.bdapp.disconnect(self))
        self.disconnectB.place(x=440, y=0, width=80, height=30)

    def createOrder(self):
        products = self.controller.bdapp.products
        amount = self.controller.bdapp.nrOfProducts
        isok = 1
        msg = ""
        total = 0.0
        idClient = 0
        prodOrder = []
        if len(products) > 0:
            for i in range(len(products)):
                s = "SELECT * From produse WHERE ID_Produs = " + str(products[i])
                self.controller.bdapp.db.cursor.execute(s)
                res = self.controller.bdapp.db.cursor.fetchall()[0]
                stock = res[3]
                if int(amount[i]) <= stock:
                    total += float(int(amount[i])*float(res[2]))
                    prodOrder += res
                else:
                    isok = 0
                    msg += res[1] + ", "
        else:
            isok = -3
            msg = "Cosul nu contine produse"
        if isok == 1:
            if self.clientName.get() == '' or self.phoneNumber.get() == '' or self.series.get() == '' or self.nrSeries.get() == '':
                isok = -1
                msg = "Trebuie completat numele/nr. de telefon/seria/nr. serie!"
        if isok == 1:
            if len(self.phoneNumber.get()) > 10 or len(self.phoneNumber.get())<10:
                isok = -1
                msg = "Numarul de telefon trebuie sa aiba 10 carac."
        if isok == 1:
            if len(self.series.get()) > 2 or len(self.nrSeries.get()) > 6:
                isok = -2
                msg = "Seria trebuie sa aiba max. 2 carac.(ex. XT), numarul de serie trebuie sa aiba 6 carac."
        if isok == 1:
            s = "SELECT * FROM clienti WHERE Nume = '" + self.clientName.get() +"' AND Serie = '"+self.series.get() + "' AND Nr_Serie = '" +self.nrSeries.get()+"'"
            self.controller.bdapp.db.cursor.execute(s)
            res = self.controller.bdapp.db.cursor.fetchall()
            if len(res) > 0:
                isok = 2
                idClient = res[0][0]
        if isok == 1:
            s = "select \"clients_seq\".NEXTVAL from dual"
            self.controller.bdapp.db.cursor.execute(s)
            idClient = self.controller.bdapp.db.cursor.fetchall()[0][0]
            s = "INSERT INTO clienti VALUES ("+str(idClient)+",'"+self.clientName.get()+"', '"+self.phoneNumber.get()+"', '"+self.series.get()
            s += "', '"+self.nrSeries.get()+"')"
            self.controller.bdapp.db.cursor.execute(s)
        if isok == 1 or isok == 2:
            s = "select \"order_seq\".NEXTVAL from dual"
            self.controller.bdapp.db.cursor.execute(s)
            idOrder = self.controller.bdapp.db.cursor.fetchall()[0][0]
            s = "INSERT INTO Comenzi VALUES ("+str(idOrder)+","+str(float(total))+","+str(self.controller.bdapp.id_angajat)+","+str(idClient)+")"
            self.controller.bdapp.db.cursor.execute(s)
            prods = self.controller.bdapp.products
            amount = self.controller.bdapp.nrOfProducts
            for i in range(len(prods)):
                s = "update produse set stock = stock - "+str(amount[i])+" where id_produs = " + str(prods[i])
                self.controller.bdapp.db.cursor.execute(s)
                s = "INSERT INTO Produse_Comenzi VALUES("+str(idOrder)+","+str(prods[i])+","+str(amount[i])+")"
                self.controller.bdapp.db.cursor.execute(s)
            self.controller.bdapp.db.conn.commit()
            self.controller.bdapp.products = []
            self.controller.bdapp.nrOfProducts = []
            msg = "Comanda plasata cu succes!"
        if isok == 0:
            msg += " nu sunt suficient in stock"
        self.phoneNumber.delete(0, 'end')
        self.clientName.delete(0, 'end')
        self.series.delete(0, 'end')
        self.nrSeries.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")
        for widget in self.prodFrame.winfo_children():
            widget.destroy()
        Thread(target=createInfoPage, args=(msg,)).start()


    def gotoStartPage(self):
        for widget in self.prodFrame.winfo_children():
            widget.destroy()
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")