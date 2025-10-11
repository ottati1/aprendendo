##n1 = int(input('digite um valor: '))
##n2 = int(input('digite ouytro valor: '))
#print('a soma entre {} e {} e {}'.format(n1, n2, n1+n2)) esse é o exercicio 
import tkinter as tk 
import random as rd

janela = tk.Tk()
janela.title('Exercício 03')
janela.geometry('400x500')
janela.resizable(False, False)
#icone da janela 
janela.iconbitmap('icone.ico')
texto_ex = tk.Label(janela, text='Exercício 03 ', font=('ArialBlack', 12))
texto_ex.place(x=150, y=30)
def movi():
    x = rd.randint(100, 200)
    y = rd.randint(15, 45)
    texto_ex.place(x=x, y=y)
    texto_ex.after(300), movi)
movi()


janela.mainloop()