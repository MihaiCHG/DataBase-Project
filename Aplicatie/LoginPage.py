import tkinter as tk
import tkinter.ttk as ttk

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.geometry("300x150")
        self.text = tk.StringVar()
        self.text.set("Conectare(nume angajat)")
        self.auth = tk.Label(self, textvariable=self.text)
        self.auth.grid(row=0, column=1, pady=10)

        self.labelName = tk.Label(self, text="Nume")
        self.labelName.grid(row=1, column=0)
        self.name = tk.Entry(self)
        self.name.grid(row=1, column=1)

        self.loginButton = tk.Button(self, text="Login", command=lambda: controller.bdapp.login(self, self.name.get()))
        self.loginButton.grid(row=3, column=1)
