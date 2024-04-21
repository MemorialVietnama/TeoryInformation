#entropy_menu
import os
from entropy_calculator import calculate_entropy

def main():
    while True:
        print("Выберите действие:")
        print("1. Выбрать файл")
        print("2. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            filename = input("Введите название файла: ")
            if os.path.exists(filename):
                alphabet_size, hartley_entropy, shannon_entropy, redundancy = calculate_entropy(filename)
                print(f"Размер Алфавита: {alphabet_size}")
                print(f"Энтропия Харти: {hartley_entropy}")
                print(f"Энтропия Шеннона: {shannon_entropy}")
                print(f"Избыточность Алфавита: {redundancy:.2f}%")
            else:
                print("Файл не найден.")
        elif choice == "2":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
