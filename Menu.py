import tkinter as tk
from tkinter import filedialog
import P1 as P1
import sys


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Datos")
        self.window.geometry('500x400+600+100')

        btnStart = tk.Button(self.window, text="Start", font=(
            "Agency FB", 14), width=10, command=self.newWindow).place(x=200, y=140)

        btnExit = tk.Button(self.window, text="Exit", bg='red', command=self.window.quit, font=(
            "Agency FB", 14), width=10).place(x=200, y=190)

        self.window.mainloop()

    def fileUpload(self):
        filename = filedialog.askopenfilename(
            initialdir="\ ", title="Select file", filetypes=[("Text files", "*.json")])
        P1.inicio(filename)

    def salir(self):
        sys.exit()

    def newWindow(self):
        # window.withdraw()
        win = tk.Toplevel()
        win.geometry('500x400+600+100')
        win.configure(background='dark turquoise')
        win.title("Valores")

        menubar = tk.Menu(win)
        win.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        editmenu = tk.Menu(menubar)
        helpmenu = tk.Menu(menubar)

        """ Menu de opciones """
        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        menubar.add_cascade(label="Editar", menu=editmenu)

        filemenu.add_cascade(label="File upload", command=self.fileUpload)
        filemenu.add_command(label="Exit", command=win.destroy)

        editmenu.add_command(label="Sorry")


app = Application()
