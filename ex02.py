import tkinter as tk
from random import randint
lista = []


janela = tk.Tk()
janela.title('Exercício 02')
janela.state('zoomed')
# texto da tarefa 
texto = tk.Label(janela, text='Exercício 02- perguntas sobre data de nascimento', font=('Arial',15))
texto.place(x=800, y=50)
def movi():
    y = randint(40, 60)
    texto.place(x=800, y = y) 
    janela.after(1000, movi)
movi() 

# fazer os botoes para salvar 
while True:
    pergunta 

janela.mainloop()

# Exercício 02 - Crie um script Python que leia o dia, o mês e o
#fazer interface
#vincular com o botão
#vincular com def
#fazwer a def criar um label mostrando o sesultado ''''