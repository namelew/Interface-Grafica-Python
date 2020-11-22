import tkinter
# utilizando grid
menu_inicial = tkinter.Tk()
menu_inicial.title("App")

label1 =tkinter.Label(menu_inicial, text='Label 1', bg='red', font='Arial 20', fg='white')
label2 =tkinter.Label(menu_inicial, text='Label 2', bg='green',font='Arial 20', fg='white')
label3 =tkinter.Label(menu_inicial, text='Label 3', bg='blue',font='Arial 20', fg='white')

btn1= tkinter.Button(menu_inicial, text='Click 1')
btn2= tkinter.Button(menu_inicial, text='Click 2')
btn3= tkinter.Button(menu_inicial, text='Click 3')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

menu_inicial.mainloop()