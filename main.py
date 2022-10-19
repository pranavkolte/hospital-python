import add_patient
import os
import login
import display
import get_patient
import time


def executeChoice(choice):
    os.system('cls')
    if choice == 1:
        print("Loading Patient List.....")
        patient_dict = get_patient.fetch_list()
        return display.display_patient(patient_dict)
    elif choice == 2:
        return add_patient.addPatient()
    else:
        print("enter valid choice\n")
        getChoice()


def getChoice():
    while True:
        os.system('cls')
        try:
            choice = int(
                input("1.show patient \n2.add patient \n \nEnter your choice : "))
            print('wait a moment')
            time.sleep(1)
            return executeChoice(choice)

        except ValueError:
            print("enter number only\n")


def login_main():

    while True:
        username = input('Enter username : ')
        password = input('Enter password : ')
        result = login.login(username, password)
        if result:
            print('Login successfull!!!\n')
            time.sleep(2)
            return True
        else:
            print('Wrong credentials. Try again. \n')


def main():
    if login_main():
        getChoice()


if __name__ == '__main__':
    main()
