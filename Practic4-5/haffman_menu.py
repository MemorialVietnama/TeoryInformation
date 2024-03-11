# huffman_menu.py

import os
import json
from datetime import datetime
from haffman import CodeGenerator, calculate_entropy

def create_code_folder():
    # Создает уникальную директорию на основе текущей даты и времени
    folder_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name

def get_input_file():
    # Получает список файлов в текущей директории и позволяет пользователю выбрать файл
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
    # Закодирует выбранный файл с использованием кода Хаффмана
    input_file = get_input_file()
    cgen = CodeGenerator()
    code_folder = create_code_folder()
    code_file_path = os.path.join(code_folder, "code.json")

    try:
        # Создает код Хаффмана для выбранного файла и сохраняет его
        cgen.gen_code(input_file, code_file_path)
        print(f"Код Хаффмана сохранен. Код сохранен в файле: {code_file_path}")

        # Загружает закодированный текст из файла
        with open(code_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            encoded_text = data["binary_text"]

        print(f"Закодированный текст: {encoded_text}")
        
        # Вычисляет размеры файлов, энтропию, среднее количество бит на символ и степень сжатия
        input_file_size = os.path.getsize(input_file)
        encoded_file_size = os.path.getsize(code_file_path)

        entropy = calculate_entropy(input_file)
        average_bits_per_symbol = encoded_file_size * 8 / len(encoded_text)
        compression_ratio = input_file_size / encoded_file_size

        print(f"Размер исходного файла: {input_file_size} байт")
        print(f"Размер закодированного файла: {encoded_file_size} байт")
        print(f"Энтропия исходного текстового файла: {entropy}")
        print(f"Среднее количество бит на символ в закодированном файле: {average_bits_per_symbol}")
        print(f"Степень сжатия: {compression_ratio:.2f}%")

    except Exception as e:
        print(f"Ошибка: {e}")

def decode_file():
    try:
        # Раскодирует выбранный файл, используя код Хаффмана
        code_file_path = input("Введите путь к закодированному JSON файлу: ")
        output_folder = os.path.dirname(code_file_path)

        with open(code_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            encoded_text = data["binary_text"]
            codes = data["codes"]

        cgen = CodeGenerator()
        cgen.codes = codes  # Используем переданный массив кодов для декодирования
        decoder_text = cgen.decode_text(encoded_text)

        output_file_path = os.path.join(output_folder, "decoded_text.txt")
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(decoder_text)

        print(f"Файл успешно раскодирован. Результат сохранен в файле: {output_file_path}")
        print(f"Декодированный текст:  {decoder_text} ")

        # Вычисляет размеры файлов, энтропию, среднее количество бит на символ и степень сжатия
        input_file_size = os.path.getsize(code_file_path)
        decoded_file_size = os.path.getsize(output_file_path)

        entropy = calculate_entropy(output_file_path)
        average_bits_per_symbol = input_file_size * 8 / len(encoded_text)
        compression_ratio = decoded_file_size / input_file_size

        print(f"Размер закодированного файла: {input_file_size} байт")
        print(f"Размер раскодированного файла: {decoded_file_size} байт")
        print(f"Энтропия раскодированного текстового файла: {entropy}")
        print(f"Среднее количество бит на символ в раскодированном файле: {average_bits_per_symbol}")
        print(f"Степень сжатия: {compression_ratio:.2f}%")
        
        # Добавляет результаты сравнения в файл "decoded_text.txt"
        comparison_results = f"\n\nСравнение результатов:\n" \
                             f"Размер закодированного файла: {input_file_size} байт\n" \
                             f"Размер раскодированного файла: {decoded_file_size} байт\n" \
                             f"Энтропия раскодированного текстового файла: {entropy}\n" \
                             f"Среднее количество бит на символ в раскодированном файле: {average_bits_per_symbol}\n" \
                             f"Степень сжатия: {compression_ratio:.2f}%\n"

        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write(comparison_results)

    except Exception as e:
        print(f"Ошибка при раскодировании: {e}")

def main():
    # Основной цикл программы, предоставляющий пользователю меню
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
