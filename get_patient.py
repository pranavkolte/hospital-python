import mysql.connector
import config


def convert_result(li):
    if not li:
        return None
    raw = []
    for record in li:
        raw.append(list(record))
    return set_result(raw)


def set_result(li):
    new_dict = {}
    for item in li:
        keyy = li.index(item)
        uid = 'none'
        name = 'none'
        mobile = 'none'
        gender = 'none'
        age = 'none'
        con = 'none'
        for id, val in enumerate(item):
            if id == 0:
                uid = str(val)
            if id == 1:
                name = str(val)
            if id == 2:
                mobile = str(val)
            if id == 3:
                gender = str(val)
            if id == 4:
                age = str(val)
            if id == 5:
                con = str(val)
            # print(f"{li.index(item)} - {id} : {val}")
        new_dict[keyy] = {"uid": uid,
                          "name": name,
                          "mobile": mobile,
                          "gender": gender,
                          "age": age,
                          "con": con}

    return new_dict


def fetch_list():
    database = config.get_database()
    cur = database.cursor()
    cur.execute(config.QUERRY_GET_PATIENT)
    p_list = cur.fetchall()
    if p_list:
        return convert_result(p_list)
    else:
        return None


if __name__ == '__main__':
    n = fetch_list()
    print("| uid|   Name          |")
    print("------------------------")
    for item in n:
        print(f"|{n[item]['uid'] : >3} | {n[item]['name'] : <15} |")
