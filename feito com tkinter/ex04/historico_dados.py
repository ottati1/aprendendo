import tkinter as tk
from ex4 import exemplo04
cor = "#adf5fa"
def historico1():
    janela = tk.Tk()
    janela.title('Histórico')
    janela.geometry('700x800')
    janela.resizable(False, False)
    janela.iconbitmap('icones/icone.ico')
    janela.configure(background=cor)
    #BOTÃO PARA RETORNAR PARA A JANELA PRINCIPAL 
    def voltar():
        exemplo04()

    botao_volta = tk.Button(
        janela,
        text='Voltar',
        font=('arial', 12, 'bold'),
        command=voltar
    )
    botao_volta.grid(row=0, column=0)



    janela.mainloop()