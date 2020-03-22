import tkinter as tk
import tkinter.ttk as ttk
import sys, os
sys.path.append(os.getcwd())
from InfoPage import *
from threading import *

class RemoveModelsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = tk.Label(self, text="Sterge model")
        self.page.place(x=50, y=10, width=200, height=30)
        self.brandLabel = tk.Label(self, text="Marca")
        self.brandLabel.place(x=50, y=40, width = 100, height = 30)
        self.brands = ttk.Combobox(self)
        self.brands.place(x=170, y=40, width=150, height=30)
        self.search = tk.Button(self, text="Search", command=self.updateListModels)
        self.search.place(x=360, y=40, width=50, height=30)
        self.frame = tk.Frame(self)
        self.frame.place(x=50, y=80, width=450, height=350)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.place(x=0,y=0)
        self.modelsFrame = tk.Frame(self.canvas)
        self.modelsFrame.pack()
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.goStartPage = tk.Button(self, text="Pagina principala", command=self.gotoStartPage)
        self.goStartPage.place(x=420, y=0, width=100, height=30)

    def gotoStartPage(self):
        for widget in self.modelsFrame.winfo_children():
            widget.destroy()
        self.brands.delete(0, 'end')
        self.controller.geometry("520x300")
        self.controller.show_frame("StartPage")

    def updateListModels(self):
        try:
            for widget in self.modelsFrame.winfo_children():
                widget.destroy()
            brand = self.brands.get()
            if brand is not None:
                s = "SELECT ID_Marca FROM Marci_Masini WHERE Nume_Marca = '"+brand+"'"
                self.controller.bdapp.db.cursor.execute(s)
                idBrand = self.controller.bdapp.db.cursor.fetchall()[0][0]
                y=0
                res = []
                s = "SELECT * FROM Modele_Masini WHERE ID_Marca = " +str(idBrand)
                self.controller.bdapp.db.cursor.execute(s)
                res += self.controller.bdapp.db.cursor.fetchall()
                checkList = []
                for model in res:
                    text = str(model[1])
                    print(text)
                    label = tk.Label(self.modelsFrame, text=text)
                    label.grid(row=y, column=0)
                    var = tk.IntVar()
                    ckbutton = tk.Checkbutton(self.modelsFrame, variable=var)
                    ckbutton.grid(row=y, column=1)
                    y += 1
                    checkList.append(var)
                deleteButton = tk.Button(self, text="Sterge modelele bifate", command=lambda: self.deleteModels(res,checkList))
                deleteButton.place(x=360, y=540, width=150, height=30)
        except:
            pass

    def deleteModels(self, models, checkList):
        nrModels=0
        msg = ""
        modelWithProd = []
        for i in range(len(checkList)):
            if checkList[i].get() == 1:
                idModel=models[i][0]
                s = "SELECT * FROM compatibilitati WHERE ID_Model = " + str(idModel)
                self.controller.bdapp.db.cursor.execute(s)
                nrProd = len(self.controller.bdapp.db.cursor.fetchall())
                if nrProd > 0:
                    modelWithProd.append(i)
        if len(modelWithProd) == 0:
            for i in range(len(checkList)):
                if checkList[i].get() == 1:
                    idModel=models[i][0]
                    try:
                        s = "DELETE FROM Modele_Masini WHERE ID_Model = " +str(idModel)
                        self.controller.bdapp.db.cursor.execute(s)
                        self.controller.bdapp.db.conn.commit()
                        nrModels += 1
                    except:
                        pass

            self.controller.geometry("520x300")
            self.controller.show_frame("StartPage")
            msg += str(nrModels) + " modele sterse cu succes!"
        else:
            for x in modelWithProd:
                msg += models[x][1]+", "
            msg += " contin produse si nu pot fi sterse!"
            self.controller.geometry("520x300")
            self.controller.show_frame("StartPage")
        for widget in self.modelsFrame.winfo_children():
            widget.destroy()
        Thread(target=createInfoPage, args=(msg,)).start()