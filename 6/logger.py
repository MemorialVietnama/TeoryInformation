import logging
import os
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename='user_actions.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

# Функция для записи в лог файл при выборе пользователем опции 5
def log_user_action(action):
    logging.info(action)

# Функция для сохранения лог файла в файл log.txt
def save_log_to_file():
    try:
        current_dir = os.path.dirname(__file__)
        folder_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        folder_path = os.path.join(current_dir, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        log_file_path = os.path.join(folder_path, 'user_actions.log')
        print("Пытаюсь записать в", log_file_path)
        
        # Создаем файл лога, если он не существует
        if not os.path.exists(log_file_path):
            with open(log_file_path, 'w'):
                pass

        # Копируем содержимое исходного файла лога в новый файл
        with open(log_file_path, 'w') as output_file:
            with open('user_actions.log', 'r') as log_file:
                output_file.write("Содержимое лог файла:\n")
                for line in log_file:
                    output_file.write(line.strip() + '\n')
        
        print("Лог файл успешно сохранен в папке", folder_path)
    except Exception as e:
        print("Произошла ошибка при сохранении лог файла:", e)