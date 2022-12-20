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
    return {
        'студент': 'students',
        'пенсионер': 'pensioners',
        'пользователь': 'peoples',
        'школьник': 'schools',
        'научный работник': 'scientists',
        'преподаватель': 'teachers'
    }.get(user_type)


def add_user(req_data: dict, table_name: str, connection):
    if table_name == 'students':
        db.add_student(req_data, connection)
    elif table_name == 'teachers':
        db.add_teacher(req_data, connection)
    elif table_name == 'peoples':
        db.add_people(req_data, connection)
    elif table_name == 'schools':
        db.add_school(req_data, connection)
    elif table_name == 'scientists':
        db.add_scientist(req_data, connection)
    elif table_name == 'pensioners':
        db.add_pensioner(req_data, connection)


def get_not_null_values(data, columns):
    result = {}
    for item in data:
        if item[1] is not None:
            for column in columns:
                if item[0] in column:
                    result.update({column: item[1]})
    return result


def get_correct_columns(columns):
    array = [column for column in columns if 'id' not in column and 'date' not in column ]
    return ' '.join(array)


def get_selected_values(table_name: str, connection):
    columns = db.get_columns({'tablename': table_name}, connection)
    user_columns = db.get_columns({'tablename': 'users'}, connection)
    correct_columns = get_correct_columns(columns)
    user_correct_columns = get_correct_columns(user_columns)
    select = correct_columns + ' ' + user_correct_columns
    return ', '.join(select.split())

