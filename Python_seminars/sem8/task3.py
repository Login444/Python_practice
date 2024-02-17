# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def load_json(file_name: str):
    with open(file_name, 'r', encoding='UTF-8') as json_file:
        return json.load(json_file)


def json_to_csv(filename: str):
    json_dict = load_json(filename)
    user_list = []
    for user_lvl, user in json_dict.items():
        for user_id, user_name in user.items():
            user_list.append((user_name, user_id, user_lvl))
    with open(filename.split('.')[0] + '.csv', 'w', encoding='UTF-8') as csv_file:
        csv_write = csv.writer(csv_file, dialect='excel', delimiter='|', lineterminator='\n')
        csv_write.writerow(['Name', 'ID', 'LVL'])
        for row in user_list:
            csv_write.writerow(row)


my_string = input('Введи строку: ')
my_string = my_string.title()
print(my_string)
