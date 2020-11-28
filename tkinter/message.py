import tkinter
# aprendendo a usar message
root = tkinter.Tk()
root.title("Aplicação")
root.geometry('400x300')
# criando a Message
t = tkinter.Message(root, text='Esse é o texto do widget message.', width=200)
t.grid()

root.mainloop()