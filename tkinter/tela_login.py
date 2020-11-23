import tkinter
# Uma tela de login que realmente faz login

# Lógica
def login():
    usuario = text_user.get()
    senha = text_senha.get()
    confirmar = tkinter.Label(root, text='Usuário: '+usuario+' Senha: '+senha+'. Login Concluído com Sucesso', font='Times 15')
    confirmar.grid(row=3, column=1,)


# Gráfico
root = tkinter.Tk()
root.title("Login")

user = tkinter.Label(root, text='Usuário:', font='Times 15')
text_user = tkinter.Entry(root)
senha = tkinter.Label(root, text='Senha:', font='Times 15')
text_senha = tkinter.Entry(root)
cmd_login = tkinter.Button(root, text='Login', command=login)

user.grid(row=0, column=0, sticky='w')
text_user.grid(row=0, column=1, columnspan=2)
senha.grid(row=1, column=0, sticky='w')
text_senha.grid(row=1, column=1)
cmd_login.grid(row=2, column=1, sticky='nswe')

root.mainloop()