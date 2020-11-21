import tkinter

menu_inicial = tkinter.Tk()
menu_inicial.title("Tipos de Bordas")

label_1 = tkinter.Label(
    menu_inicial,
    text='solid',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='solid', # tipo de borda (linha contínua)
).pack()

label_2 = tkinter.Label(
    menu_inicial,
    text='flat',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='flat', # tipo de borda (linha contínua)
).pack()

label_3 = tkinter.Label(
    menu_inicial,
    text='raised',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='raised', # tipo de borda (linha contínua)
).pack()

label_4 = tkinter.Label(
    menu_inicial,
    text='sunken',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='sunken', # tipo de borda (linha contínua)
).pack()

label_5 = tkinter.Label(
    menu_inicial,
    text='ridge',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='ridge', # tipo de borda (linha contínua)
).pack()

label_6 = tkinter.Label(
    menu_inicial,
    text='groove',
    font='Arial 20',
    bd=5, # espessura da borda
    relief='groove', # tipo de borda (linha contínua)
).pack()


menu_inicial.mainloop()