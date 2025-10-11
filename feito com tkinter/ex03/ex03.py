##n1 = int(input('digite um valor: '))
##n2 = int(input('digite ouytro valor: '))
#print('a soma entre {} e {} e {}'.format(n1, n2, n1+n2)) esse é o exercicio 
import tkinter as tk 

janela = tk.Tk()
janela.title('Exercício 03')
janela.geometry('800x500')
janela.resizable(False, False)
#icone da janela 
janela.iconbitmap('icone.ico')
texto_ex = tk.Label(janela, text='Exercício 03 ', font=('ArialBlack', 12))
texto_ex.place(x=350, y=30)

janela.mainloop()