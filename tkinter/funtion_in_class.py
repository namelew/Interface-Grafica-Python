import tkinter
# - - ----------------------------------------------------------------------------------
# esse programa é uma demonstração de como implementar uma função interna dentro de uma subclasse
class MinhaFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__()
        self.text1_text = tkinter.StringVar()
        self.label1_text = tkinter.StringVar() 
        # widget
        self.label1 = tkinter.Label(self, textvariable=self.label1_text).grid()
        entry = tkinter.Entry(self, textvariable=self.text1_text).grid()
        cdm1= tkinter.Button(self, text='Click', command=self.executar).grid()

    def executar(self):
        self.label1_text.set('Você digitou ' + self.text1_text.get() + '.')
# ---------------------------------------------------------------------------------------
# GUI
root = tkinter.Tk()
root.title("Aplicação")

frame = MinhaFrame(root).grid()

root.mainloop()