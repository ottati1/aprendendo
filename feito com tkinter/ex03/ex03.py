##n1 = int(input('digite um valor: '))
##n2 = int(input('digite ouytro valor: '))
#print('a soma entre {} e {} e {}'.format(n1, n2, n1+n2)) esse é o exercicio 
import tkinter as tk 
import random as rd
lista_calculo = []
janela = tk.Tk()
janela.title('Exercício 03')
janela.geometry('400x500')
janela.resizable(False, False)
janela.configure(bg='#FF7F7F')
#icone da janela 
janela.iconbitmap('icone.ico')
texto_ex = tk.Label(janela, text='Exercício 03 ', font=('ArialBlack', 12), bg='#FF7F7F')
texto_ex.place(x=150, y=30)
def movi():
    x = rd.randint(100, 200)
    y = rd.randint(15, 45)
    texto_ex.place(x=150, y=y)
    texto_ex.after(300, movi)
movi()
janela_resposta = tk.Entry(janela)
janela_resposta.place(x= 135, y=90)
#botão salvar com as funçoes 
def salvar():
    valor = janela_resposta.get()
    lista_calculo.append(valor)
    print(lista_calculo)



botao = tk.Button(janela, text='salvar', font=('ArialBlack', 12), bg="#FFFFFF", command=salvar)
botao.place(x=170 , y=120)


janela_resposta.focus()
janela.mainloop()