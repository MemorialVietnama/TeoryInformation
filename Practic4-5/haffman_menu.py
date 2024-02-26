import os
import argparse
from haffman import CodeGenerator
from datetime import datetime

def create_code_folder():
    folder_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name

def get_input_file():
    files_in_current_dir = [f for f in os.listdir('.') if os.path.isfile(f)]

    if not files_in_current_dir:
        raise FileNotFoundError("В текущей директории нет файлов.")

    print("Доступные файлы:")
    for i, file in enumerate(files_in_current_dir, start=1):
        print(f"{i}. {file}")

    while True:
        try:
            choice = int(input("Введите номер файла (1, 2, и т.д.): "))
            if 1 <= choice <= len(files_in_current_dir):
                return files_in_current_dir[choice - 1]
            else:
                print("Некорректный выбор. Пожалуйста, введите номер из списка.")
        except ValueError:
            print("Некорректный ввод. Введите номер файла.")

def main():
    input_file = get_input_file()

    cgen = CodeGenerator()
    code_folder = create_code_folder()
    code_file_path = os.path.join(code_folder, "code.json")

    try:
        cgen.gen_code(input_file, code_file_path)
        print(f"Код Хаффмана сохранен. Код сохранен в файле: {code_file_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
