import os
import get_patient


def display_patient_list(patient_dict):
    os.system('cls')
    print("| UID|   Name          |")
    print("|----+-----------------|")
    for item in patient_dict:
        print(
            f"|{patient_dict[item]['uid'] : >3} | {patient_dict[item]['name'] : <15} |")
        print("|----+-----------------|")


def display_patient(uid):
    os.system('cls')
    print('Loadind Patient Details..........\n\n')
    patient_dict = get_patient.get_list()
    print("| uid|   Name          | Gender| Age|     Medical History         |")
    print("|----+-----------------+-------+----+-----------------------------|")
    print(
        f"""|{patient_dict[uid]['uid'] : >3} | {patient_dict[uid]['name'] : <15} | {patient_dict[uid]['gender'] : <6}| {patient_dict[uid]['age'] : <3}| {patient_dict[uid]['medical_history'] : <28}|""")
    print("|----+-----------------+-------+----+-----------------------------|\n\n")


if __name__ == '__main__':
    # display_patient_list(get_patient.get_list())
    display_patient(int(12))
