import os


def display_patient(patient_dict):
    os.system('cls')
    print("| uid|   Name          |")
    print("|----+-----------------|")
    for item in patient_dict:
        print(
            f"|{patient_dict[item]['uid'] : >3} | {patient_dict[item]['name'] : <15} |")
        print("|----+-----------------|")


if __name__ == '__main__':
    display_patient()
