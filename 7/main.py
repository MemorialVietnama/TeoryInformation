from auth import authenticate_user
from admin import admin_menu
from user import user_menu, register_user

def is_admin(login):
    # Предположим, что здесь будет код, который проверяет, является ли пользователь администратором
    return login == "admin"

def is_registered_user(login, users):
    # Предположим, что здесь будет код, который проверяет, является ли пользователь зарегистрированным пользователем
    return login in users

def main():
    users = {}

    while True:
        print("\nГлавное меню:")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if authenticate_user(login, password, users):
                print("Вы авторизованы")
                if is_admin(login):
                    admin_menu(users)
                elif is_registered_user(login, users):
                    user_menu(users)
                else:
                    print("Пользователь не определен")
            else:
                print("Неправильный логин или пароль")
        elif choice == "2":
            register_user(users)
        elif choice == "3":
            print("Выход из программы")
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()
