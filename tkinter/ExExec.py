import tkinter
# ------- Lógica ------
def olah():
    nome = text_box.get()
    ola = tkinter.Label(root, text='Olá '+nome+', pra em conhecê-lo!')
    ola.grid()
# -------- GUI --------
root = tkinter.Tk()
root.title("Título da App")
root.geometry('200x100')

# criar os widgets
label1 = tkinter.Label(root, text='Qual o seu nome?')
text_box = tkinter.Entry(root)
button1 = tkinter.Button(root, text='Executar', command=olah)

#organizar os widgets
label1.grid()
text_box.grid()
button1.grid()

root.mainloop()