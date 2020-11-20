# Funções e Classes
# Usar python -m tkinter no terminal para dar desplay da versão da biblioteca e um
# exemplo de interface
import tkinter

objeto_tk = tkinter.Tk()
# Class tkinter.Tk():
# - Classe principal e contem a página inicial
# - Iniciada sem argumentos

objeto_tk.mainloop()
# Abre a página

objeto_tk.title("Título")
# altera o título da página objeto_tk

objeto_tk.geometry()
# altera as dimensões e posição inicial da página
# recebe uma string "AlturaxLargura+x+y"
# onde AxL, são o tamanho inicial, e x e y, a posição da janela

objeto_tk.resizable()
# altera a redimensionalidade da janela
# parâmetros: altura: none, largura: none (ambos recebem valores booleanos)
# ex: .resizable(False, True), a largura não pode ser alteradam mas a altura sim

objeto_tk.minsize()
# define a dimensões mínima da janela
# dois parâmetros: (largura, altura)

objeto_tk.maxsize()
# define as dimensões máximas da janela
# dois parâmetros: (largura, altura)

objeto_tk.state()
# define o estado inicial da página
# - state("zoomed"): inicial em tamanho máximo
# - state("iconic"): inicial minimizado na barra de tarefas

objeto_tk.iconbitmap()
# substituir o icone padrão por um arquivo .ico
# ex: objeto_tk.iconbitmap("imagens/icon.ico")

botaotk = tkinter.Button(objeto_tk)
# criando um botão que pertence a objeto_tk 'master=objeto_tk'
# Button possui os seguintes atributos:
# - text='': o texto que irá aparecer dentro do botão
# - command='': código que será executado ao apertar o botão
# obs: command deve receber uma função ou um código presedido de 'lambda: codigo'
botaotk.pack()
# mostra o botão na tela

objecto_tcl = tkinter.Tcl()
# Funtion tkinter.Tcl():
# - Substituto do .Tk()
# - Cria um objeto que "ignora" o Tcl interpreter.