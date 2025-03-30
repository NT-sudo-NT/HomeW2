import os

def create_file(file_path):
    # Создает новый файл, если он не существует.
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("Это новый файл.\n")  # Начальное содержимое
            print(f"Файл '{file_path}' был создан.")
    else:
        print(f"Файл '{file_path}' уже существует.")

def append_to_file(file_path, data):
    # Добавляет данные в файл, если он существует.
    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(data + "\n")
            print(f"Данные добавлены в файл '{file_path}': '{data}'")
    else:
        print(f"Файл '{file_path}' не существует. Сначала создайте файл.")

def view_file_content(file_path):
    # Просматривает содержимое файла.
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nСодержимое файла:")
            print(content)
    else:
        print(f"Файл '{file_path}' не существует. Сначала создайте файл.")

def update_file(file_path, replacements):
    # Обновляет данные в файле, если старые данные существуют.
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        original_content = ''.join(content)  # Сохраняем оригинальное содержимое
        changes_made = False

        for old_data, new_data in replacements.items():
            old_data = old_data.strip()  # Убираем пробелы
            new_data = new_data.strip()  # Убираем пробелы
            
            # Проверяем, есть ли старые данные в файле и заменяем их
            new_content = []
            for line in content:
                if old_data in line:
                    line = line.replace(old_data, new_data)
                    print(f"Заменено '{old_data}' на '{new_data}' в файле '{file_path}'.")  # Вывод информации об изменении
                    changes_made = True
                new_content.append(line)

            content = new_content  # Обновляем содержимое файла

        if changes_made:
            with open(file_path, 'w') as file:
                file.writelines(content)

            # Выводим обновленное содержимое файла
            print("\nОбновленное содержимое файла:")
            view_file_content(file_path)

            log_changes(file_path, replacements, original_content, ''.join(content))
    else:
        print(f"Файл '{file_path}' не существует. Сначала создайте файл.")

def log_changes(file_path, replacements, original_content, new_content):
    # Логирует изменения в файл 'changes_log.txt'.
    with open('changes_log.txt', 'a') as log_file:
        log_file.write(f"Изменения в файле '{file_path}':\n")
        log_file.write("Оригинальное содержимое:\n")
        log_file.write(original_content + "\n")
        log_file.write("Новое содержимое:\n")
        log_file.write(new_content + "\n")
        log_file.write("Список замен:\n")
        for old_data, new_data in replacements.items():
            log_file.write(f"  Заменено '{old_data.strip()}' на '{new_data.strip()}'\n")
        log_file.write("\n")

def delete_file(file_path):
    # Удаляет файл, если он существует.
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл '{file_path}' был удален.")
        return True  # Возвращаем True, если файл успешно удален
    else:
        print(f"Файл '{file_path}' не существует.")
        return False  # Возвращаем False, если файл не существует


def main():
    # Запрашиваем у пользователя имя файла
    file_name = input("Введите имя файла (с расширением, например, 'example.txt'): ")
    create_file(file_name)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить данные")
        print("2. Изменить существующие данные")
        print("3. Удалить файл")
        print("4. Выйти")
        
        choice = input("Введите номер действия: ")

        if choice == '1':
            print("Введите данные для добавления. Введите 'стоп' для завершения:")
            while True:
                data_to_add = input("Введите данные: ")
                if data_to_add.lower() == 'стоп':
                    break
                append_to_file(file_name, data_to_add)

        elif choice == '2':
            print("Содержимое файла перед изменениями:")
            view_file_content(file_name)  # Показываем содержимое файла перед изменениями
            print("Введите данные для замены (например, 'первая:новая первая'). Введите 'стоп' для завершения:")
            replacements = {}
            while True:
                user_input = input("Введите замену (старые данные:новые данные): ")
                if user_input.lower() == 'стоп':
                    break
                old_data, new_data = user_input.split(':', 1)  # Используем split для разделения
                if old_data and new_data:  # Проверяем, что обе части не пустые
                    replacements[old_data.strip()] = new_data.strip()  # Убираем пробелы
                else:
                    print("Неправильный формат. Используйте 'старые данные:новые данные'.")

            update_file(file_name, replacements)

        elif choice == '3':
            delete_choice = input(f"Вы уверены, что хотите удалить файл '{file_name}'? (да/нет): ")
            if delete_choice.lower() == 'да':
                if delete_file(file_name):
                    break  # Завершаем цикл после успешного удаления файла

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите номер действия от 1 до 4.")

if __name__ == "__main__":
    main()