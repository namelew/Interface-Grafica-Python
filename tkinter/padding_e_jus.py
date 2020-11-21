import tkinter

menu_inicial = tkinter.Tk()
menu_inicial.title("Padding e Justificação")

largurat = menu_inicial.winfo_screenwidth()
alturat = menu_inicial.winfo_screenheight()
posx = largurat/2 - 500/2
posy = alturat/2 - 500/2
menu_inicial.geometry('500x500+%d+%d'%(posx,posy))

label_1 = tkinter.Label(
    menu_inicial,
    text='Texto Label 1',
    font='Arial 20',
    bd=1,
    relief='solid',
    padx=5, # padding horizontal
    pady=5  #padding vestical
)

label_2 = tkinter.Label(
    menu_inicial,
    text='Texto Label 2\nOutra Frase\nÚltima frase',
    font='Arial 20',
    bd=1,
    width=50,
    height=5,
    relief='solid',
    anchor='w',
    justify='center' # justificando ao centro
)

label_1.pack()
label_2.pack()
menu_inicial.mainloop()