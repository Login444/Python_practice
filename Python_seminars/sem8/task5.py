# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import os
import json
import pickle


def search_json(dir_name: str):
    for obj in os.listdir(os.path.join(os.getcwd(), dir_name)):
        file_name, file_ext = obj.split('.')
        if file_ext == 'json':
            pass
            
