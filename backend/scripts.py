from datetime import datetime
import sqlalchemy_connect as db


def get_library_name(items: dict, library_id: int):
    item = items.get(library_id)
    if item:
        return item
    return -1


def cur_data():
    return str(datetime.now())[:11]


def get_table_name(user_type: str):
    match user_type:
        case 'студент':
            return 'students'
        case 'пенсионер':
            return 'pensioners'
        case 'пользователь':
            return 'peoples'
        case 'школьник':
            return 'schools'
        case 'научный работник':
            return 'scientists'
        case 'преподаватель':
            return 'teachers'


def add_user(req_data: dict, table_name: str, connection):
    match table_name:
        case 'students':
            db.add_student(req_data, connection)
        case 'teachers':
            db.add_teacher(req_data, connection)
        case 'peoples':
            db.add_people(req_data, connection)
        case 'schools':
            db.add_school(req_data, connection)
        case 'scientists':
            db.add_scientist(req_data, connection)
        case 'pensioners':
            db.add_pensioner(req_data, connection)


def get_not_null_values(data, columns):
    result = {}
    for item in data:
        if item[1] is not None:
            for column in columns:
                if item[0] in column:
                    result.update({column: item[1]})
    return result