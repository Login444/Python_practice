# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
import os


# def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
#     count = 1
#     os.chdir('test_folder')
#     dir_list = os.listdir()
#     for obj in dir_list:
#         file_name, file_ext = obj.split('.')
#         if file_ext == source_ext:
#             len_count = len(str(count))
#             new_name = (
#                 f'{desired_name}'
#                 f'{count:0>{(num_digits + 1) - len_count}}')
#             os.rename(obj, f'{new_name}.{target_ext}')
#             count += 1


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


rename_files('successfully', 3, 'txt', 'csv')