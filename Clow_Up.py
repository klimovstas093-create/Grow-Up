import Assistant
import Vegetable
import time

piople = Assistant()

Corn = Vegetable()
Tomato = Vegetable()
Potato = Vegetable()

print('Симуляция рабочего дня началась.')


Time = ''
deistvie = ''

for i in range(8, 19):
    Time = input('Время: 8:00.\n Вы зашли в кабинет с опытными образцами.\n Выберите образец:\n 1 — кукуруза;\n 2 — помидор;\n3 — картофель')
    
    if Time == "1":
        chouse = Corn 
    elif Time == "2":
        chouse = Tomato
    elif Time == '3':
        chouse = Potato

    deistvie = input('Выберите действие:\n1 — полить;\n2 — внести удобрение;\n3 — включить дополнительное освещение')

    if deistvie == "1":
        print('полить')
    elif deistvie == "2":
        print('внести удобрение')
    elif deistvie == '3':
        print('включить дополнительное освещение')
