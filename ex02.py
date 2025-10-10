import tkinter as tk
from random import randint
 
janela = tk.Tk()
janela.title('Exercício 02')
janela.state('zoomed')
# texto da tarefa 
texto = tk.Label(janela, text='Exercício 02- perguntas sobre data de nascimento', font=('Arial',15))
texto.place(x=350, y=50)
def movi():
    y = randint(40, 60)
    texto.place(x=700, y = y) 
    janela.after(200, movi)
movi()  

# fazer os botoes   para salvar 

       
entrada = tk.Entry(janela)
entrada.place(x=800, y=180)
lista_respostas = []
c=  0
def salvar():
    global c  
    valoe = entrada.get()
    lista_respostas.append(valoe)
    print(lista_respostas)

    if c <= 3:
        if c == 0:
            pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format('dia'), font=('Arial', 12))
            pergunta.place(x=750, y=150)
            c += 1

        elif c == 1:
            pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format('mês'), font=('Arial', 12))
            pergunta.place(x=800, y=150)
            c += 1

        elif c == 2:
            pergunta = tk.Label(janela, text='Qual o {} do seu nascimento?'.format('ano'), font=('Arial', 12))
            pergunta.place(x=800, y=150)
            
            c += 1
            
            
        else:
            botão.destroy()
            entrada.destroy()
            pergunta = tk.Label(janela, text='   Você nasceu {}/{}/{}  correto?    '.format(lista_respostas[1], lista_respostas[2], lista_respostas[3]), font=('Arial', 12))
            pergunta.place(x=800, y=150)
            
            
            



salvar()

botão = tk.Button(janela, text='Salvar', font=('Arial',12), command=lambda: [salvar()],)
botão.place(x=820, y=210)


janela.mainloop()
#### FALTA FAZER O BOTÃO SALVAR O RESULKTADO E ADCIONAR UM VALOR A MAIS EM C
# Exercício 02 - Crie um script Python que leia o dia, o mês e 
#fazer interface
#vincular com o botão
#vincular com def
#fazwer a def criar um label mostrando o sesultado ''''