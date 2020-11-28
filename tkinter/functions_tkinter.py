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
# - image = armzana um objeto que armazena uma imagem
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

label.focus()
# Relacionado ao tab order, define qual vai ser a primeira caixa de texto que irá receber uma entrada por padão

imagem = tkinter.PhotoImage(file='imagens/smol.png')
# armzane uma imagem .png dentro da variável imagem e a transforma em um objeto de PhotoImage()

valor = tkinter.IntVar()
# criação de um objeto IntVar() responsável por guardar valores inteiros provenientes de widgets.

check = tkinter.Checkbutton(objeto_tk, variable = valor)
# é um botão que gera um retorno booleano(0, 1), dever ser associado a um objeto IntVar() mas possue os mesmos atributos de um button comum(inclusive o command)
# Atributos:
# - master: mesmo coisa dos outros
# - variable = variavel que receberá o valor bool, 0 ou 1. Normalmente é um objeto IntVar()

lista = tkinter.Listbox(objeto_tk)
# listbox são como 'listas' visiveis, ela monstram na tela opções que podem ser armazenadas dentro delas.
# Atributos:
# - master = mesmo dos outros
# - selectmode = alterna o modo de seleção de elementos
# obs: os modos de seleção são: 'extended'(Mútipla seleção)

lista.insert(0, '1')
# embora só recebão valores string, podemos adicionar infinitos elementos dentro dela
# parâmetros:
# index = valor número que define onde o valor será adicionado(usar 'end' para funcionar como o .append())

lista.delete(0,0)
# apaga um ou vários valores da listbox, o primeiro número é de onde ele vai começar e o segundo será o ultimo valor a ser apagado.
# para apagar todo o conteúdo dela, usar listbox.delete(0, 'end')

mensagem = tkinter.Message(objeto_tk, text='Essa é uma Message', width=200)
# parecido com um label, mas com uma organização mais 'agradável'
# atributos(Basicamente os mesmos dos Labels(Não repetirei os já citados):
# - master, text, width: os atributos principais da message e os que mais serão alterados

scale = tkinter.Scale(objeto_tk, from_=0, to=100)
# scale é uma barra a qual o usuário pode interagir. Pode receber comandos, funções, dentro dele ou ter seus valores atrelados a um button. Mais detalhes no arquivo scale.py.
# Atributos:
# - master = mesmo de sempre
# - from_ = valor mínimo do scale
# - to = valor máximo do scale
# - resolution = taxa de variação dos valores
# - orient = disposição do scale na tela(pode ser vestical ou horizontal, devem ser referenciados como strings)
# - command = armazena uma função que será executada conforme a variação dos valores

v1 = tkinter.IntVar()
ra1 = tkinter.Radiobutton(objeto_tk, text='Exemplo RadioButton', variable=v1, value=1)
# radiobuttons são widgets parecidos com checkboxs, mas que retornão valores diferentes de valores bool.
# Elas podem conter funções e necessitam de um objeto que faça um elo entre elas, no exemplo se está usando o v1. Mais informações me radiobutton.py
# Atributos:
# - master = mesmo de sempre
# - text = mais do mesmo
# - variable = objeto que armazenará o valor que será retornado pelo widget
# - value = valor que será retornado por ele ao ser selecionado
# - command = mais do mesmo
# - indicatoron = aparência do radiobutton
# Obs 1: Os tipos de aparências definidas pelo indicatoron são: 0(sunken(on), raised(off)), 1(default)

ra1.select()
# faz com que esse radiobutton seja o padrão a ser selecionado. Util quano trabalhar com vários.

s = tkinter.Spinbox(objeto_tk, values=('Um', 2, 3.0, 'Four'))
# spinbox, são parecidos com as entrys, mais possuem valores pré definidos pelos quais o usuário pode navegar. Devesse tomar cuidado com a entrada, pois o usuário pode alterar os valore padrões. 
# mais detalhes em spinbox.py
# Atributos:
# - master = mais do mesmo
# - from_, to = mesmos do scale
# - values = tupla que contem os valores pré definidos(pode conter n valores de n tipos)
# - wrap = permite que ao passar do ultimo(ou primeiro valor) a seleção volte ao inicio(ou ao fim).

menu = tkinter.Menu(root, tearoff=0)
menu.add_command(label='Opção 1')
# Menus são estruturas que se adaptão ao S.O do cliente, e armazenam opções e funções
# são muito úteis e versáteis dentro de uma aplicação, mais detalhes no arquivo menu.py
# Atributos:
# master = mais do mesmo(pode ser um menu também)
# tearoff = permite que o menu possa sair da tela em que ele se encontra. 0 = desabilitar, 1 = default
# obs 1: para criar um elo entre um menu e um submenu se usa menu.add_cascade(label='File', menu=submenu) 

menu.add_separator() 
# cria um separador visual entre as opções que estão antes e depois dele

menu.add_command(label='Opção 1')
# adiciona uma nova opção ao menu

objeto_tk.config(menu)
# coloca na janela o menu

objeto2 = tkinter.Toplevel()
# um toplevel é uma outra página atrelada a página principal, fazer todas as funções da principal e receber os mesmos atributos. Além de poder ser atrelada a uma  ou mais funções
objeto2.title('Nova página')
label2 = tkinter.Label(objeto2, text='Label do TopLevel').pack()

objecto_tcl = tkinter.Tcl()
# Funtion tkinter.Tcl():
# - Substituto do .Tk()
# - Cria um objeto que "ignora" o Tcl interpreter.