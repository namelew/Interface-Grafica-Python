import tkinter
# apredendo a utilizar frames
# - - ----------------------------------------------------------------------------------
# funções
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")
# ------------------------------------------------------------------------------------
# widget
frame_login = tkinter.Frame(root) # criando a frame
# atribuindo widgets a frame
usuario = tkinter.Label(frame_login, text='Usuário:')
password = tkinter.Label(frame_login, text='Senha:')
text_user = tkinter.Entry(frame_login)
text_pass = tkinter.Entry(frame_login)
b_entrar = tkinter.Button(frame_login, text='Entrar')
# ------------------------------------------------------------------------------------
# layout
usuario.grid(row=0, column=0)
password.grid(row=1, column=0)
text_user.grid(row=0, column=1)
text_pass.grid(row=1, column=1)
b_entrar.grid(row=2, column=1)

frame_login.grid() # inserindo a frame dentro de root

root.mainloop()