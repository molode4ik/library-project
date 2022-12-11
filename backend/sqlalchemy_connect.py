from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from session import get_session
from datetime import datetime


def cur_data():
    return str(datetime.now())[:11]


def get_users(connection):
    users = connection.execute(text("SELECT * from users")).fetchall()
    print(users)


def add_student(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        's_university': req_data.get('university'),
        's_course': req_data.get('course'),
        's_faculty': req_data.get('faculty')
    }
    connection.execute(text(
        "INSERT INTO students(user_id, s_university, s_course, s_faculty) VALUES (:user_id,:s_university, :s_course, :s_faculty)"),
        **data)


def add_teacher(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        't_university': req_data.get('university'),
        't_faculty': req_data.get('faculty'),
        't_rank': req_data.get('rank'),
    }
    connection.execute(text(
        "INSERT INTO teachers(user_id, t_university, t_faculty, t_rank) VALUES (:user_id, :t_university, :t_faculty, :t_rank)"),
        **data)


def add_people(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **dataa)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        'p_place': req_data.get('place')
    }
    connection.execute(text("INSERT INTO peoples(user_id, p_place) VALUES (:user_id, :p_place)"), **data)


def add_school(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        'school': req_data.get('school'),
        'sc_class': req_data.get('sc_class')
    }
    connection.execute(text("INSERT INTO schools(user_id, school, sc_class) VALUES (:user_id, :school, :sc_class)"),
                       **data)


# Переписать
# def add_library_worker(req_data: dict, connection):  # нужна?
#     # создание словаря для добавления (по другому не работает)
#     dataa = {
#         'u_last_date': date,
#         'u_fio': fio,
#         'id_library': id_library
#     }
#     s = text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)")
#     connection.execute(s, **dataa)
#
#     # находим id в юзерсах
#     s = text("SELECT max(u_id) from users")
#     id_users = connection.execute(s)
#     user_id = id_users.fetchone()[0]
#
#     # словарь для добовления
#     dataa2 = {
#         'user_id': user_id,
#         'library': library,
#         'number_room': number_room
#     }
#     s = text("INSERT INTO library_workers(user_id, library, number_room) VALUES (:user_id, :library, :number_room)")
#     connection.execute(s, **dataa2)


def add_pensioner(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        'pen_certificate_number': req_data.get('certificate')
    }
    connection.execute(
        text("INSERT INTO Pensioners(user_id, pen_certificate_number) VALUES (:user_id, :pen_certificate_number)"),
        **data)


def add_scientist(req_data: dict, connection):
    data = {
        'u_last_data': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"),
        **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        'organization': req_data.get('organization'),
        'theme': req_data.get('theme')
    }
    connection.execute(
        text("INSERT INTO scientists(user_id, organization, theme) VALUES (:user_id, :organization, :theme)"),
        **data)


def list_charters(
        data):  # 1 запрос параметр указывай как таблицу тебе выдаст всех юзеров из таблицы тебе надо будет их обработать иначе придется писать кучу запросов
    conn = get_session()
    return conn.execute(text(f"SELECT * FROM users JOIN {data} ON u_id = user_id")).fetchall()


def book_on_hands(a_book):  # 2-3 запрос
    conn = get_session()
    data = {
        'a_book': a_book
    }
    return conn.execute(text(
        "SELECT u_fio FROM users JOIN extradition ON u_id = user_id JOIN publication ON p_id = pub_id JOIN books ON book_id = b_id WHERE b_name = :a_book"),
        **data).fetchall()


def list_interval(data1, data2):  # 4 запрос
    conn = get_session()
    data = {
        'data1': data1,
        'data2': data2
    }
    return conn.execute(text(
        "SELECT u_fio, b_name FROM users JOIN extradition ON u_id = user_id JOIN publication ON p_id = pub_id JOIN books ON book_id = b_id WHERE :data1 < datatime AND :data2 > datatime"),
        **data).fetchall()


def info_users(user_id):  # 5 запрос должен передавать id пользователя
    conn = get_session()
    data = {
        'user_id': user_id
    }
    return conn.execute(text("""SELECT b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN library_workers ON id_workers = lw_id
                                 JOIN libraries ON library_id = l_id
                                 WHERE id_library IN (SELECT id_library FROM users WHERE u_id = :user_id) AND u_id = :user_id"""),
                        **data).fetchall()


