import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
import P1 as P1


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Datos")
        self.window.geometry('500x400+600+100')
        self.window.configure(background='lavender')

        btnStart = tk.Button(self.window, text="Start", font=(
            "Agency FB", 14), width=10, command=self.newWindow).place(x=200, y=140)

        btnExit = tk.Button(self.window, text="Exit", bg='red', command=self.window.quit, font=(
            "Agency FB", 14), width=10).place(x=200, y=190)

        self.window.mainloop()

    def fileUpload(self):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=[("Text files", "*.json")])
        # filename = filedialog.askopenfilename(initialdir="\ ", title="Select file", filetypes=[("Text files", "*.json")])
        P1.inicio(filename)

    def loadDates(self):
        def enviardatos():
            li = (int(val1.get()), int(val2.get()))
            print(li)
            P1.delNode(li)

        # mb.showinfo(message="Dates load", title="Error")
        win = tk.Toplevel()
        win.geometry('300x200+700+200')
        win.configure(background='azure')
        win.title("Coordinates")

        lb1 = tk.Label(win, text="Value X", bg="black", fg="white")
        lb1.pack(padx=5, pady=4, ipadx=5, ipady=5)
        val1 = tk.Entry(win)
        val1.pack(padx=3, pady=3, ipadx=3, ipady=3)

        lb2 = tk.Label(win, text="Value Y", bg="red", fg="white")
        lb2.pack(padx=5, pady=5, ipadx=5, ipady=5)
        val2 = tk.Entry(win)
        val2.pack(padx=3, pady=3, ipadx=3, ipady=3)

        btSend = tk.Button(win, text="Load", fg="blue",
                           command=enviardatos)
        btSend.pack(side=tk.TOP)

    def newWindow(self):
        # window.withdraw()
        win = tk.Toplevel()
        win.geometry('500x400+600+100')
        win.configure(background='azure')
        win.title("Valores")

        menubar = tk.Menu(win)
        win.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        delNode = tk.Menu(menubar)
        editmenu = tk.Menu(menubar)
        showmenu = tk.Menu(menubar)

        """ Menu de opciones """
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Delete Nodo", menu=delNode)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Show", menu=showmenu)

        filemenu.add_cascade(label="File upload", command=self.fileUpload)
        filemenu.add_command(label="Exit", command=win.destroy)

        delNode.add_cascade(label="Load Dates", command=self.loadDates)

        editmenu.add_command(label="Sorry")

        showmenu.add_cascade(label="Show Tree", command=P1.mostrar)


app = Application()
