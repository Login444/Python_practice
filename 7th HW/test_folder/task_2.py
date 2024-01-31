# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

string_to_write = """
def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
    count = 1
    dir_list = os.listdir()
    for obj in dir_list:
        ext_ind = obj.find('.')
        if obj[ext_ind+1:] == source_ext:
            len_count = len(str(count))
            new_name = (
                f'{desired_name}'
                f'{count:0>{(num_digits + 1) - len_count}}')
            os.rename(obj, f'{new_name}.{target_ext}')
            count += 1
"""


with open('__init__.py', 'w') as init_file:
    init_file.write(string_to_write)