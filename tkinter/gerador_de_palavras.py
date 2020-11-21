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
    for l in palavra:
        print(l, end='')
    print()


main = tkinter.Tk()
main.title("Gerador de Palavras")

leg = tkinter.Label(main, text="Gera palavras no terminal de forma aleatória.")
cmd = tkinter.Button(main, text="Gerar", command = gpalavra)

leg.pack()
cmd.pack()

main.mainloop()