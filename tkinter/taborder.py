import tkinter
# configurando tab order
# - - ----------------------------------------------------------------------------------
# funções
def executar():
    label1['text'] = text_1.get()
    label2['text'] = text_2.get()
    label3['text'] = text_3.get()
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")
# ------------------------------------------------------------------------------------
# widget
text_1 = tkinter.Entry(root)
text_2 = tkinter.Entry(root)
text_3 = tkinter.Entry(root)

label1 = tkinter.Label(root)
label2 = tkinter.Label(root)
label3 = tkinter.Label(root)

b = tkinter.Button(root, text='Executar', command=executar)
# ------------------------------------------------------------------------------------
# layout
text_1.grid()
text_2.grid()
text_3.grid()

label1.grid()
label2.grid()
label3.grid()

b.grid()

text_1.focus() # Cursor inicia na textbox 1
# a sequencia de tab é definida pela criação dos widgets

root.mainloop()