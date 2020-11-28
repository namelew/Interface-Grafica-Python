import tkinter
# Aprendendo a utilizar menus
 
def fileNewClick():
    print('New File as created')


root = tkinter.Tk()
root.geometry('300x200')
# criando o menu
menu_inicial = tkinter.Menu(root)

# criando um sub menu dentro da opção File
file_menu = tkinter.Menu(
    menu_inicial,
    tearoff=0 # desabilitada a posibilidade de separar o menu da janela principal(0). 1 = default
)
# opções do submenu
file_menu.add_command(label='New', command=fileNewClick) # adicionando um comando
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator() # separador visual
file_menu.add_command(label='Close')
# elo do submenu com o menu principal
menu_inicial.add_cascade(label='File', menu=file_menu)

# Submenu Edit
edit_menu = tkinter.Menu(menu_inicial, tearoff=0)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
menu_inicial.add_cascade(label='Edit', menu=edit_menu)

root.config(menu=menu_inicial) # atreland o menu ao root, 'pack' de um menu

root.mainloop()