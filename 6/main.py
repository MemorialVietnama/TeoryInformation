import sys
import os
import configparser
from code_generator import CodeGenerator
from hamming_coding import HammingCoding

from read_setting import read_word_size

def huffman_menu():
    print("Алгоритм Хаффмана:")
    print("1. Закодировать по Хаффману")
    print("2. Вернуться в главное меню")
    choice = input("Введите номер действия: ")
    return choice

def hamming_menu():
    print("Алгоритм Хемминга:")
    print("1. Закодировать bitarray по Хеммингу")
    print("2. Декодировать bitarray по Хеммингу")
    print("3. Вернутся в главное меню")
    choice = input("Введите номер действия: ")
    return choice

def hamming_errors_menu():
    print("Ошибки в Хемминге:")
    print("1. Внести ошибки в результат кодировки Хемминга")
    print("2. Исправить ошибки в ошибочном коде Хемминга")
    print("3. Вернутся в главное меню")
    choice = input("Введите номер действия: ")
    return choice



def main():

    filename = 'settings.ini'  # Укажите имя вашего файла
    rword_size = read_word_size(filename)

    if rword_size is not None:
        print("Значение переменной word_size:", rword_size)
    else:
        print("Не удалось получить значение переменной word_size.")

    while True:
        print("\nГлавное меню:")
        print("1. Алгоритм Хаффмана")
        print("2. Алгоритм Хемминга")
        print("3. Ошибки в Хемминге")
        print("4. Вывод файла Log")
        print("5. Выход из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            huffman_choice = huffman_menu()
            if huffman_choice == '1':
                text = input("Введите текст для кодировки по Хаффману: ")
                code_generator = CodeGenerator()  # Instantiate CodeGenerator here
                result = code_generator.gen_code(text)
                print("Код Хаффмана сгенерирован.")
                print("Закодированный текст:", result["binary_text"])
                print("Соответствующие коды:", result["codes"])
            elif huffman_choice == '2':
                continue
            else:
                print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")

        elif choice == '2':
            hamming_choice = hamming_menu()
            if hamming_choice == '1':
                text_hem = input("Введите текст для кодировки Хемминга: ")
                hamming_coder = HammingCoding(rword_size)
                encoded_text = hamming_coder.encode(text_hem, rword_size)
                print("Закодированный текст по Хеммингу:", encoded_text)
                pass
            elif hamming_choice == '2':
                pre_text = input("Введите закодированный текст: ")
                decoded_text = hamming_coder.decode(pre_text, rword_size)
                print("Декодированный текст по Хеммингу:", decoded_text)
            elif hamming_choice == '3':
                continue
            else:
                print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")
        elif choice == '3':
            hamming_errors_choice = hamming_errors_menu()
            if hamming_errors_choice == '1':
                # Реализация внесения ошибок в код Хемминга
                pass
            elif hamming_errors_choice == '2':
                # Реализация исправления ошибок в коде Хемминга
                pass
            else:
                print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")
        elif choice == '4':
            # Реализация вывода файла Log
            pass
        elif choice == '5':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")

if __name__ == "__main__":
    main()
