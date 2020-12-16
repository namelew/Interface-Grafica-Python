from tkinter import *

inst = Tk()

label = Label(inst, text='Label 1')
label.pack(side=LEFT) # ponto de onde ele vai começar a monstrar na tela(esqueda)

label2 = Label(inst, text='Label 2')
label2.pack(side=RIGHT) # alem desses existem também button e top(padrão)

inst.mainloop()