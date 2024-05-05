'''Auth user script file'''

import hashlib
import database
import identify

def auth(db: database.DataBase, login, password) -> bool:

    if not identify.is_user_exists(db, login):
        return False

    hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

    cursor = db.cursor()
    cursor.execute(f'SELECT password FROM Users WHERE login = "{login}"')
    db_password = cursor.fetchall()[0][0]
    cursor.close()

    return hashed == db_password
