import sqlalchemy_connect as db
import api_models as models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from session import get_session, check_connection
import scripts

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup():
    global connection
    connection = None
    connection = get_session()


@app.post('/api/get_readers')
async def get_readers():
    """
        Возвращает всех юзеров
    """
    try:
        result = db.get_all_users(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_users')
async def get_users(user: models.UserData):
    """
        Первый запрос
        Принимает тип юзера, а также необязательные значения в зависимости от типа
        Получить список читателей с заданными характеристиками: студентов указанного учебного заведения, факультета, научных работников по определенной тематике и т.д.
    """
    try:
        result = []
        table_name = scripts.get_table_name(user.user_type.lower())
        columns = db.get_columns({'tablename': table_name}, check_connection(connection))
        search_values = scripts.get_not_null_values(user, columns)
        select_string = scripts.get_selected_values(table_name, connection)
        searh = db.list_charters(None, table_name, select_string, check_connection(connection))
        if search_values:
            searh = db.list_charters(search_values, table_name, select_string, check_connection(connection))
        for item in searh:
            temp = {}
            for key, value in zip(select_string.split(','), item):
                temp.update({
                    key.strip(): value
                })
            result.append(temp)

    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 2-3 request
@app.post('/api/get_users_with_book')
async def get_borrowed_books(book_name: str):
    """
        2-3 запросы
        Выдать перечень читателей, на руках у которых находится указанное произведение.
        Получить список читателей, на руках у которых находится указанное издание (книга, журнал и т.д).
    """
    try:
        result = db.get_borrowed_books({'a_book': book_name}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 4 request
@app.post('/api/get_books_date')
async def get_books_date(start_date: str, finish_date: str):
    """
        4 запрос
        Получить перечень читателей, которые в течение указанного промежутка времени получали издание с некоторым произведением, и название этого издания.
    """
    try:
        result = db.list_interval({'start_date': start_date, 'finish_date': finish_date}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 5 request
@app.post('/api/get_user_info')
async def get_user_info(u_fio: str):
    """
        5 запрос
        Выдать список изданий, которые в течение некоторого времени получал указанный читатель из фонда библиотеки, где он зарегистрирован.
    """
    try:
        result = db.get_user_info({'u_fio': u_fio}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 6 request
@app.post('/api/get_user_info_library')
async def get_user_info_library(user_id: int):
    """
        6 запрос
        Получить перечень изданий, которыми в течение некоторого времени пользовался указанный читатель из фонда библиотеки, где он не зарегистрирован.
    """
    try:
        result = db.get_user_info_library({'user_id': user_id}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 7 request
@app.post('/api/get_books_from_shelf')
async def get_books_from_shelf(shelf: int):
    """
        7 запрос
        Получить список литературы, которая в настоящий момент выдана с определенной полки некоторой библиотеки.
    """
    try:
        result = db.get_books_from_shelf({'shelf': shelf}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 8 request
@app.post('/api/get_serviced_users')
async def get_serviced_users(worker: int):
    """
        8 запрос
        Выдать список читателей, которые в течение обозначенного периода были обслужены указанным библиотекарем.
    """
    try:
        result = db.get_serviced_users({'worker': worker}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 9 request
@app.post('/api/get_worker_production')
async def get_worker_production(start_date: str, finish_date: str):
    """
        9 запрос
        Получить данные о выработке библиотекарей (число обслуженных читателей в указанный период времени).
    """
    try:
        result = db.get_worker_production({'start_date': start_date, 'finish_date': finish_date},
                                          check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 10 request
@app.post('/api/get_users_with_deadline')
async def get_users_with_deadline():
    """
        10 запрос
        Получить список читателей с просроченным сроком литературы.
    """
    try:
        result = db.get_users_with_deadline(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 11 request
@app.post('/api/get_scrapped_books')
async def get_scrapped_books():
    """
        11 запрос
        Получить перечень указанной литературы, которая поступила (была списана) в течение некоторого периода.
    """
    try:
        result = db.get_scrapped_books(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 12 request
@app.post('/api/get_hall_workers')
async def get_hall_workers(hall_id: int):
    """
        12 запрос
        Выдать список библиотекарей, работающих в указанном читальном зале некоторой библиотеки.
    """
    try:
        result = db.get_hall_workers({'h_id': hall_id}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 13 request
@app.post('/api/get_overdue_users')
async def get_overdue_users():
    """
        13 запрос
        Получить список читателей, не посещавших библиотеку в течение указанного времени.
    """
    try:
        result = db.get_overdue_users(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 14 request
@app.post('/api/get_inventory_numbers_by_book')
async def get_inventory_numbers_by_book(book_name: str):
    """
        14 запрос
        Получить список инвентарных номеров и названий из библиотечного фонда, в которых содержится указанное произведение.
    """
    try:
        result = db.get_inventory_numbers_by_book({'book': book_name}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 15 request
@app.post('/api/get_inventory_numbers_by_author')
async def get_inventory_numbers_by_author(author_name: str):
    """
        15 запрос
        Выдать список инвентарных номеров и названий из библиотечного фонда, в которых содержатся произведения указанного автора.
    """
    try:
        result = db.get_inventory_numbers_by_author({'data': author_name}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 16 request
@app.post('/api/get_popular_books')
async def get_popular_books():
    """
        16 запрос
        Получить список самых популярных произведений.
    """
    try:
        result = db.get_popular_books(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/add_user')
async def add_user(user: models.UserData):
    try:
        table_name = scripts.get_table_name(user.user_type.lower())
        print(user.place)
        columns = db.get_columns({'tablename': table_name}, check_connection(connection))
        req_data = scripts.get_not_null_values(user, columns)
        req_data.update({'fio': f"{user.lastname} {user.firstname} {user.middlename}", 'id_library': user.id_library,
                         'u_type': user.user_type})
        scripts.add_user(req_data, table_name, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_library_name')
async def get_library_name(library_id: int):
    try:
        result = scripts.get_library_name(db.get_libraries(check_connection(connection)), library_id)
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_authors')
async def get_authors():
    try:
        result = []
        db_result = db.get_authors(check_connection(connection))
        authors = db_result.keys()
        for author in authors:
            books = []
            types = db_result.get(author).get('b_type').split(',')
            genres = db_result.get(author).get('genre').split(',')
            names = db_result.get(author).get('b_name').split(',')
            for genre, book_type, name in zip(genres,types,names):
                books.append({
                    'genre': genre,
                    'type': book_type,
                    'name': name
                })
            author_array = {'author': author, 'books': books}
            result.append(author_array)
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_books')
async def get_books():
    try:
        result = db.get_books(check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result
