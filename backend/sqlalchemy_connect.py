from sqlalchemy import create_engine, text
from scripts import cur_data
import hashlib


def check_logpass(password, login, connection):
    log, paswd = [[log, pas] for log, pas in connection.execute(text("SELECT login, password FROM users")).fetchall()]
    hash_pass, hash_login = hashlib.md5(password.encode()), hashlib.md5(password.encode())


def get_libraries(connection):
    return {i: j for i, j in connection.execute(
        text("SELECT l_id, name FROM libraries")).fetchall()}


def get_columns(req_data: dict, connection):
    data = {
        'tablename': req_data.get('tablename')
    }
    return [str(i[0]) for i in connection.execute(
        text("""SELECT column_name
                FROM information_schema.columns
                WHERE TABLE_NAME = :tablename
                ORDER BY ordinal_position;"""), **data).fetchall()]


def get_user_id(connection, fio, id_library, u_type):
    data = {
        'u_last_data': cur_data(),
        'u_fio': fio,
        'id_library': id_library,
        'u_type': u_type
    }
    connection.execute(
        text(
            "INSERT INTO users(u_last_date, u_fio, id_library, u_type) VALUES(:u_last_data,:u_fio, :id_library, :u_type)"),
        **data)
    return connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]


def get_authors(connection):
    return {authors_fio: {"genre": genre, "b_type": b_type, "b_name": b_name} for authors_fio, genre, b_type, b_name in
            connection.execute(
                text(
                    "SELECT authors_fio, string_agg(genre, ','), string_agg(b_type, ','), string_agg(b_name, ',') FROM authors JOIN books ON books.a_id = authors.a_id GROUP BY authors_fio")).fetchall()}


def get_books(connection):
    return connection.execute(
            text("""SELECT b_id, b_type, genre, quantity, books.b_name, authors_fio, shelves.sh_id, number_hall, location FROM books 
                 JOIN authors ON books.a_id = authors.a_id
                 JOIN shelves ON books.sh_id = shelves.sh_id
                 JOIN halls ON halls.h_id = shelves.h_id
                 JOIN libraries ON libraries.l_id = halls.l_id""")).fetchall()


def add_student(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        's_university': req_data.get('university'),
        's_course': req_data.get('course'),
        's_faculty': req_data.get('faculty'),
    }
    connection.execute(text(
        "INSERT INTO students(user_id, s_university, s_course, s_faculty) VALUES (:user_id,:s_university, :s_course, :s_faculty)"),
        **data)


def add_teacher(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        't_university': req_data.get('t_university'),
        't_faculty': req_data.get('t_faculty'),
        't_rank': req_data.get('t_rank'),
    }
    connection.execute(text(
        "INSERT INTO teachers(user_id, t_university, t_faculty, t_rank) VALUES (:user_id, :t_university, :t_faculty, :t_rank)"),
        **data)


def add_people(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        'p_place': req_data.get('p_place')
    }
    connection.execute(text("INSERT INTO peoples(user_id, p_place) VALUES (:user_id, :p_place)"), **data)


def add_school(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        'school': req_data.get('school'),
        'sc_class': req_data.get('sc_class')
    }
    connection.execute(text("INSERT INTO schools(user_id, school, sc_class) VALUES (:user_id, :school, :sc_class)"),
                       **data)


def add_library_worker(req_data: dict, connection):
    data = {
        'u_last_date': cur_data(),
        'u_fio': req_data.get('fio'),
        'id_library': req_data.get('id_library')
    }
    connection.execute(
        text("INSERT INTO users(u_last_data, u_fio, id_library) VALUES(:u_last_data,:u_fio, :id_library)"), **data)
    user_id = connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]
    data = {
        'user_id': user_id,
        'library': req_data.get('library'),
        'number_room': req_data.get('number_room')
    }
    connection.execute(
        text("INSERT INTO library_workers(user_id, library, number_room) VALUES (:user_id, :library, :number_room)"),
        **data)


def add_pensioner(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        'pen_certificate_number': req_data.get('pen_certificate_number')
    }
    connection.execute(
        text("INSERT INTO Pensioners(user_id, pen_certificate_number) VALUES (:user_id, :pen_certificate_number)"),
        **data)


def add_scientist(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        'organization': req_data.get('organization'),
        'theme': req_data.get('theme')
    }
    connection.execute(
        text("INSERT INTO scientists(user_id, organization, theme) VALUES (:user_id, :organization, :theme)"),
        **data)


def get_all_users(connection):
    return [{"u_last_date": u_last_date, "u_fio": u_fio, "u_type": u_type} for u_last_date, u_fio, u_type in
            connection.execute(text(f"SELECT u_last_date, u_fio, u_type FROM users ")).fetchall()]


def list_charters(search_values: dict, table_name: str, select_string: str, connection):
    string = ''
    if search_values and search_values:
        items = search_values.items()
        for index, item in enumerate(items):
            string += f" {item[0]} = '{item[1]}' "
            if len(items) > 0 and index < len(items) - 1:
                string += 'AND'
        return connection.execute(text(
            f"SELECT {select_string} FROM users JOIN {table_name} ON u_id = user_id WHERE {string.strip()}")).fetchall()
    else:
        return connection.execute(text(
            f"SELECT {select_string} FROM users JOIN {table_name} ON u_id = user_id")).fetchall()


def list_users(table_name: str, connection):
    return connection.execute(
        text(f"SELECT dic['values'] FROM users JOIN {table_name} ON u_id = user_id")).fetchall()


