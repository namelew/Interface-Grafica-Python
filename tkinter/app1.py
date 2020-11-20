import tkinter

menu_inicial = tkinter.Tk()
menu_inicial.title("Primeira app") # altera o título da página

menu_inicial.geometry("500x200+200+200") # altera as dimensões da janela
menu_inicial.resizable(True, True) # altera a redimensionalidade da janela

menu_inicial.minsize(500, 250) # define as dimensões mínimas da página
menu_inicial.maxsize(700, 400) # define as dimensões máximas da página
menu_inicial.state("zoomed") #janela inicial com zoom(tamanho máximo)

menu_inicial.iconbitmap("imagens/icon.ico")

menu_inicial.mainloop() # abre a janela principal