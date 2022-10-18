import mysql.connector
DATABASE_ADDERESSS = '127.0.0.1'
DATABASSE_USERNAME = 'root'
DATABASE_NAME = 'hospital'
DATABASSE_PASSWORD = ''

QUERRY_GET_PATIENT = "select ID, name, mobile, gender, age, medical_condition from tblpatient"
QUERRY_LOGIN = "SELECT username, password FROM login WHERE username=%s AND password= %s"


def get_database():
    mydatabase = mysql.connector.connect(
        host=DATABASE_ADDERESSS,
        user=DATABASSE_USERNAME,
        password=DATABASSE_PASSWORD,
        database=DATABASE_NAME
    )

    return mydatabase
