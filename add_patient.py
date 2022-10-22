import time
import config
import display


def addPatient():
    print("\n---------Enter Patient Datils----------")
    name = input('Name = ')
    gender = input('Gender = ')
    age = input('Age = ')
    mobile = input('Mobile = ')
    address = input('Address = ')
    medical_history = input('Medical History = ')
    if upload_addPatient(name=name, gender=gender, age=age, mobile=mobile, address=address, medical_history=medical_history):
        print("\nSaving.....")
        time.sleep(1)
        display.display_patient_list()
    return False


def upload_addPatient(name, gender, age, mobile, address, medical_history):

    try:
        database = config.get_database()
        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_ADD_PATIENT,
                         (name, gender, age, mobile, address, medical_history))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


if __name__ == '__main__':
    print(addPatient('Naruto Uzumaki', 'male', '24',
          '9876543210', 'Leaf Village', 'being dumb'))
