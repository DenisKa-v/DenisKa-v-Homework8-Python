"""1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить
на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано
положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела"""

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.readlines()
#     if not text:
#         print(f'Файл {file.name} пустой.')
#     elif len(text) < lines:
#         print(f'Все строки из файла {file.name} (так как кол-во строк в файле меньше, чем запрашиваемых '
#               f'({len(text)} < {lines})):')
#         print(*text, sep='')
#     else:
#         print(f'Посдедние {lines} строки из файла {file.name}:')
#         print(*text[(len(text) - lines):], sep='')
#
#
# read_file = 'article.txt'
# read_lines = input(f'Введите кол-во строк, которые необходимо вывести из файла {read_file}: ')
# if not read_lines.isdigit() or int(read_lines) == 0:
#     print('Некорректный ввод! Введите положительное целое число.')
# else:
#     read_last(int(read_lines), read_file)

"""2. Документ «article.txt» содержит следующий текст:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела

Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину 
(или список слов, если таковых несколько)."""

# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.read().split()
#     if not text:
#         print(f'Файл {file.name} пустой.')
#     else:
#         max_el = 0
#         text2 = set()
#         for el in text:
#             if len(el) > max_el:
#                 max_el = len(el)
#         for elm in text:
#             if len(elm) == max_el:
#                 text2.add(elm)
#         print(f'Слово или слова с максимальной длиной (равной {max_el}) из файла {file.name}:')
#         for i in text2:
#             print(i)
#         print(f'Количество, найденный слов: {len(text2)}.')
#
#
# read_file = 'article.txt'
# longest_words(read_file)