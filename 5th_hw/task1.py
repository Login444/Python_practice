# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path: str):
    last_dir = file_path.rfind('/')
    dir_path = file_path[:last_dir+1]
    file_name = file_path[last_dir + 1:]
    dot_index = file_name.rfind('.')
    expansion = file_name[dot_index:]
    file_name = file_name.rstrip(expansion)
    return (dir_path, file_name, expansion)


print(get_file_info(file_path))
