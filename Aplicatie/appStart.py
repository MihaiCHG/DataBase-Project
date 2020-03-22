import sys, os
sys.path.append(os.getcwd())
from LoginPage import *
from StartPage import *
from AddProdPage import *
from AddBrandPage import *
from AddCategoryPage import *
from AddModelPage import *
from RemoveModelsPage import *
from RemoveCategoryPage import *
from AddStockPage import *
from RemoveBrandsPage import *
from CreateOrderPage import *
from CartPage import *
from ShowOrdersPage import *
from dbConnection import *


class bdApp:
    def __init__(self):
        self.db = Connection("bdt" , "bdt")
        self.id_angajat = 0
        self.products = []
        self.nrOfProducts = []
        self.app = SampleApp(self)
        self.app.mainloop()

    def login(self, page, name):
        self.db.cursor.execute("SELECT ID_ANGAJAT, NUME FROM angajati WHERE NUME = '"+name+"'")
        rez = self.db.cursor.fetchall()
        if len(rez) == 1:
            self.id_angajat = rez[0][0]
            page.controller.show_frame("StartPage")
            page.controller.geometry("520x300")
        else:
            page.text.set("Nume gresit!")
            page.controller.show_frame("LoginPage")

    def disconnect(self, page):
        self.id_angajat = 0
        self.app.frames["LoginPage"].text.set("Conectare(nume angajat")
        self.app.frames["LoginPage"].name.delete(0, 'end')
        page.controller.geometry("300x150")
        page.controller.show_frame("LoginPage")


class SampleApp(tk.Tk):

    def __init__(self, bdapp, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.bdapp = bdapp
        self.title("Tema baza de date")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, StartPage, AddProdPage, AddBrandPage, AddModelPage, AddCategoryPage, AddStockPage, RemoveCategoryPage, RemoveBrandsPage, RemoveModelsPage, CreateOrderPage, CartPage, ShowOrdersPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    bd = bdApp()