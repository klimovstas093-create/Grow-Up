#код Кроткова Льва
from Assistant import Assistant
from Vegetable import Vegetable
from random import random

assistant = Assistant(input("Введите ваше имя:\n"), "Ассистент")

Corn = Vegetable("Кукуруза", 10+random(), 10+random(), 10+random())
Tomato = Vegetable("Помидор", 10+random(), 10+random(), 10+random())
Potato = Vegetable("Картофель", 10+random(), 10+random(), 10+random())

print('Симуляция рабочего дня началась.')
print("Вы зашли в кабинет с опытными образцами.")

Time = ''
deistvie = ''

for i in range(8, 19):
    Time = input(f'\nВремя: {i}:00.\nВыберите образец:\n 1 — кукуруза;\n 2 — помидор;\n 3 — картофель\n 4 — ничего не делать\n')
    if Time == "1":
        chouse = Corn 
    elif Time == "2":
        chouse = Tomato
    elif Time == '3':
        chouse = Potato
    else:
        continue

    deistvie = input('Выберите действие:\n 1 — полить;\n 2 — внести удобрение;\n 3 — включить дополнительное освещение\n 4 — узнать информацию\n 5 — ничего не делать\n')

    if deistvie == "1":
        assistant.water_sample(chouse)
    elif deistvie == "2":
        assistant.udobrenie_sample(chouse)
    elif deistvie == '3':
        assistant.light_sample(chouse)
    elif deistvie == '4':
        print(chouse)

    Corn.water -= 0.1
    Tomato.water -= 0.1
    Potato.water -= 0.1

vegetables = []

print("\nКонец рабочего дня\nРезультаты:")
print(Corn)
vegetables.append(Corn.check_state(11, 10, 10))
print(Tomato)
vegetables.append(Tomato.check_state(11, 10, 10))
print(Potato)
vegetables.append(Potato.check_state(11, 10, 10))
print("\nИтог:")
assistant.check_certificate(vegetables)
