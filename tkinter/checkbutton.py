import tkinter
# utizando checkbutton
def apresentar():
    print(valor_check.get())

root = tkinter.Tk()
root.title("Aplicação")

valor_check = tkinter.IntVar()

check = tkinter.Checkbutton(root,
                            text='Isso é uma checkbox',
                            variable=valor_check,
                            command = apresentar
).pack()

root.mainloop()