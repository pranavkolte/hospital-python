import time
import config
import display
import get_patient
import os
import main


def updateName(UID, name):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_UPDATE_PATIENT_NAME, (name, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateGender(UID, gender):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_UPDATE_PATIENT_GENDER, (gender, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateAge(UID, age):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_UPDATE_PATIENT_AGE, (age, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateMobile(UID, mobile):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_UPDATE_PATIENT_MOBILE, (mobile, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateAddress(UID, address):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_UPDATE_PATIENT_ADDRESS, (address, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateMedical_History(UID, medical_history):
    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(
            config.QUERRY_UPDATE_PATIENT_MEDICAL_HISTORY, (medical_history, UID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def updateAll(UID):
    try:
        name = input("\n\nName = ")
        gender = input("Gender = ")
        age = input("Age = ")
        mobile = input("Mobile = ")
        address = input("Address = ")
        medical_history = input("Medical History = ")
        database = config.get_database()
        mycursor = database.cursor()
        print("updating...")
        mycursor.execute(config.QUERRY_UPDATE_PATIENT, (name,
                         gender, age, mobile, address, medical_history, UID))
        database.commit()
        os.system('cls')
        print("Data Updated Successfully!!!\n\nwait a moment")
        time.sleep(2)
        display.display_patient(UID)
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


def update(uid):
    patient_dict = get_patient.get_list()
    print(
        f"what you want to update \n1.Name = {patient_dict[uid]['name']} \n2.Gender = {patient_dict[uid]['gender']} \n3.Age = {patient_dict[uid]['age']} \n4.Mobile = {patient_dict[uid]['mobile']}\n5.Address = {patient_dict[uid]['address']} \n6.Medical History = {patient_dict[uid]['medical_history']}\n7.All details")
    while True:
        try:
            choice = int(input("Enter your Choice = "))
            if choice == 1:
                name = input("\n\nEnter New Name = ")
                return updateName(uid, name)
            elif choice == 2:
                gender = input("\n\nEnter Gender = ")
                return updateGender(uid, gender)
            elif choice == 3:
                age = input("\n\nEnter Age = ")
                return updateAge(uid, age)
            elif choice == 4:
                mobile = input("\n\nEnter Mobile = ")
                return updateMobile(uid, mobile)
            elif choice == 5:
                address = input("\n\nEnter Address = ")
                return updateAddress(uid, address)
            elif choice == 6:
                medical_history = input("\n\nEnter Medical History = ")
                return updateMedical_History(uid, medical_history)
            elif choice == 7:
                return updateAll(uid)
            else:
                print("Invalid Choice \n enter again")
        except TypeError:
            print("\n Enter Valid Choice")
            continue


if __name__ == '__main__':
    update(12)
