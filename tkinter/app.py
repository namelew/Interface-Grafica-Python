import tkinter
root = tkinter.Tk()
root.title("Aplicação")

img = tkinter.PhotoImage(file='imagens/smol.png')
label_imagem = tkinter.Label(root, image=img).grid()

root.mainloop()