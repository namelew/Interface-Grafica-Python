import tkinter
# - - ----------------------------------------------------------------------------------
# Criando um widget personalizado
class FrameNome(tkinter.Frame): # fiz a classe herdar os atributas da superclasse Frame
    def __init__(self, master): # construtor da classe
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = 'solid'

        label_nome = tkinter.Label(self, text='Nome:')
        tex_nome = tkinter.Entry(self)
        label_nome.grid(row=0, column=0)
        tex_nome.grid(row=0, column=1)
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")
# utilizando o novo widget FrameNome()
frame_1 = FrameNome(root).grid()
frame_2 = FrameNome(root).grid()
frame_3 = FrameNome(root).grid()
frame_4 = FrameNome(root).grid()

root.mainloop()