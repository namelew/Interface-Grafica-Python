import tkinter
# Aprendendo a utilizar 
class A(tkinter.Frame):
    def __init__(self, master):
        super().__init__()
        self.valor_a = tkinter.IntVar() # Variável que armazena o value das opções
        label = tkinter.Label(self, text='Grupo A').pack()
        ra_1 = tkinter.Radiobutton(
            self, # master
            text='Opção A1', # texto
            variable=self.valor_a, # objeto que irá armazenar os valores, também é o elo de ligação entre eles
            value=1, # valor que será armazenado quando ele for selecionado
            command=self.raf1, # associando funções a radiobuttons
            indicatoron=0 # muda a aparência do radiobutton(0 = sunken, 1 = default)
        )
        ra_2 = tkinter.Radiobutton(self, text='Opção A2', variable=self.valor_a, value=2, indicatoron=0)
        ra_3 = tkinter.Radiobutton(self, text='Opção A3', variable=self.valor_a, value=3, indicatoron=0)
        cmd = tkinter.Button(self, text='Gerar(A)', command=self.ver_radio)
        ra_1.pack()
        ra_2.pack()
        ra_3.pack()
        cmd.pack()
        ra_1.select() # opção que será escolida por "default" 
    def ver_radio(self):
        print(self.valor_a.get())
    def raf1(self):
        print('Opção 1')

class B(tkinter.Frame):
    def __init__(self, master):
        super().__init__()
        self.valor_b = tkinter.IntVar()
        label = tkinter.Label(self, text='Grupo B').pack()
        ra_1 = tkinter.Radiobutton(self, text='Opção 1B', variable=self.valor_b, value=1)
        ra_2 = tkinter.Radiobutton(self, text='Opção 2B', variable=self.valor_b, value=2)
        ra_3 = tkinter.Radiobutton(self, text='Opção 3B', variable=self.valor_b, value=3)
        cmd = tkinter.Button(self, text='Gerar(B)', command=self.ver_radio)
        ra_1.pack()
        ra_2.pack()
        ra_3.pack()
        cmd.pack()
    def ver_radio(self):
        print(self.valor_b.get())

root = tkinter.Tk()

# Grupo Radiobuttons A
grupo_a = A(root)
grupo_a.pack()

# Grupo Radiobuttons B
grupo_b = B(root)
grupo_b.pack()

root.mainloop()