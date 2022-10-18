from sys import displayhook
import get_patient


def display_patient(patient_dict):
    print("| uid|   Name          |")
    print("------------------------")
    for item in patient_dict:
        print(
            f"|{patient_dict[item]['uid'] : >3} | {patient_dict[item]['name'] : <15} |")


if __name__ == '__main__':
    display_patient()
