from pathlib import Path


def create_file():
    flag = 0
    while flag == 0:
        path_choosing = input("Укажите путь создания файла: ")
        if not Path(path_choosing).exists():
            print("\nПуть Не существует\n")
        else:
            flag += 1

    def file_name_choosing():
        global new_file
        global new_file_path
        global file_name
        file_name = input("Укажите название файла с раcширением .csv: ")
        new_file = Path(path_choosing + '\\' + file_name)
        new_file_path = path_choosing + '\\' + file_name

        if new_file.exists():
            print('\nОшибка: Файл с таким именем уже существует\n')
            file_name_choosing()
        elif '.csv' not in file_name:
            print('\nНеверное расширение файла\n')
            file_name_choosing()
        else:
            new_file.touch()

    file_name_choosing()

    if new_file.exists():
        print("Файл успешно создан!")
        new_file_path = path_choosing + '\\' + file_name

    else:
        print("Возникла ошибка")


create_file()
