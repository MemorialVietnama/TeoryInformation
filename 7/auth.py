import hashlib

def hash_password(password):
    # Хеширование пароля с использованием алгоритма MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def authenticate_user(login, password, users):
    # Проверка наличия пользователя в базе
    if login in users:
        # Получение хеша пароля из базы данных
        stored_hashed_password = users[login]
        # Хеширование введенного пароля для сравнения с хешем из базы
        hashed_password = hash_password(password)
        # Проверка соответствия хешей
        if stored_hashed_password == hashed_password:
            return True
    return False

