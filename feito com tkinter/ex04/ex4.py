import tkinter as tk 
import time as tempo
import winsound as som
#cor da janela padrão
cor_janela = '#727070'
fonte_padrão = 'arial', 12, 'bold'
#janela 
janela = tk.Tk()
janela.title('Exercício 04')
janela.geometry('700x800')
janela.resizable(False, False)
janela.iconbitmap('icones/icone.ico')
janela.config(background=cor_janela)
#faz funcionar o enter
def funcao1(a):
    funcao()
#funcao principal
tela = tk.Label(
        janela,
        text='',
        font=('arial', 12, 'bold'),
        width=40,
        height=20,
        relief='ridge'
    )
tela.place(x=160, y=140)
listag = []
def funcao():
    lista = enviar.get()
    listag.append(lista)
    #qual variavel
    if lista.isdigit():
            lista= int(lista)
            a3 = 'Sim'
            a4 = 'Não'
    else:
            lista = str(lista)
            a3 = 'Não'
            a4 = 'Sim'
    a1 = list(str(type(lista))) 
    #espaço
    a2 = str(lista) 
    if a2 == ' ' or a2.isspace == True:
            a2 = 'Sim'
    else:
            a2 = 'Não' 
    if a3 =='Sim':
            a5 = 'Não é uma letra'
    else:
            a5 = lista.islower()
            if a5 == True:
                a5 = 'É minusculo'
            else:
                a5 = 'É maiusculo'
    if a4 == 'Sim':
            a6 = str(lista)
            a6 = lista.isupper()
            if a6 == True:
                a6 = 'Sim'
    else:
            a6 ='Não'
                    
    tela.config(text='*Qual variavel é {}{}{}\n *Esta vaziu?  {}\n *É um número? {}\n *É uma letra? {}\n *{}\n *A primeira letra é maiuscula? {}'
                    .format(a1[8], a1[9], a1[10], a2, a3, a4, a5, a6))
    enviar.delete(0, tk.END)
    janela.after(100000, funcao)
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
            
def historico():
      janela.destroy()
      janela_historico = tk.Tk()
      janela_historico.geometry('700x800')
      janela_historico.resizable(False, False)
      janela_historico.title('Histórico')
      janela_historico.iconbitmap('icones/icone.ico')
      janela_historico.config(background=cor_janela)
      xx = 10
      yy = 10
      for c in range(len(listag)):
        histo = tk.Label(text=listag, font=('aria', 10, 'bold'))
        histo.place(x=xx , y= yy)
        yy += 20

      janela_historico.mainloop

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
    bg=cor_janela
)

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
        command=funcao
    )
botao.place(x=450 , y=85)
enviar = tk.Entry(
    janela,
    width=30
        
)

enviar.place(x=250, y=90)
#comeca já podendo digitar
enviar.focus()
#botao historico9
botao_historico = tk.Button(
      janela,
      text='Histórico',
      font=('arial', 10, 'bold'),
      cursor='hand2',
      command=historico

)
botao_historico.place(x=620, y=10)
#vincula o botão enter com o botao enviar
janela.bind('<Return>', funcao1)
janela.mainloop()
# o programa tem que me dizer se oque foi digitado é 
#variavel e qual variavel  FEITO
#se só tem espaço  #feito 
#é um número # feito
#é uma letra # feito
# e maiuscula ou minuscula #feito
# a primeira letra e maiuscula ?  # feito
# faazer isso em loop e que cada vez que eu faça um novo atualize # feito
# se possivel criar um historico doque já foi pesquisado com uma haba onde eu possa acessar import tkinter as tk 
    