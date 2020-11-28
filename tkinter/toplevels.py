import tkinter
# Aprendendo a utilizar toplevels

def abrir_formulario():
    # criando um toplevel
    top = tkinter.Toplevel()
    top.title('Nova Página')
    top.geometry('200x100')
    la1 = tkinter.Label(top, text='Esta é uma nova janela').pack()


root = tkinter.Tk()
root.geometry('300x200')

cmd = tkinter.Button(root, text='Abrir nova janela', command=abrir_formulario)
cmd.pack()

root.mainloop()