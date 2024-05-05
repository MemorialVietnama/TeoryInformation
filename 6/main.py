import sys
from haff_hem import *
from logger import log_user_action, save_log_to_file
from read_setting import read_word_size

def main():
    while True:
        log_user_action("Программа запущена.")
        filename = 'settings.ini' 
        rword_size = read_word_size(filename)

        if rword_size is not None:
            print("Значение переменной word_size:", rword_size)
        else:
            print("Не удалось получить значение переменной word_size.")

        print("\nПредварительное меню:")
        print("1. Начать")
        print("2. Выйти из программы")

        pre_choice = input("Выберите действие: ")
        if pre_choice == '1':
            text = input("Введите текст для кодировки в Юникод: ")
            log_user_action("Получен текст для кодировки в Юникод: ")
            unicode_text = text_to_unicode(text)
            print("Текст в Юникод:", unicode_text)

            codes = Haffman(text).get_codes()
            log_user_action("Коды Хаффмана успешно сгенерированы.")
            crypted = crypt(codes, text)
            print("Код Хаффмана: ", crypted)

            hem = Heming()
            crypted_hem = hem.code(crypted, True)  # Encoding with Hamming
            log_user_action("Текст успешно закодирован с помощью Хемминга.")
            print("Код Хемминга: ", crypted_hem)

            noised = hem.noise(crypted_hem, 2)  # Introducing noise
            log_user_action("Код Хемминга успешно подвергнут воздействию шума.")
            print("Код Хемминга с добавленными ошибками: ", noised)

            encrypted = hem.code(noised, False)  # Decoding Hamming
            log_user_action("Код Хемминга успешно декодирован.")
            print("Расшифрованное сообщение в Хаффмане: ", encrypted)

            encrypted = encrypt(codes, encrypted)[:len(text)]  # Encrypting with Huffman
            log_user_action("Расшифрованное сообщение успешно зашифровано с помощью Хаффмана.")

            if text != encrypted:
                print("Было найдено более 1-й ошибки!")
                log_user_action("Было найдено более 1-й ошибки!")
            print(f"Расшифрованное сообщение: {encrypted}")
            log_user_action("Расшифрованное сообщение успешно выведено на экран.")
            save_log_to_file()
        

        elif pre_choice == '2':
            print("Выход из программы.")
            log_user_action("Программа завершила свою работу.")
            save_log_to_file()
            sys.exit()
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие 1 или 2.")

        
if __name__ == "__main__":
    main()
