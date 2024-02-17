# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory.

code_to_write = '''
import os
import json
import csv
import pickle

def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path_1.join(dirpath, f)
            total_size += os.path_1.getsize(fp)
        for d in dirnames:
            dp = os.path_1.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)

def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])

def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path_1 = os.path_1.join(root, name)
            size = os.path_1.getsize(path_1)
            results.append({'Path': path_1, 'Type': 'File', 'Size': size})
        for name in dirs:
            path_1 = os.path_1.join(root, name)
            size = get_dir_size(path_1)
            results.append({'Path': path_1, 'Type': 'Directory', 'Size': size})
    return results
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)