def info_users1(user_id):  # 6 запрос должен передавать id пользователя !!! не робит мелкая бд
    conn = get_session()
    data = {
        'name': user_id
    }
    return conn.execute(text("""SELECT b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN library_workers ON id_workers = lw_id
                                 JOIN libraries ON library_id = l_id
                                 WHERE id_library NOT IN (SELECT id_library FROM users WHERE u_id = :user_id) AND u_id = :user_id"""),
                        **data).fetchall()


def book_on_shelf(shelf):  # 7 запрос
    conn = get_session()
    data = {
        'shelf': shelf
    }
    return conn.execute(text("""SELECT b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON s_id = shelf_id
                                 WHERE s_id = :shelf"""), **data).fetchall()


def serviced_users(worker):  # 8 запрос
    conn = get_session()
    data = {
        'worker': worker
    }
    return conn.execute(text("""SELECT u_fio FROM extradition     
                                 JOIN users ON user_id = u_id
                                 WHERE id_workers = :worker"""), **data).fetchall()


def production(data1, data2):  # 9 запрос
    conn = get_session()
    data = {
        'data1': data1,
        'data2': data2
    }
    return conn.execute(text("SELECT count(user_id) FROM extradition GROUP BY id_workers"), **data).fetchall()


def deadline():  # 10 запрос
    conn = get_session()
    data = {
        'data': cur_data()
    }
    return conn.execute(text("SELECT * FROM extradition WHERE deadline < :data"), **data).fetchall()


def write_off():  # 11 запрос
    conn = get_session()
    return conn.execute(text("""SELECT b_name FROM decommissioned 
                                JOIN publication ON decommissioned.book_id = publication.pub_id
                                JOIN books ON publication.book_id = books.b_id
                            """)).fetchall()


def list_worker(data):  # 12 запрос
    conn = get_session()
    data = {
        'data': data
    }
    return conn.execute(text("""SELECT libraries.location, library_workers.lw_id, library_workers.fio_workers FROM library_workers 
                                 JOIN libraries ON library_id = l_id
                                 JOIN halls ON halls.l_id = libraries.l_id
                                 WHERE hall_id = :data"""), **data).fetchall()


def overdue():  # 13 запрос
    conn = get_session()
    data = {
        'data': cur_data()
    }
    return conn.execute(text("""SELECT u_id, u_fio FROM extradition 
                                 JOIN users ON u_id = user_id
                                 WHERE deadline < :data"""), **data).fetchall()


def inventory_book(data):  # 14 запрос
    conn = get_session()
    data = {
        'data': data
    }
    return conn.execute(text("""SELECT b_name, shelf_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON s_id = shelf_id
                                 JOIN halls ON shelves.hall_id = halls.hall_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 WHERE b_name = :data"""), **data).fetchall()


def inventory_author(data):  # 15 запрос
    conn = get_session()
    data = {
        'data': data
    }
    return conn.execute(text("""SELECT authors_fio, shelf_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON s_id = shelf_id
                                 JOIN halls ON shelves.hall_id = halls.hall_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 JOIN authors ON authors.a_id = books.a_id
                                      WHERE authors_fio = :data"""), **data).fetchall()


#

def popular_book():  # 16 запрос
    conn = get_session()
    return conn.execute(text("""SELECT max(b_name) FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 GROUP BY b_name""")).fetchall()

# added_student("Папа", "горхоз", 1, 'ФФАИГР', 3)
# added_pensioners("Рашевский Николай Михайлович", "ГОРХОЗ", "ФАИГР", "зафкафедры", 3)
# print(list_charters("teachers")) 1 запрос student, schools, peoples ....
# print(book_on_hands("Дед")) 2-3 запрос
# print(list_interval('2000-01-01','2222-01-01')) 4 запрос
# print(info_users(3)) 5 запрос
# print(info_users1(3)) 6 запрос не робит бд мелкая
# print(book_on_shelf(1)) 7 запрос
# print(serviced_users(1)) 8 запрос
# print(production("2000-01-01","2222-01-01")) 9 запрос
# print(deadline()) 10 запрос
# print(write_off()) 11 запрос
# print(list_worker(2)) 12 запрос
# print(overdue()) 13 запрос
# print(inventory_book("Дед")) 14 запрос
# print(inventory_author("Пушкин")) 15 запрос
# print(popular_book()) 16 запрос
