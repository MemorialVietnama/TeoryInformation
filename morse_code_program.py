# morse_code_program.py

import os
from morse_decoder_encoder import text_to_morse, morse_to_text


def main():
    while True:
        print("Выберите действие:")
        print("1. Кодировать текст в азбуке Морзе")
        print("2. Декодировать азбуку Морзе в текст")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if not choice.strip():  
            print("Ошибка: Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")
            continue

        if choice == '1':
            print("Выберите источник данных:")
            print("1 - Ввод вручную")
            print("2 - Загрузка из файла")
    
            choice_source = input("Введите номер источника: ")
    
            if not choice_source.strip():
                print("Ошибка: Некорректный ввод. Пожалуйста, введите 1 или 2.")
                continue

            if choice_source == '1':
                text_input = input("Введите текст для кодирования: ")
                
                if not text_input.strip():
                    print("Ошибка: Нету текста. Пожалуйста, введите текст для кодирования.")
                    continue

            elif choice_source == '2':
                filename = input("Введите имя файла для загрузки: ")
                filepath = os.path.join(os.getcwd(), filename)  # Полный путь к файлу
                try:
                    with open(filepath, 'r') as file:
                        text_input = file.read()
                        
                    if not text_input.strip():
                        print("Ошибка: Нету текста в файле. Пожалуйста, введите текст для кодирования.")
                        continue
                        
                except FileNotFoundError:
                    print(f"Файл {filename} не найден.")
                    continue
            else:
                print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
                continue

            morse_code = text_to_morse(text_input)
            print("Результат кодирования: ", morse_code)

            save_to_file = input("Желаете сохранить результат в файл? (y/n): ")
            if save_to_file.lower() == 'y':
                filename = input("Введите имя файла: ")
                with open(filename, 'w') as file:
                    file.write(morse_code)

        elif choice == '2':
            print("Выберите источник данных:")
            print("1 - Ввод вручную")
            print("2 - Загрузка из файла")
    
            choice_source = input("Введите номер источника: ")
    
            if not choice_source.strip():
                print("Ошибка: Некорректный ввод. Пожалуйста, введите 1 или 2.")
                continue

            if choice_source == '1':
                morse_input = input("Введите азбуку Морзе для декодирования: ")
                
                if not morse_input.strip():
                    print("Ошибка: Нету текста. Пожалуйста, введите азбуку Морзе для декодирования.")
                    continue

            elif choice_source == '2':
                filename = input("Введите имя файла для загрузки: ")
                filepath = os.path.join(os.getcwd(), filename)  # Полный путь к файлу
                try:
                    with open(filepath, 'r') as file:
                        morse_input = file.read()
                        
                    if not morse_input.strip():
                        print("Ошибка: Нету текста в файле. Пожалуйста, введите азбуку Морзе для декодирования.")
                        continue
                        
                except FileNotFoundError:
                    print(f"Файл {filename} не найден.")
                    continue
            else:
                print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
                continue

            text = morse_to_text(morse_input)
            print("Результат декодирования: ", text)

            save_to_file = input("Желаете сохранить результат в файл? (y/n): ")
            if save_to_file.lower() == 'y':
                filename = input("Введите имя файла: ")
                with open(filename, 'w') as file:
                    file.write(text)

        elif choice == '3':
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()
