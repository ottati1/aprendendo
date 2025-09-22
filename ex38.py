from datetime import date

data_hoje = date.today()
hoje = []
hoje.append(int(data_hoje.strftime("%d")))
hoje.append(int(data_hoje.strftime('%m')))
hoje.append(int(data_hoje.strftime('%y')))
print(hoje)

perfil = []
while True:
   data = int(input('Digite o dia :'))
   if data <= 30:
        perfil.append(data)
        break
while True:
    mes = int(input('Digite o més '))
    if mes <= 12:
        perfil.append(mes)
        break
while True:
    ano = int(input('Digite o ano'))
    if ano <= hoje[2]:
        perfil[]
        break
print(perfil)