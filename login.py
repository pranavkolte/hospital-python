import hashlib
import config
import main


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password


def check_status():
    database = config.get_database()
    cursor = database.cursor()
    cursor.execute(config.QUERRY_CHECK_LOGIN_STATUS)
    result = cursor.fetchall()
    if result:
        IP = result[0][0]
        status = result[0][1]
        if IP == config.CURRENT_IP and status == 1:
            return True
        else:
            return False


def login(username, password):
    try:

        database = config.get_database()
        if not database:
            print('something wrong with connection')
            return False
        print("\nLoggin in...")
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_LOGIN, (username, getSHA(password)))
        result = mycursor.fetchall()
        if result:
            mycursor.execute(config.QUERRY_SET_LOGIN_STATUS,
                             (config.CURRENT_IP, 1, result[0][0]))
            database.commit()
            return True
        else:
            return False
    except:
        database.rollback()
        return False
    finally:
        database.close()


def logout():
    try:
        database = config.get_database()
        cursor = database.cursor()
        cursor.execute(config.QUERRY_LOGOUT, (0, 1))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


if __name__ == '__main__':
    # print(login('user', '123456'))
    # print(check_status())
    print(logout())
