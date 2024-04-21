def register_user(users, login, password):
    if login not in users:
        users[login] = password
        print("Новый пользователь зарегистрирован")
    else:
        print("Пользователь с логином", login, "уже существует")

def change_own_password(users, login, new_password):
    if login in users:
        users[login] = new_password
        print("Пароль успешно изменен")
    else:
        print("Пользователь с логином", login, "не найден")
