import csv
import json
import os
import pickle


def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            total_size += get_dir_size(os.path.join(dirpath, d))
    return total_size


def traverse_directory(directory):
    list_res = []
    for path, dir_list, file_list in os.walk(directory):
        for cur_file in file_list:
            list_res.append({
                'Path': os.path.join(path, cur_file),
                'Type': 'File',
                'Size': os.path.getsize(os.path.join(path, cur_file))})
        for cur_dir in dir_list:
            list_res.append({
                'Path': os.path.join(path, cur_dir),
                'Type': 'Directory',
                'Size': get_dir_size(os.path.join(path, cur_dir))})

    return list_res


def save_results_to_json(source, name):
    with open(name, 'w', encoding='utf-8') as data:
        json.dump(source, data, indent=4, ensure_ascii=False)


def save_results_to_pickle(source, name):
    with open(name, 'wb') as pickle_file:
        pickle.dump(source, pickle_file)


def save_results_to_csv(source, name):
    file = [['Path', 'Type', 'Size']]
    for item in source:
        file.append([*item.values()])
    with open(name, 'w', encoding='utf-8') as data:
        csv_write = csv.writer(data, dialect='excel', delimiter=',', lineterminator="\n", )
        csv_write.writerows(file)


results = traverse_directory(os.getcwd())

save_results_to_pickle(results, 'results.pkl')
save_results_to_json(results, 'results.json')

save_results_to_csv(results, 'results.csv')