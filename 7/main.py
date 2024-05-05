import hashlib
import database
import identify
import authentication as auth

if __name__ == "__main__":
    while True:
        try:
            TEXT = "\nРежим работы:\n1) Вход;\n2) Зарегистироваться;\n3) Выход.\n\nВвод: "
            mode = int(input(TEXT))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        if mode == 3:
            break

        try:
            LOGIN = str(input("Введите логин: "))
        except ValueError:
            print("\nНеверный тип данных.")

        try:
            PASSWORD = str(input("Введите пароль: "))
        except ValueError:
            print("\nНеверный тип данных.")

        print('\n')

        db = database.DataBase('test.db')

        if mode == 2:
            if identify.is_user_exists(db, LOGIN):
                print('Пользователь с таким логином существует!')

                continue

            INSERT_QUERY = "INSERT INTO Users (login, password, utype_id) VALUES (?,?,?);"
            HASHED = hashlib.md5(PASSWORD.encode('utf-8')).hexdigest()
            cursor = db.cursor()
            cursor.execute(INSERT_QUERY, (LOGIN, HASHED, 0))
            db.commit()
            cursor.close()

            print('Вы успешно прошли регистрацию!')

            continue

        if auth.auth(db, LOGIN, PASSWORD) is False:
            print('Неверный логин или пароль!')

            continue

        cursor = db.cursor()
        cursor.execute(f'SELECT utype_id FROM Users WHERE login = "{LOGIN}"')

        user_type = cursor.fetchall()[0][0]
        cursor.close()
        if user_type == 0:
            print("Вы вошли с правами пользователя!")

            while True:
                try:
                    TEXT = "\nРежим работы:\n1) Сменить пароль;\n2) Выйти с аккаунта.\n\nВвод: "
                    user_mode = int(input(TEXT))
                except ValueError:
                    print("\nНеверный тип данных.")

                    continue

                if user_mode == 2:
                    break

                try:
                    PASSWORD = str(input("Введите новый пароль: "))
                except ValueError:
                    print("\nНеверный тип данных.")

                print('\n')

                HASHED = hashlib.md5(PASSWORD.encode('utf-8')).hexdigest()
                cursor = db.cursor()
                cursor.execute(f'UPDATE Users SET password = "{HASHED}" WHERE login = "{LOGIN}"')
                db.commit()
                cursor.close()

                print("Вы успешно сменили пароль!")

        else:
            print("Вы вошли с правами администратора!")

            while True:
                try:
                    TEXT = "\nРежим работы:\
                            \n1) Вывести список пользователей;\
                            \n2) Удалить пользователя;\
                            \n3) Добавить пользователя;\
                            \n4) Сменить пароль;\
                            \n5) Выйти с аккаунта.\
                            \n\nВвод: "
                    user_mode = int(input(TEXT))
                except ValueError:
                    print("\nНеверный тип данных.")

                    continue

                if user_mode == 5:
                    break

                print("\n")

                if user_mode == 1:
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM Users")
                    respond = cursor.fetchall()
                    cursor.close()

                    for row in respond:
                        TEXT = f"Пользователь: {row[1]},\
                                Админ?: {bool(row[3])}"
                        print(TEXT)
                elif user_mode == 2:
                    try:
                        VICTIM_LOGIN = str(input("Введите логин удаляемого пользователя: "))
                    except ValueError:
                        print("\nНеверный тип данных.")

                    print('\n')

                    if not identify.is_user_exists(db, VICTIM_LOGIN):
                        print(f'Пользователя с логином "{VICTIM_LOGIN}" не существует!')

                        continue

                    cursor = db.cursor()
                    cursor.execute(f'DELETE FROM Users WHERE login = "{VICTIM_LOGIN}"')
                    db.commit()
                    cursor.close()

                    print("Пользователь успешно удалён!")

                elif user_mode == 3:
                    try:
                        NEW_LOGIN = str(input("Введите логин: "))
                    except ValueError:
                        print("\nНеверный тип данных.")

                    try:
                        NEW_PASSWORD = str(input("Введите пароль: "))
                    except ValueError:
                        print("\nНеверный тип данных.")

                    while True:
                        try:
                            NEW_TYPE = int(input("Сделать пользователя администратором (0/1): "))
                        except ValueError:
                            print("\nНеверный тип данных.")

                            continue

                        break

                    print('\n')

                    if identify.is_user_exists(db, NEW_LOGIN):
                        print('Пользователь с таким логином существует!')

                        continue

                    INSERT_QUERY = "INSERT INTO Users (login, password, utype_id) VALUES (?,?,?);"
                    HASHED = hashlib.md5(NEW_PASSWORD.encode('utf-8')).hexdigest()
                    cursor = db.cursor()
                    cursor.execute(INSERT_QUERY, (NEW_LOGIN, HASHED, NEW_TYPE))
                    db.commit()
                    cursor.close()

                elif user_mode == 4:
                    try:
                        PASSWORD = str(input("Введите новый пароль: "))
                    except ValueError:
                        print("\nНеверный тип данных.")

                    print('\n')

                    HASHED = hashlib.md5(PASSWORD.encode('utf-8')).hexdigest()
                    query = f'UPDATE Users SET password = "{HASHED}" WHERE login = "{LOGIN}"'
                    cursor = db.cursor()
                    cursor.execute(query)
                    db.commit()
                    cursor.close()

                    print("Вы успешно сменили пароль!")
