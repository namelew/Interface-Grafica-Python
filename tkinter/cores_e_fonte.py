import tkinter

menu_inicial = tkinter.Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x300")
# inserindo elementos no label
label_1 = tkinter.Label(menu_inicial,
                        text='Este é o label 1',
                        bg='white', # background
                        fg='black', # cor da letra
                        font='Arial') # fonte
label_1.pack()

label_2 = tkinter.Label(menu_inicial,
                        text='Este é o label 2',
                        font='Arial 20 bold italic') # alterando tamanho e tipo
label_2.pack()

label_3 = tkinter.Label(menu_inicial,
                        text='Este é o label 3',
                        font='Verdana 15 italic') # alterando tamanho e tipo
label_3.pack()

menu_inicial.mainloop()