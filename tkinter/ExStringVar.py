import tkinter
# Fazendo o exemplo anterior, mas usando o StringVar()
# - - ----------------------------------------------------------------------------------
# funções
def olah():
    vartexto.set("O seu nome é "+textbox_1.get()) # adiciona o valor do textbox no objeto vartexto
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")
vartexto = tkinter.StringVar()

# ------------------------------------------------------------------------------------
# widget
label_1 = tkinter.Label(root, text='Qual o seu nome?')
textbox_1 = tkinter.Entry(root)
cmd = tkinter.Button(root, text='Executar', command=olah)
label_2 = tkinter.Label(root, textvariable=vartexto)
# ------------------------------------------------------------------------------------
# layout
label_1.grid()
textbox_1.grid()
cmd.grid()
label_2.grid()

root.mainloop()