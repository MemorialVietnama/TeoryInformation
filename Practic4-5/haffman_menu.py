# huffman_menu.py
import os
import json
from datetime import datetime
from haffman import CodeGenerator

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

def encode_file():
    input_file = get_input_file()
    cgen = CodeGenerator()
    code_folder = create_code_folder()
    code_file_path = os.path.join(code_folder, "code.json")

    try:
        cgen.gen_code(input_file, code_file_path)
        print(f"Код Хаффмана сохранен. Код сохранен в файле: {code_file_path}")

        with open(code_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            encoded_text = cgen.encode_text(data["text"])

        print(f"Закодированный текст: {encoded_text}")

    except Exception as e:
        print(f"Ошибка: {e}")

def decode_file():
    try:
        code_file = input("Введите путь к закодированному JSON файлу: ")
        output_file = input("Введите путь к файлу для сохранения раскодированного текста: ")

        with open(code_file, "r", encoding="utf-8") as file:
            codes = json.load(file)

        encoded_text = input("Введите закодированный текст: ")

        cgen = CodeGenerator()
        decoded_text = cgen.decode_text(encoded_text)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decoded_text)

        print(f"Файл успешно раскодирован. Результат сохранен в файле: {output_file}")

    except Exception as e:
        print(f"Ошибка при раскодировании: {e}")

def main():
    while True:
        print("Генератор Кода Хаффмана, выберите условия контекстного меню:")
        print("1. Закодировать по шифровке Хаффмана")
        print("2. Раскодировать JSON")
        print("3. Выход из программы.")
        choice = input("Введите номер действия: ")

        if not choice.strip():
            print("Ошибка: Некорректный ввод. Пожалуйста, введите 1, 2.")
            continue

        if choice == "1":
            encode_file()
        elif choice == "2":
            decode_file()
        elif choice == "3":
            print("Выход из программы")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер из списка.")

if __name__ == "__main__":
    main()
