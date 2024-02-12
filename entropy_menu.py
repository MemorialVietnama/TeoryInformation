import os
from entropy_calculator import main as calculate_entropy

def main():
    while True:
        print("Выберите действие:")
        print("1. Выбрать файл")
        print("2. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            filename = input("Введите название файла: ")
            if os.path.exists(filename):
                calculate_entropy(filename)
            else:
                print("Файл не найден.")
        elif choice == "2":
            print("Выход из программы.")
            break  # Завершаем цикл, если выбран второй пункт
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()