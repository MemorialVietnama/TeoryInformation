# morse_decoder.py

import os

MORSE_CODE_DICT = {'А': '•-', 'Б': '-•••', 'В': '•--', 'Г': '--•', 'Д': '-••',
                  'Е': '•',  'Ж': '•••-', 'З': '--••', 'И': '••', 'Й': '•---',
                  'К': '-•-', 'Л': '•-••', 'М': '--', 'Н': '-•', 'О': '---',
                  'П': '•--•', 'Р': '•-•', 'С': '•••', 'Т': '-', 'У': '••-',
                  'Ф': '••-••', 'Х': '••••', 'Ц': '-•-•', 'Ч': '---•', 'Ш': '----',
                  'Щ': '--•-', 'Ъ': '--•--', 'Ы': '-•--', 'Ь': '-••-', 'Э': '••-••',
                  'Ю': '••--', 'Я': '•-•-', '0': '-----', '1': '•----', '2': '••---',
                  '3': '•••--', '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
                  '8': '---••', '9': '----•', '.': '•-•-•-', ',': '--••--', ';': '-•-•-•',
                  ':': '---•••', '?': '••--••', '!': '-•-•--', '-': '-••••-', ' ': '\t'}

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for char, morse in MORSE_CODE_DICT.items():
            if code == morse:
                text += char
    return text


def decode_input():
    print("Выберите источник данных:")
    print("1 - Ввод вручную")
    print("2 - Загрузка из файла")
    
    choice = input("Введите номер источника: ")
    
    if choice == '1':
        morse_input = input("Введите азбуку Морзе для декодирования: ")
        return morse_input
    elif choice == '2':
        filename = input("Введите имя файла для загрузки: ")
        filepath = os.path.join(os.getcwd(), filename)  # Полный путь к файлу
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return decode_input()
    else:
        print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
        return decode_input()