import mysql.connector
import socket


DATABASE_HOST = '<hostname>'
DATABASSE_USER = '<username>'
DATABASE_NAME = '<database name>'
DATABASSE_PASSWORD = '<password>'

QUERRY_CHECK_LOGIN_STATUS = "SELECT IP, status FROM login"
QUERRY_LOGIN = "SELECT ID, username, password FROM login WHERE username=%s AND password= %s"
QUERRY_SET_LOGIN_STATUS = "UPDATE login SET IP=%s, status=%s WHERE ID=%s"
QUERRY_LOGOUT = "UPDATE login SET status=%s WHERE ID=%s"
QUERRY_GET_PATIENT = "select ID, name, mobile, gender, age, medical_history, address from patient"
QUERRY_ADD_PATIENT = "INSERT INTO patient (name, gender, age, mobile, address, medical_history) VALUES (%s, %s, %s, %s, %s, %s)"
QUERRY_UPDATE_PATIENT = "UPDATE patient SET name=%s, gender=%s, age=%s, mobile=%s, address=%s, medical_history=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_NAME = "UPDATE patient SET name=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_GENDER = "UPDATE patient SET gender=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_AGE = "UPDATE patient SET age=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_MOBILE = "UPDATE patient SET mobile=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_ADDRESS = "UPDATE patient SET address=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_MEDICAL_HISTORY = "UPDATE patient SET medical_history=%s WHERE ID=%s"

CURRENT_IP = socket.gethostbyname(socket.gethostname())


def get_database():
    mydatabase = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASSE_USER,
        password=DATABASSE_PASSWORD,
        database=DATABASE_NAME,
    )
    if mydatabase:
        return mydatabase
    else:
        print('Cannot connect to database :-(')
        return None
