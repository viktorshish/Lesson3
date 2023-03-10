users = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

# Запишите содержимое списка словарей в файл в формате csv
import csv

fields = ['name', 'age', 'job']

with open('users.csv', 'w', encoding = 'utf-8') as file:
    writer = csv.DictWriter(file, fields, delimiter = ';')
    writer.writeheader()
    for user in users:
        writer.writerow(user)
