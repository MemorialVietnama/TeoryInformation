import os
import configparser

def read_word_size(filename):
    # Получение пути к текущему скрипту
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Получение пути к файлу settings.ini в той же директории, что и скрипт
    file_path = os.path.join(script_dir, filename)

    # Проверка существования файла
    if not os.path.isfile(file_path):
        print(f"Файл {filename} не найден в текущей директории.")
        return None

    # Чтение содержимого файла
    config = configparser.ConfigParser()
    config.read(file_path)

    # Получение значения переменной word_size из раздела Settings
    if 'Settings' in config:
        word_size = config['Settings'].getint('word_size', fallback=None)
        return word_size
    else:
        print("Раздел 'Settings' не найден в файле settings.ini.")
        return None
    
    
