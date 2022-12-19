from sqlalchemy import create_engine, text
from session import get_session
from scripts import cur_data


def get_libraries(connection):
    return {i: j for i, j in connection.execute(
        text("SELECT l_id, name FROM libraries")).fetchall()}

# def pop(connection,d1,d2,d3,d4):
#     data = {
#         'd1': d1,
#         'd2': d2,
#         'd3': d3,
#         'd4': d4
# 
#     }
#     return connection.execute(
#         text(
#             "SELECT b_id, b_type, quantity, books.b_name FROM books JOIN authors ON books.a_id = authors.a_id")).fetchall()


def get_columns(req_data: dict, connection):
    data = {
        'tablename': req_data.get('tablename')
    }
    return [i for i in connection.execute(
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
        text("INSERT INTO users(u_last_date, u_fio, id_library, u_type) VALUES(:u_last_data,:u_fio, :id_library, :u_type)"),
        **data)
    return connection.execute(text("SELECT max(u_id) from users")).fetchone()[0]


# def get_authors(connection):
#     return {a_id: {"author_fio": author_fio, "book_name": book_name} for a_id, author_fio, book_name in connection.execute(
#         text("SELECT a_id, authors_fio, b_name FROM authors")).fetchall()}
def get_authors(connection):
    return [[a_id, authors, b_name] for a_id, authors, b_name in connection.execute(text("SELECT a_id, authors_fio, b_name FROM authors")).fetchall()]
print(get_authors(get_session()))
def get_books(connection):
    return {b_id: {"type": b_type, "quantity": quantity, "book_name": book_name, "author": authors_fio, "shelf": sh_id, "hall":h_id, "library": l_id} for b_id, b_type, quantity, book_name, authors_fio, sh_id, h_id, l_id in connection.execute(
        text("""SELECT b_id, b_type, quantity, books.b_name, authors_fio, shelves.sh_id, number_hall, location FROM books 
                 JOIN authors ON books.a_id = authors.a_id
                 JOIN publication ON book_id = b_id 
                 JOIN shelves ON publication.sh_id = shelves.sh_id
                 JOIN halls ON halls.h_id = shelves.h_id
                 JOIN libraries ON libraries.l_id = halls.l_id""")).fetchall()}


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
        't_university': req_data.get('university'),
        't_faculty': req_data.get('faculty'),
        't_rank': req_data.get('rank'),
    }
    connection.execute(text(
        "INSERT INTO teachers(user_id, t_university, t_faculty, t_rank) VALUES (:user_id, :t_university, :t_faculty, :t_rank)"),
        **data)


