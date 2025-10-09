import tkinter as tk
def digitou():
    valor = entrada.get()
    print(valor)
    return valor


  #janela  
janela = tk.Tk()
janela.title('validação de sexo')
janela.geometry('300x500+800+300')
#texto fixo
tk.Label(janela, text='Validação de sexo').pack()
tk.Label(janela, text='Digite M ou F').pack()
#area de interação 
entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text='Validar', command=digitou).pack()

#loop janela
janela.mainloop()
