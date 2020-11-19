# Funções e Classes
# Usar python -m tkinter no terminal para dar desplay da versão da biblioteca e um
# exemplo de interface
import tkinter
# Class tkinter.Tk():
# - Classe principal e contem a página inicial
# - Iniciada sem argumentos
objeto_tk = tkinter.Tk()
# Abre a página
objeto_tk.mainloop()
# altera o título da página objeto_tk
objeto_tk.title("Título")



# Funtion tkinter.Tcl():
# - Substituto do .Tk()
# - Cria um objeto que "ignora" o Tcl interpreter.
objecto_tcl = tkinter.Tcl()