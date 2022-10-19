import mysql.connector
DATABASE_HOST = 'remotemysql.com'
DATABASSE_USER = 'LKxXNksPlP'
DATABASE_NAME = 'LKxXNksPlP'
DATABASSE_PASSWORD = 'LGh76olfte'
PORT = '3360'

QUERRY_LOGIN = "SELECT username, password FROM login WHERE username=%s AND password= %s"
QUERRY_GET_PATIENT = "select ID, name, mobile, gender, age, medical_history from patient"
QUERRY_ADD_PATIENT = "INSERT INTO patient (name, gender, age, mobile, address, medical_history) VALUES (%s, %s, %s, %s, %s, %s)"


def get_database():
    mydatabase = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASSE_USER,
        password=DATABASSE_PASSWORD,
        database=DATABASE_NAME,
    )
    return mydatabase
