import tkinter

main = tkinter.Tk()
main.title("Título")

# dimensões da janela
largura = 750
altura = 450

# resolução do sistema
largura_screen = main.winfo_screenwidth()
altura_screen = main.winfo_screenheight()

# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir o geometry
main.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))# janela centralizada

main.mainloop()