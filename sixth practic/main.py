import logic
import configparser
import os

def main_menu():
    settings_file = os.path.join(os.path.dirname(__file__), "settings.ini")


    while True:
        print("\nВыберите действие:")
        print("1. Перевести текст в Юникод, закодировать его по Хаффману и сформировать bytearray")
        print("2. Закодировать последовательность байт кодом Хэмминга")
        print("3. Декодировать последовательность байт кодом Хэмминга")
        print("4. Обработка ошибок кодом Хэмминга")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            text = input("Введите текст: ")
            unicode_text = logic.text_to_unicode(text)
            encoded_text = logic.huffman_encode(text)
            bytearray_text = bytearray(encoded_text.encode('utf-8'))
            print("Закодированный текст в формате bytearray:", bytearray_text)
            print("Последовательность байтов:", ','.join(encoded_text))
        elif choice == "2":
            byte_sequence = input("Введите последовательность байт через запятую: ").split(',')
            byte_sequence = [int(byte) for byte in byte_sequence]

            if os.path.exists(settings_file):
                settings = logic.read_settings_from_ini(settings_file)
                word_size = int(settings.get('word_size', 8))
                hamming_coder = logic.HammingCoder(word_size)
                encoded_sequence = hamming_coder.encode(byte_sequence)
                print("Закодированная последовательность байт:", bytearray(encoded_sequence))
            else:
                print(f"Файл настроек '{settings_file}' не найден.")
        elif choice == "3":
            if os.path.exists(settings_file):
                 logic.decode_hamming_sequence()  # вызов функции для декодирования последовательности байт
            else:
                print(f"Файл настроек '{settings_file}' не найден.")
        elif choice == "4":
            if os.path.exists(settings_file):
                logic.hamming_menu()  # Вызов новой функции подменю для управления ошибками в коде Хэмминга
            else:
                print(f"Файл настроек '{settings_file}' не найден.")

        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
if __name__ == "__main__":
    main_menu()
