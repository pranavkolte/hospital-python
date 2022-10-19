import hashlib
import config


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password


def login(username, password):
    database = config.get_database()
    if not database:
        print('something wrong with connection')
        return False
    mycursor = database.cursor()
    mycursor.execute(config.QUERRY_LOGIN, (username, getSHA(password)))
    result = mycursor.fetchall()
    if result:
        return True
    else:
        return False


if __name__ == '__main__':
    print(login('user', '123456'))
