import login
import display
import get_patient


def getChoice():
    patient_dict = get_patient.fetch_list()
    display.display_patient(patient_dict)
    # choice = input("show patient details of : ")


def get_login_cred():

    while True:
        username = input('Enter username : ')
        password = input('Enter password : ')
        result = login.login(username, password)
        if result:
            print('Login successfull!!!')
            getChoice()
            break
        else:
            print('Wrong credentials. Try again.')


def main():
    get_login_cred()


if __name__ == '__main__':
    main()
