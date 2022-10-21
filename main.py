from cmath import log
import add_patient
import os
import login
import display
import get_patient
import time
import update_patient


def executeChoice(choice):
    os.system('cls')
    if choice == 1:
        print("Loading Patient List.....")
        patient_dict = get_patient.get_list()
        return display.display_patient_list(patient_dict)
    elif choice == 2:
        return add_patient.addPatient()
    elif choice == 3:
        if login.logout():
            login_main()
    else:
        print("enter valid choice\n")
        time.sleep(1)
        return getChoice()


def getChoice():
    while True:
        os.system('cls')
        try:
            choice = int(
                input("1.show patient \n2.add patientv \n3.Log Out\n\nEnter your choice : "))
            print('wait a moment')
            time.sleep(1)
            return executeChoice(choice)

        except ValueError:
            print("enter number only\n")


def login_main():

    if login.check_status():
        return getChoice()

    while True:
        os.system('cls')
        username = input('Enter username : ')
        password = input('Enter password : ')
        result = login.login(username, password)
        if result:
            print('Login successfull!!!\n')
            time.sleep(2)
            return getChoice()
        else:
            print('\n Login Failed. Wrong credentials. Try again. \n')


# def main():
#     login_main()
if __name__ == '__main__':
    login_main()