def add_people(req_data: dict, connection):
    data = {
        'user_id': get_user_id(connection, req_data.get('fio'), req_data.get('id_library'), req_data.get('u_type')),
        'p_place': req_data.get('place')
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
        'pen_certificate_number': req_data.get('certificate')
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


def list_charters(table_name: str, connection):
    return connection.execute(text(f"SELECT * FROM users JOIN {table_name} ON u_id = user_id")).fetchall()


def some(req_data: dict, connection):
    """
    req_data = {
        'table_name' = str,
        'b_name' = some value
    }
    """
    ...


def get_borrowed_books(req_data: dict, connection):  # 2-3 запрос
    return {i: j for i, j in connection.execute(text(
        "SELECT u_id, u_fio FROM users JOIN extradition ON u_id = user_id JOIN publication ON p_id = pub_id JOIN books ON book_id = b_id WHERE b_name = :a_book"),
        **req_data).fetchall()}


def list_interval(dates: dict, connection):  # 4 запрос
    return {i: j for i, j in connection.execute(text(
        "SELECT u_fio, b_name FROM users JOIN extradition ON u_id = user_id JOIN publication ON p_id = pub_id JOIN books ON book_id = b_id WHERE :start_date < datetime AND :finish_date > datetime"),
        **dates).fetchall()}


def get_user_info(user_id: int, connection):  # 5 запрос должен передавать id пользователя
    data = {
        'user_id': user_id
    }
    return {i: j for i, j in connection.execute(text("""SELECT u_id, authors.b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN authors ON books.a_id = authors.a_id
                                 JOIN library_workers ON extradition.lw_id = library_workers.lw_id
                                 JOIN libraries ON l_id = l_id
                                 WHERE id_library IN (SELECT id_library FROM users WHERE u_id = :user_id) AND u_id = :user_id"""),
                                                **data).fetchall()}


def get_user_info_library(req_data: dict,
                          connection):
    return {i: j for i, j in connection.execute(text("""SELECT u_id, authors.b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN authors ON books.a_id = authors.a_id
                                 JOIN library_workers ON extradition.lw_id = library_workers.lw_id
                                 JOIN libraries ON libraries.l_id = library_workers.l_id
                                 WHERE id_library NOT IN (SELECT id_library FROM users WHERE u_id = :user_id) AND u_id = :user_id"""),
                                                **req_data).fetchall()}


def get_books_from_shelf(req_data: dict, connection):  # 7 запрос
    return {i: j for i, j in connection.execute(text("""SELECT u_id, b_name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON shelves.sh_id = publication.sh_id
                                 WHERE s_id = :shelf"""), **req_data).fetchall()}


def get_serviced_users(req_data: dict, connection):  # 8 запрос
    return {i: j for i, j in connection.execute(text("""SELECT u_id,u_fio FROM extradition     
                                 JOIN users ON user_id = u_id
                                 WHERE lw_id = :worker"""), **req_data).fetchall()}


def get_worker_production(req_data: dict, connection):  # 9 запрос
    return {i: j for i, j in
            connection.execute(text("SELECT lw_id, count(user_id) FROM extradition GROUP BY lw_id"),
                               **req_data).fetchall()}


def get_users_with_deadline(connection):  # 10 запрос
    data = {
        'data': cur_data()
    }
    return {i: j for i, j in connection.execute(
        text("SELECT u_id, u_fio FROM extradition JOIN users ON user_id = u_id WHERE deadline < :data"),
        **data).fetchall()}


def get_scrapped_books(connection):  # 11 запрос
    return {i: j for i, j in connection.execute(text("""SELECT b_id, b_name FROM decommissioned 
                                JOIN publication ON decommissioned.pub_id = publication.pub_id
                                JOIN books ON publication.book_id = books.b_id
                            """)).fetchall()}


def get_hall_workers(req_data: dict, connection):  # 12 запрос
    return {i: j for i, j in connection.execute(text("""SELECT library_workers.lw_id, library_workers.lw_fio FROM library_workers 
                                 JOIN libraries ON libraries.l_id = library_workers.l_id
                                 JOIN halls ON halls.l_id = libraries.l_id
                                 WHERE halls.h_id = :h_id"""), **req_data).fetchall()}


def get_overdue_users(connection):  # 13 запрос
    data = {
        'data': cur_data()
    }
    return {i: j for i, j in connection.execute(text("""SELECT u_id, u_fio FROM extradition 
                                 JOIN users ON u_id = user_id
                                 WHERE deadline < :data"""), **data).fetchall()}


# rework
def get_inventory_numbers_by_book(req_data: dict, connection):  # 14 запрос
    return {b_name: ["shelf", shelf_id, "hall", number_hall, "library", name] for b_name, shelf_id, number_hall, name
            in connection.execute(text("""SELECT b_name, sh_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON shelves.sh_id = publication.sh_id
                                 JOIN halls ON shelves.h_id = halls.h_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 WHERE b_name = :book"""), **req_data).fetchall()}


# rework
def get_inventory_numbers_by_author(req_data: dict, connection):  # 15 запрос
    return {a_name: ["shelf", shelf_id, "hall", number_hall, "library", name] for a_name, shelf_id, number_hall, name
            in connection.execute(text("""SELECT authors_fio, sh_id, number_hall, libraries.name FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 JOIN shelves ON shelves.sh_id = publication.sh_id
                                 JOIN halls ON shelves.hall_id = halls.hall_id
                                 JOIN libraries ON halls.l_id = libraries.l_id
                                 JOIN authors ON authors.a_id = books.a_id
                                      WHERE authors_fio = :data"""), **req_data).fetchall()}


def get_popular_books(connection):  # 16 запрос
    return connection.execute(text("""SELECT max(b_name) FROM users
                                 JOIN extradition ON u_id = user_id
                                 JOIN publication ON p_id = pub_id
                                 JOIN books ON book_id = b_id
                                 GROUP BY b_name""")).fetchall()

# dit = {
#         "fio":"fff",
#         "id_library": 5,
#         "u_type": "школьние",
#         "certificate": 234
#     }
#
# print(add_pensioner(dit, get_session()))
