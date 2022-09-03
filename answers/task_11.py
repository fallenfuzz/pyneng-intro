"""
Запросить у пользователя ввод цвета через input.

Если введенный цвет есть в списке colors, вывести сообщение "Такой цвет есть".
Если цвета нет, вывести сообщение "В списке colors нет такого цвета".

Сделать так чтобы пользователь мог вводить цвет в любом регистре, но при этом
проверка для слова работала (ниже пример).

Пример работы задания:
$ python task_11.py
Введите цвет: red
Такой цвет есть

$ python task_11.py
Введите цвет: Red
Такой цвет есть

$ python task_11.py
Введите цвет: RED
Такой цвет есть

$ python task_11.py
Введите цвет: blue
В списке colors нет такого цвета

Для выполнения задания нельзя менять список colors.
"""
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

# вариант 1
user_color = input('Введите цвет: ')
found_color = False
for color in colors:
    if user_color.lower() == color.lower():
        found_color = True

if found_color:
    print('Такой цвет есть')
else:
    print('В списке colors нет такого цвета')


# вариант 2
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
colors_lower = []
for color in colors:
    colors_lower.append(color.lower())

user_color = input('Введите цвет: ')
if user_color.lower() in colors_lower:
    print("Такой цвет есть")
else:
    print("В списке colors нет такого цвета")

# вариант 3

colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
user_color = input("Введите цвет: ")
message = "В списке colors нет такого цвета"
for color in colors:
    if user_color.lower() == color.lower():
        message = "Такой цвет есть"
print(message)

# вариант 4, но в теории не было break
user_color = input('Введите цвет: ')
for color in colors:
    if user_color.lower() == color.lower():
        print('Такой цвет есть')
        break
else:
    print('В списке colors нет такого цвета')
