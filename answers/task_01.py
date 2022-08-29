"""
Если запустить код задания, будет такой вывод:
$ python task_01.py
Python is a high-level, interpreted, general-purpose programming language.

Надо преобразовать строку start_data таким образом, чтобы на экран была выведена
такая строка (заменить Python на Ruby):
$ python task_01.py
Ruby is a high-level, interpreted, general-purpose programming language.

При этом нельзя менять строку start_data вручную, то есть нельзя менять исходную строку
start_data.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
print(start_data)
print(start_data.replace('Python', 'Ruby'))
