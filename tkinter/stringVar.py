import tkinter
# Utilizando StringVar e armazenando no atributo textvariable
menu_inicial = tkinter.Tk()
menu_inicial.title("App 1")
menu_inicial.geometry("500x500")

texto = tkinter.StringVar() # criando o objeto StringVar()
texto.set('Novo Texto') # inserindo um valor a ele

label_1 = tkinter.Label(
    menu_inicial,
    font='Arial 20',
    padx=3,
    pady=3,
    bd=1,
    relief='solid',
    bg='blue',
    fg='white',
    textvariable=texto
)

label_1.pack()

label_2 = tkinter.Label(
    menu_inicial,
    font='Arial 20',
    padx=3,
    pady=3,
    bd=1,
    relief='solid',
    bg='blue',
    fg='white',
    textvariable=texto
)

label_2.pack()

label_3 = tkinter.Label(
    menu_inicial,
    font='Arial 20',
    padx=3,
    pady=3,
    bd=1,
    relief='solid',
    bg='blue',
    fg='white',
    textvariable=texto
)

label_3.pack()

label_4 = tkinter.Label(
    menu_inicial,
    font='Arial 20',
    padx=3,
    pady=3,
    bd=1,
    relief='solid',
    bg='blue',
    fg='white',
    textvariable=texto
)

label_4.pack()

texto.set("Diogo Cunha")

menu_inicial.mainloop()