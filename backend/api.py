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


@app.post('/api/get_users')
async def get_users(user: models.UserData):
    table_name = scripts.get_table_name(user.user_type.lower())
    columns = db.get_columns({'tablename': table_name}, check_connection(connection))
    scripts.get_not_null_values(user, columns)


# 2-3 request
@app.post('/api/get_users_with_book')
async def get_borrowed_books(book_name: str):
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
    try:
        result = db.list_interval({'start_date': start_date, 'finish_date': finish_date}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 5 request
@app.post('/api/get_user_info')
async def get_user_info(user_id: int):
    try:
        result = db.get_user_info({'user_id': user_id}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 6 request
@app.post('/api/get_user_info_library')
async def get_user_info_library(user_id: int):
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
    try:
        result = db.get_worker_production({'start_date': start_date, 'finish_date': finish_date}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 10 request
@app.post('/api/get_users_with_deadline')
async def get_users_with_deadline():
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
        columns = db.get_columns({'tablename': table_name}, check_connection(connection))
        req_data = scripts.get_not_null_values(user, columns)
        req_data.update({'fio': f"{user.lastname} {user.firstname} {user.middlename}", 'id_library': user.id_library, 'u_type': user.user_type})
        scripts.add_user(req_data, table_name, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_students')
async def get_users():
    try:
        result = db.list_charters('students', check_connection(connection))
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
        result = db.get_authors(check_connection(connection))
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
