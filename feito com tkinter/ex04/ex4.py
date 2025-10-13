import tkinter as tk 
import time as tempo
import winsound as som
#cor da janela padrão
cor_janela = '#727070'
fonte_padrão = 'arial', 12, 'bold'
def teste():
    print('deu certo')
def escrita():
    texto = 'Exercício 04'
    lista = list(texto)
    texto_final = ''

    for c in range(len(lista)):
        texto_final += lista[c]
        texto_entrada.config(text=texto_final)
        janela.update()
        #som.Beep(100, 10)
        tempo.sleep(0.1)
        
#janela 
janela = tk.Tk()
janela.title('Exercício 04')
janela.geometry('700x800')

janela.resizable(False, False)
janela.iconbitmap('icones/icone.ico')
janela.config(background=cor_janela)

#texto de explicação de exercicio (quero que ele entre digitando com som de teclado)
texto_entrada = tk.Label(
    janela,
    text='', 
    font=(fonte_padrão), 
    bg=cor_janela
)
texto_entrada.place(x= 290, y=15)
janela.after(1000, escrita)

texto_funcao = tk.Label(
    janela,  
    text='Escreva algo', 
    font=(fonte_padrão), 
    bg=cor_janela)

texto_funcao.place(x=300, y=60)
#onde vou digitar
botao = tk.Button(
    janela,
    text='Verificar',
    font=(fonte_padrão),
    bg='#ffffff',
    cursor='hand2',
    width=7,
    height=0,
    command=teste
)
botao.place(x=450 , y=85)
enviar = tk.Entry(
    janela,
    width=30
    
)

enviar.place(x=250, y=90)
#comeca já podendo digitar
enviar.focus()
#vincula o botão enter com o botao enviar
janela.bind('<Return>', teste)
janela.mainloop()
# o programa tem que me dizer se oque foi digitado é 
#variavel e qual variavel 
#se só tem espaço
#é um número
#é uma letra 
# e maiuscula ou minuscula 
# a primeira letra e maiuscula ? 
# faazer isso em loop e que cada vez que eu faça um novo atualize
# se possivel criar um historico doque já foi pesquisado com uma haba onde eu possa acessar import tkinter as tk 
