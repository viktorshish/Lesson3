# Скачайте файл по ссылке
# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as file:
    content = file.read()
string_length = len(content)
print(f'Длина строки: {string_length}')
words = content.split()
print(f'Количество слов в тексте: {len(words)}')
new_content = content.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as file:
    file.write(new_content)