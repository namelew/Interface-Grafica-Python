import tkinter
# criando um layout de uma tela de login com tkinter
root = tkinter.Tk()
root.title("Login")

tkinter.Label(root, width=20, bg='red').grid(column=0)
tkinter.Label(root, width=20, bg='green').grid(column=1)
tkinter.Label(root, width=40, bg='blue').grid(columnspan=2, sticky='we') # define que ele vai ocupar 2 colunas

root.mainloop()