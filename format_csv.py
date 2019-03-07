import csv

workers_list = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
              {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
              {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},]

with open('workers.csv', 'w', encoding = 'utf-8', newline = '') as outinf:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(outinf, fields, delimiter = ':')
    writer.writeheader()
    for worker in workers_list:
        writer.writerow(worker)