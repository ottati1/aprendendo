from datetime import date

data_hoje = date.today()
hoje = []
hoje.append(int(data_hoje.strftime("%d")))
hoje.append(int(data_hoje.strftime('%m')))
hoje.append(int(data_hoje.strftime('%y')))
print(hoje)

nasc = int(input('Em que ano você nasceu? '))
if 