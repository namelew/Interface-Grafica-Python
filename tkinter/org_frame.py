import tkinter
# organizando e trabalhando com duas frames
# - - ----------------------------------------------------------------------------------
# funções
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")
# ------------------------------------------------------------------------------------
# widget
frame_nome = tkinter.Frame(root)
frame_end = tkinter.Frame(root)

label_nome = tkinter.Label(frame_nome, text='Nome:')
label_sobren = tkinter.Label(frame_nome, text='Sobrenome:')
label_rua = tkinter.Label(frame_end, text='Rua:')
label_cidade = tkinter.Label(frame_end, text='Cidade:')

text_nome = tkinter.Entry(frame_nome)
text_sobren = tkinter.Entry(frame_nome)
text_rua = tkinter.Entry(frame_end)
text_cidade = tkinter.Entry(frame_end)

cmd_salvar = tkinter.Button(root, text='Salvar')
# ------------------------------------------------------------------------------------
# layout
label_nome.grid(row=0, column=0)
label_sobren.grid(row=1, column=0)
text_nome.grid(row=0, column=1)
text_sobren.grid(row=1, column=1)

label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

frame_nome.grid(row=0, column=0)
frame_end.grid(row=0, column=1)

cmd_salvar.grid()

root.mainloop()