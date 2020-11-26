# gera palavras aleatórias
import tkinter
import random 

class GerarPalavras(tkinter.Frame):
    def __init__(self, parent):
        super().__init__()
        self['width'] = 300
        self['height'] = 250
        self['bg'] = 'blue'
    
        label1 = tkinter.Label(self, text="Gera palavras de forma aleatória.", font='Times 15', bg='green').grid()
        cmd = tkinter.Button(self, text="Gerar", command = self.gpalavra, font='Times 15', bg='purple').grid()

    def gpalavra(self):
        palavra = list()
        while len(palavra) < 6:
            v = random.sample('aeiou', 1)
            con = random.sample('bcdfghjklmnpqrstvxwz', 1)
            palavra.append(con[0])
            palavra.append(v[0])
        tkinter.Label(self, text=''.join(palavra), font='Times 15', bg='green').grid()


main = tkinter.Tk()
main.title("Gerador de Palavras")

objeto1 = GerarPalavras(main).grid()
objeto2 = GerarPalavras(main).grid()

main.mainloop()