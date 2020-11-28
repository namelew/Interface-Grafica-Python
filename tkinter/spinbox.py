import tkinter
# Aprendendo a utilizar spinbox 

def executar():
    print(s2.get())


root = tkinter.Tk()
root.geometry('300x200')

s1 = tkinter.Spinbox(root, from_=0, to=10)
s2 = tkinter.Spinbox(
    root,
    values=(10, 20, 30, 40, 50), # valores que podem ser selecionados
    wrap=True # após o ultimo valor, irá retornar ao primeiro(o inverso também é válido)
    )
s3 = tkinter.Spinbox(root, values=('João', 'Maria', 'Carlos'), wrap=True)
cmd = tkinter.Button(root, text='Click', command=executar)

s1.grid()
s2.grid()
s3.grid()
cmd.grid()

root.mainloop()