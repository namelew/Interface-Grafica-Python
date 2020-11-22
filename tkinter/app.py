import tkinter
# criando um layout de uma tela de login com tkinter
root = tkinter.Tk()
root.title("Login")
# criando labels estáticos
tkinter.Label(root, text='Usuário:').grid(row=0, sticky='w')
tkinter.Label(root, text='Senha:').grid(row=1, sticky='w')
#adiconando textboxs
text_usuario = tkinter.Entry(root).grid(row=0, column=1)
text_senha = tkinter.Entry(root).grid(row=1, column=1)

cmd_login = tkinter.Button(root, text='Login').grid(row=2, column=1, sticky='e')

root.mainloop()