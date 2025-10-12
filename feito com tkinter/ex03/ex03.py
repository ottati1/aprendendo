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

#texto da pergunra
pergunta_txt = tk.Label(janela, text='Digite o primeiro valor', font=('ArialBlack', 12), bg="#ff7f7f")
pergunta_txt.place(x=119 , y=70)
#botão salvar com as funçoes 

def salvar():
    valor = janela_resposta.get()
    lista_calculo.append(valor)
    print(lista_calculo, len(lista_calculo))
    c = 0
    if len(lista_calculo) >= 1:
        if len(lista_calculo) <= 1:
            pergunta_txt.config(text='Digite o segundo valor')
        if len(lista_calculo) >=2:
            pergunta_txt.destroy()
            botao.destroy()
            janela_resposta.destroy()
            valor = tk.Label(janela, text=lista_calculo[0], font=('arial', 12), bg='#ff7f7f')
            valor.place(x=180, y=70)
            valor1 = tk.Label(janela, text=lista_calculo[1], font=('arial', 12), bg='#ff7f7f')
            valor1.place(x=180, y=100)
            mais =  tk.Label(janela, text='+', font=('arial', 12), bg='#ff7f7f')
botao = tk.Button(janela, text='salvar', font=('ArialBlack', 12), bg="#FFFFFF", command=salvar)
botao.place(x=170 , y=120)


janela_resposta.focus()
janela.mainloop()