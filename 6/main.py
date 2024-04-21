import logic

def huffman_menu():
    print("\nВыберите действие для Хаффмана:")
    print("1. Сгенерировать код Хаффмана для текста")
    print("2. Сохранить код Хаффмана в JSON")
    print("3. Декодировать текст из кода Хаффмана")
    print("4. Вернуться в главное меню")

    choice = input("Введите номер действия: ")

    if choice == "1":
        text = input("Введите текст: ")
        logic.huffman.generate_huffman_code(text)
    elif choice == "2":
        logic.huffman.save_huffman_code_to_json()
    elif choice == "3":
        encoded_text = input("Введите закодированный текст: ")
        decoded_text = logic.huffman.decode_huffman(encoded_text)
        print("Декодированный текст:", decoded_text)
    elif choice == "4":
        return
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
        huffman_menu()

def hamming_menu():
    print("\nВыберите действие для Хэмминга:")
    print("1. Закодировать последовательность байт кодом Хэмминга")
    print("2. Вернуться в главное меню")

    choice = input("Введите номер действия: ")

    if choice == "1":
        byte_sequence = input("Введите последовательность байт через запятую: ").split(',')
        byte_sequence = [int(byte) for byte in byte_sequence]  # Преобразуем строки в целые числа
        word_size = logic.read_settings_from_ini("settings.ini").get("word_size", 8)
        hamming_coder = logic.HammingCoding(word_size)
        encoded_sequence = hamming_coder.encode(byte_sequence)
        print("Закодированная последовательность байт:", encoded_sequence)
    elif choice == "2":
        return
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
        hamming_menu()

def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1.переводит текст в Юникод, затем кодирует его по Хафману и формирует bytearray")
        print("2. кодирует последовательность байт (bytearray) кодом Хэминга")
        print("3. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            huffman_menu()
        elif choice == "2":
            hamming_menu()
        elif choice == "3":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main_menu()