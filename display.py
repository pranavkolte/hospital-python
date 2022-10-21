import os
import get_patient
import main
import update_patient
from prettytable import PrettyTable


def show_patient(patient_dict):
    os.system('cls')
    patientTable = PrettyTable()
    patientTable.field_names = ["UID", "Name"]
    num = 0
    for UID in patient_dict:
        num = UID
        patientTable.add_row(
            [patient_dict[UID]['uid'], patient_dict[UID]['name']])
    print(patientTable)
    return num


def display_patient_list(patient_dict):
    os.system('cls')
    patientTable = PrettyTable()
    patientTable.field_names = ["UID", "Name"]
    num = 0
    for UID in patient_dict:
        num = UID
        patientTable.add_row(
            [patient_dict[UID]['uid'], patient_dict[UID]['name']])
    print(patientTable)
    while True:
        try:
            choice = int(input("\n\nBack : 0\nPatient UID = "))

            if choice > num:
                print("enter valid choice")
                continue
            elif choice == 0:
                return main.getChoice()
            else:
                return display_patient(choice)

        except TypeError:
            continue


def display_patient(uid):
    os.system('cls')
    print('Loadind Patient Details..........\n\n')
    patient_dict = get_patient.get_list()
    pattient_table = PrettyTable()
    pattient_table.field_names = [
        "UID", "Name", "Gender", "Age", "Medical History"]
    pattient_table.add_row([patient_dict[uid]['uid'],
                           patient_dict[uid]['name'],
                           patient_dict[uid]['gender'],
                           patient_dict[uid]['age'],
                           patient_dict[uid]['medical_history']])
    print(pattient_table)
    while True:
        try:
            choice = int(
                input("\n\npress 0 for back \n1.update patient details \n\nEnter your choice = "))

            if choice == 0:
                return display_patient_list(patient_dict)
            elif choice == 1:
                # update_patient.update()
                return update_patient.update(uid)
            else:
                print("enter valid choice")
                continue

        except TypeError:
            continue


if __name__ == '__main__':
    display_patient_list(get_patient.get_list())
    # display_patient(int(17))