def get_borrowed_books(req_data: dict, connection):  # 2 запрос
    return connection.execute(text(
        "SELECT u_fio, u_type FROM users JOIN extradition ON u_id = user_id JOIN books ON books.b_id = extradition.b_id WHERE LOWER(b_name) = LOWER(:a_book)"),
                              **req_data).fetchall()


def get_borrowed_type_books(req_data: dict, connection):  # 3 запрос
    return connection.execute(text(
        "SELECT u_fio, u_type  FROM users JOIN extradition ON u_id = user_id JOIN books ON books.b_id = extradition.b_id WHERE LOWER(b_name) = LOWER(:b_type)"),
                              **req_data).fetchall()


def list_interval(dates: dict, connection):  # 4 запрос
    return connection.execute(text(
        "SELECT u_fio, b_name FROM users JOIN extradition ON u_id = user_id JOIN books ON books.b_id = extradition.b_id WHERE :start_date < start_date AND :finish_date > start_date"),
        **dates).fetchall()


def get_user_info(req_data: dict, connection):  # 5
    return connection.execute(text("""SELECT u_id, b_name FROM users
      JOIN extradition ON u_id = user_id
      JOIN books ON books.b_id = extradition.b_id
      JOIN authors ON books.a_id = authors.a_id
      JOIN library_workers ON extradition.lw_id = library_workers.lw_id
      JOIN libraries ON libraries.l_id = library_workers.l_id
      WHERE id_library IN (SELECT id_library FROM users WHERE u_fio = :u_fio) AND u_fio = :u_fio"""),
                                                **req_data).fetchall()


def get_user_info_library(req_data: dict, connection):# 6 запрос
    return connection.execute(text("""SELECT u_id, b_name FROM users
      JOIN extradition ON u_id = user_id
      JOIN books ON books.b_id = extradition.b_id
      JOIN authors ON books.a_id = authors.a_id
      JOIN library_workers ON extradition.lw_id = library_workers.lw_id
      JOIN libraries ON libraries.l_id = library_workers.l_id
      WHERE id_library NOT IN (SELECT id_library FROM users WHERE u_fio = :u_fio) AND u_fio = :u_fio"""),
                                                **req_data).fetchall()


def get_books_from_shelf(req_data: dict, connection):  # 7 запрос
    return connection.execute(text("""SELECT u_id, u_fio, b_name, number_hall, name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN books ON books.b_id = extradition.b_id
                                 JOIN shelves ON shelves.sh_id = books.sh_id
                                 JOIN halls ON halls.h_id = shelves.h_id
                                 JOIN libraries ON libraries.l_id = halls.l_id
                                 WHERE shelves.sh_id = :shelf"""), **req_data).fetchall()


def get_serviced_users(req_data: dict, connection):  # 8 запрос
    return connection.execute(text("""SELECT u_id, u_fio FROM extradition     
                                 JOIN users ON user_id = u_id
                                 WHERE lw_fio = :worker"""), **req_data).fetchall()


def get_worker_production(connection):  # 9 запрос
    return connection.execute(text("""SELECT library_workers.lw_id, count(user_id) FROM extradition 
                                         JOIN library_workers ON library_workers.lw_id = extradition.lw_id
                                         GROUP BY library_workers.lw_id""")).fetchall()


def get_users_with_deadline(connection):  # 10 запрос
    data = {
        'data': cur_data()
    }
    return connection.execute(
        text("SELECT u_id, u_fio FROM extradition JOIN users ON user_id = u_id WHERE finish_date< :data"),
        **data).fetchall()


def get_scrapped_books(connection):  # 11 запрос
    return connection.execute(text("""SELECT books.b_id, b_name FROM decommissioned 
                                JOIN books ON books.b_id = decommissioned.b_id
                            """)).fetchall()


def get_hall_workers(req_data: dict, connection):  # 12 запрос
    return connection.execute(text("""SELECT library_workers.lw_id, library_workers.lw_fio FROM library_workers 
                                 JOIN libraries ON libraries.l_id = library_workers.l_id
                                 JOIN halls ON halls.l_id = libraries.l_id
                                 WHERE halls.number_hall = :number_hall"""), **req_data).fetchall()


def get_overdue_users(connection):  # 13 запрос
    data = {
        'data': cur_data()
    }
    return connection.execute(text("""SELECT u_id, u_fio FROM extradition 
                                 JOIN users ON u_id = user_id
                                 WHERE finish_date < :data"""), **data).fetchall()


def get_inventory_numbers_by_book(req_data: dict, connection):  # 14 запрос
    return {b_name: ["shelf", shelf_id, "hall", number_hall, "library", name] for b_name, shelf_id, number_hall, name
            in connection.execute(text("""SELECT b_name, shelves.sh_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN books ON books.b_id = extradition.b_id
                                 JOIN shelves ON shelves.sh_id = books.sh_id
                                 JOIN halls ON shelves.h_id = halls.h_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 WHERE b_name = :book"""), **req_data).fetchall()}


def get_inventory_numbers_by_author(req_data: dict, connection):  # 15 запрос
    return {a_name: ["shelf", shelf_id, "hall", number_hall, "library", name] for a_name, shelf_id, number_hall, name
            in connection.execute(text("""SELECT authors_fio, shelves.sh_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN books ON books.b_id = extradition.b_id
                                 JOIN shelves ON shelves.sh_id = books.sh_id
                                 JOIN halls ON shelves.h_id = halls.h_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 JOIN authors ON authors.a_id = books.a_id
                                      WHERE authors_fio = :data"""), **req_data).fetchall()}


def get_popular_books(connection):  # 16 запрос
    return connection.execute(text("""SELECT max(b_name) FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN books ON extradition.b_id = books.b_id
                                 GROUP BY b_name""")).fetchall()
