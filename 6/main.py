# main.py

from hamming_code import HammingCode
from settings_reader import read_settings

def main():
    word_size = read_settings()
    hamming = HammingCode(word_size)

    while True:
        print("Выберите действие:")
        print("1. Кодировать последовательность байт методом Хэмминга")
        print("2. Декодировать последовательность байт методом Хэмминга")
        print("3. Внести ошибки в последовательность байт")
        print("4. Корректировать ошибки в закодированной последовательности байт")
        print("5. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            byte_sequence = input("Введите последовательность байт для кодирования: ")
            encoded_sequence = hamming.encode(byte_sequence)
            print("Закодированная последовательность:", encoded_sequence)

        elif choice == '2':
            encoded_sequence = input("Введите закодированную последовательность байт для декодирования: ")
            decoded_sequence = hamming.decode(encoded_sequence)
            print("Декодированная последовательность:", decoded_sequence)

        elif choice == '3':
            byte_sequence = input("Введите последовательность байт для внесения ошибок: ")
            error_count = int(input("Введите количество ошибок: "))
            errored_sequence = hamming.introduce_errors(byte_sequence, error_count)
            print("Последовательность с ошибками:", errored_sequence)

        elif choice == '4':
            encoded_sequence = input("Введите закодированную последовательность байт для коррекции ошибок: ")
            corrected_sequence = hamming.correct_errors(encoded_sequence)
            print("Скорректированная последовательность:", corrected_sequence)

        elif choice == '5':
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()
