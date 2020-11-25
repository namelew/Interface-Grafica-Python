# gera palavras aleatórias
import tkinter
import random 


def gpalavra():
    palavra = list()
    while len(palavra) < 6:
        v = random.sample('aeiou', 1)
        con = random.sample('bcdfghjklmnpqrstvxwz', 1)
        palavra.append(con[0])
        palavra.append(v[0])
    tkinter.Label(main, text=''.join(palavra), font='Times 15').grid()



main = tkinter.Tk()
main.title("Gerador de Palavras")

leg = tkinter.Label(main, text="Gera palavras de forma aleatória.", font='Times 15')
cmd = tkinter.Button(main, text="Gerar", command = gpalavra, font='Times 15')

leg.grid()
cmd.grid()

main.mainloop()