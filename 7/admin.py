def list_users(users):
    print("Список пользователей:")
    for user in users:
        print(user)

def delete_user(users, login):
    if login in users:
        del users[login]
        print("Пользователь с логином", login, "удален")
    else:
        print("Пользователь с логином", login, "не найден")

def add_user(users, login, password):
    users[login] = password
    print("Новый пользователь добавлен")

def change_password(users, login, new_password):
    if login in users:
        users[login] = new_password
        print("Пароль успешно изменен")
    else:
        print("Пользователь с логином", login, "не найден")
def admin_menu(users):
    while True:
        print("\nМеню администратора:")
        print("1. Вывести список пользователей")
        print("2. Удалить пользователя")
        print("3. Добавить нового пользователя")
        print("4. Сменить свой пароль")
        print("5. Выйти из учетной записи")

        choice = input("Выберите действие: ")

        if choice == "1":
            # Реализация вывода списка пользователей
            pass
        elif choice == "2":
            # Реализация удаления пользователя
            pass
        elif choice == "3":
            # Реализация добавления нового пользователя
            pass
        elif choice == "4":
            # Реализация смены своего пароля
            pass
        elif choice == "5":
            print("Выход из учетной записи")
            break
        else:
            print("Некорректный ввод")
