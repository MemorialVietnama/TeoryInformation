
from crypto import Crypt

if __name__ == "__main__":
    caesar = Crypt()

    while True:
        try:
            mode = int(input("\nРежим работы:\n1) Шифрование;\n2) Дешифрование;\n3) Выход.\n\nВвод: "))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        if mode == 3:
            caesar.__del__()
            
            break

        if mode > 2 or mode < 1:
            continue

        m = str(input("Введите текст: "))
        try:
            k = int(input("Введите ключ: "))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        try:
            n = int(input("Введите мощность: "))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        result = None

        if mode == 1:
            result = caesar.crypt(m, k, n)
        elif mode == 2:
            result = caesar.encrypt(m, k, n)

        print("\nРезультат: " + result)