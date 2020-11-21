import tkinter

menu_inicial = tkinter.Tk()
menu_inicial.title("Primeira app") # altera o título da página

menu_inicial.geometry("500x200+200+200") # altera as dimensões da janela
menu_inicial.resizable(True, True) # altera a redimensionalidade da janela

menu_inicial.minsize(500, 250) # define as dimensões mínimas da página
menu_inicial.maxsize(700, 400) # define as dimensões máximas da página
menu_inicial.state("zoomed") #janela inicial com zoom(tamanho máximo)

menu_inicial.iconbitmap("imagens/icon.ico")


def cmd_Click(mensagem):
    print(mensagem)


# Criando objetos
cmd = tkinter.Button(menu_inicial, text="Executar", command=lambda:cmd_Click("Nova mensagem"))
label_1 = tkinter.Label(
    menu_inicial,
    text='0123456789',
    bd=1,
    relief='solid',
    font='Arial 20',
    width=10,
    height=5, # altura do label(quantidade de linhas)
    anchor='n' # alinhamento do texto(varia segundo os pontos cardeais)
)

# Pack objetos
label_1.pack()
cmd.pack()

menu_inicial.mainloop() # abre a janela principal