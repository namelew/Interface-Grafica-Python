import tkinter
# criando e utilozando listboxs
def executar():
    print(lista.get('active')) # printa no terminal o item que está selecionado
root = tkinter.Tk()
root.title("Aplicação")

lista = tkinter.Listbox(root)
# lista = tkinter.Listbox(root, selectmode='extended')  habilitando seleção de multiplos itens 
lista.pack()

cmd = tkinter.Button(root, text='Click', command=executar).pack()

# inserindo elementos em uma listbox

# usando o index
lista.insert(0, 'Primeiro item da lista')
lista.insert(1, 'Segundo item da lista')
# usando 'END'
lista.insert('end', 'Tercerio item da lista')
lista.insert('end', 'Quarto item da lista')
# inserindo uma list em uma listbox
nomes = ['João', 'Carlos', 'Maradona']
for nome in nomes:
    lista.insert('end', nome)

# eliminando elementos de uma listbox
# lista.delete(0, 'end') apagando todos os elementos da lista
lista.delete(6,6) # eliminando apenas um item
root.mainloop()