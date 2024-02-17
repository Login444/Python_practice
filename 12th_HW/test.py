data = {}
with open('subjects.csv', 'r', encoding="UTF-8") as file:
    subjects_file = file.read()
    for i in subjects_file.split(','):
        data[i] = ""

print(data)
