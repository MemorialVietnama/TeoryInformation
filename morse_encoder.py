# morse_encoder.py
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

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()

def encode_input():
    print("Выберите источник данных:")
    print("1 - Ввод вручную")
    print("2 - Загрузка из файла")
    
    choice = input("Введите номер источника: ")
    
    if choice == '1':
        text_input = input("Введите текст для кодирования: ")
        return text_input
    elif choice == '2':
        filename = input("Введите имя файла для загрузки: ")
        filepath = os.path.join(os.getcwd(), filename)  # Полный путь к файлу
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return encode_input()
    else:
        print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
        return encode_input()