import tkinter as tk
from random import randint
 
janela = tk.Tk()
janela.title('Exercício 02')
janela.state('zoomed')
# texto da tarefa 
texto = tk.Label(janela, text='Exercício 02- perguntas sobre data de nascimento', font=('Arial',15))
texto.place(x=400, y=50)
def movi():
    y = randint(40, 60)
    texto.place(x=700, y = y) 
    janela.after(200, movi)
movi() 

# fazer os botoes para salvar 
c = 0
if c < 3:
    list = ['dia', 'mês',  'ano']
    if c= 0:
    pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format(list[c]), font=('Arial',12))
    pergunta.place(x=800, y=150)
    entrada = tk.Entry(janela)
    entrada.place(x=800, y=180)
    botão = tk.Button(janela, text='Salvar', font=('Arial',12))
    if c == 2:
        pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format(list[c]), font=('Arial',12))
    if c == 3:
        pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format(list[c]), font=('Arial',12))

    print(list[c])

janela.mainloop()

# Exercício 02 - Crie um script Python que leia o dia, o mês e o
#fazer interface
#vincular com o botão
#vincular com def
#fazwer a def criar um label mostrando o sesultado ''''