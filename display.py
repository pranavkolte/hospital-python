import os
import get_patient
import main
import update_patient


def show_patient(patient_dict):
    os.system('cls')
    print("| UID|   Name          |")
    print("|----+-----------------|")
    num = 0
    for UID in patient_dict:
        num = UID
        print(
            f"|{patient_dict[UID]['uid'] : >3} | {patient_dict[UID]['name'] : <15} |")
        print("|----+-----------------|")
    return num


def display_patient_list(patient_dict):
    os.system('cls')
    print("| UID|   Name          |")
    print("|----+-----------------|")
    num = 0
    for UID in patient_dict:
        num = UID
        print(
            f"|{patient_dict[UID]['uid'] : >3} | {patient_dict[UID]['name'] : <15} |")
        print("|----+-----------------|")
    # print(f"\n\n {len(patient_dict.keys())}")
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
    print("| uid|   Name          | Gender| Age|                         Medical History                          |")
    print("|----+-----------------+-------+----+------------------------------------------------------------------|")
    print(
        f"""|{patient_dict[uid]['uid'] : >3} | {patient_dict[uid]['name'] : <15} | {patient_dict[uid]['gender'] : <6}| {patient_dict[uid]['age'] : <3}| {patient_dict[uid]['medical_history'] : <65}|""")
    print("|----+-----------------+-------+----+------------------------------------------------------------------|\n\n")
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
