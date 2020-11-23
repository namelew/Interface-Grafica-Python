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

botaotk = tkinter.Button(objeto_tk, text='Exemplo de Botão')
# criando um botão que pertence a objeto_tk 'master=objeto_tk'
# Button possui os seguintes atributos:
# - text='': o texto que irá aparecer dentro do botão
# - command='': código que será executado ao apertar o botão
# obs: command deve receber uma função ou um código presedido de 'lambda: codigo'

botaotk.pack()
# mostra o botão na tela

label = tkinter.Label(objeto_tk, text='Exemplo de Label')
# Label's são texto que podem ser inseridos na janela e não tem interação com o usuário
# ele possui os atributos
# - master = página que pertence
# - text = texto do label(Não consegue armazenar um valor de um objeto StringVar())
# - bg = cor de fundo(background)
# - fg = cor da letra 
# - font = estilo das letras
# - width = largura da janela do label(implica no tamanho do texto)
# - height = altura do label(quantidade de frases que podem ser colocadas dentro dele)
# - anchor = alinhamento da página(varia segundo os pontos cardiais)
# - justify = justifica o texto(não altera a posição do texto dentro do label)
# - padx = adiciona pixeis de padding entre o texto e a borda horizontal
# - pady = adiciona pixeis de padding entre o texto e a borda vestical
# - bd = espessura da borda.
# - relief = tipo da borda.
# - textvariable = armazena um valor de um objeto atrelado a classe StringVar()
# obs 1: sintaxe de font: font='%tipo_da_letra %tamanho %estilo da letra %estilo adicional(se houver)'
# obs 2: bg e fg aceitam o sistema hexadecimal de cores RGB
# obs 3: existe 6 tipos de relief(mais informações no arquivo bordas.py):
#       - solid
#       - flat
#       - raised
#       - sunked
#       - ridge
#       - groove
# obs 4: pontos cardiais para o anchor: 'n'(norte), 's'(sul), 'e'(leste), 'w'(oeste),
# 'ne'(nordeste), 'nw'(noroeste), 'se'(sudeste), 'sw'(sudoeste) e 'center'(centro).
# obs 5: comandos aceitos pelo justify(): 'center', 'left', 'right' 

label.pack()
# mostra o label na tela
# o comando pack() cuida de monstrar os elementos na tela
# a ordem de apresentação dos elementos e definidas pela ordem dos packs()'s

texto = tkinter.StringVar()
# A Classe StringVar() cria uma variável que pode armazenar textos que podem ser utilizandos dentro de widgets
texto.set("Texto de teste")
# armazena uma string dentro do objeto da classe StringVar()

label.grid(row=0, column=0)
# Grid() é a função responsável por exibir um elemento com uma formatação diferente da padrão do pack.
# Ele funciona através de um sistema matricial que começa com a linha e coluna 0 e vai até a n, onde cada coordenada é um ponto da janela.
# sintaxe: elemento.grid(row=n, column=n)
# atributos:
# - row = index da linha, vai de 0 a n
# - column = index da coluna, vai de 0 a n
# - sticky = alinhamento(estilo rosas dos vendos, mesmo formato dos outros)
# - columnspan = define quantas colunas o widget vai ocupar

caixa_de_texto = tkinter.Entry(objeto_tk).grid(row=0, colmn=1)
# Caixas de Texto(Entry):
# Permite ao usuário inserir um texto no sistema
# Atributos:
# - master: página onde será hospedada. No exemplo é objeto_tk.

objecto_tcl = tkinter.Tcl()
# Funtion tkinter.Tcl():
# - Substituto do .Tk()
# - Cria um objeto que "ignora" o Tcl interpreter.