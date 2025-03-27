def add_data(file_name, data):
    # Добавляет новую строку в файл.
    with open(file_name, 'a') as file:
        file.write(data + '\n')
    print(f'Данные добавлены: {data}')

def update_data(file_name, old_data, new_data):
    # Обновляет существующую строку в файле.
    with open(file_name, 'r') as file: lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in lines:
            if line.strip() == old_data:
                file.write(new_data + '\n')
                print(f'Данные обновлены: {old_data} -> {new_data}')
            else:
                file.write(line)

def delete_data(file_name, data):
    # Удаляет строку из файла.
    with open(file_name, 'r') as file: lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in lines:
            if line.strip() != data:
                file.write(line)
            else:
                print(f'Данные удалены: {data}')

def display_data(file_name):
    # Отображает все данные из файла.
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("Содержимое файла")
        for line in lines:
            print(line.strip())
    print(f'Файл {file_name} не найден.')

if__name__ = "__main__"
file_name = 'file.txt'

add_data(file_name, 'Первая запись')
add_data(file_name, 'Вторая запись')
display_data(file_name)

update_data(file_name, 'Первая запись', 'Обновлённая запись')
display_data(file_name)

delete_data(file_name, 'Вторая запись')
display_data(file_name)