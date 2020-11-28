mport tkinter
# aprendendo a usar scale

# função para o caso do command dentro do scale
# def vervalor(v): # a alocação de valor por parâmetro, no caso da função dentro do widget, é dinâmica
#     print(v)

# função para o exemplo do uso de scale com button
def vervalor():
    print(slide.get())


root = tkinter.Tk()
root.geometry('300x200')

# criando um scale(barra que pode ser movida)

# função funcionando dentro do scale
# slide = tkinter.Scale(
#     root,
#     from_=0, # valor inicial do scale
#     to=100, # valor máximo
#     orient='horizontal', # orientação do scale(pode ser horizontal ou vestical)
#     resolution=0.5, # taxa de variação dos valores
#     command=vervalor
# )

# funcionando por intermédio de um botão
slide = tkinter.Scale(
    root,
    from_=0, # valor inicial do scale
    to=100, # valor máximo
    orient='horizontal', # orientação do scale(pode ser horizontal ou vestical)
    resolution=0.5, # taxa de variação dos valores
)
cmd = tkinter.Button(root, text='Executar', command=vervalor).pack()  
slide.pack()

root.mainloop()