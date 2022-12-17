import sqlalchemy_connect as db
import api_models as models
from fastapi import FastAPI
from session import get_session, check_connection
import scripts


app = FastAPI()


@app.on_event('startup')
async def startup():
    global connection
    connection = None
    connection = get_session()


# 2-3 request
@app.post('/api/get_borrowed_books')
async def get_borrowed_books(book_name: str):
    try:
        result = db.list_interval({'a_book': book_name}, check_connection(connection))
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
        result = db.get_user_info(user_id, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 6 request
@app.post('/api/get_user_info_library')
async def get_user_info_library(user_id: int):
    try:
        result = db.get_user_info_library({'name': user_id}, check_connection(connection))
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
        result = db.get_hall_workers({'hall_id': hall_id}, check_connection(connection))
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
@app.post('/api/get_inventory_numbers')
async def get_inventory_numbers(book_name: str):
    try:
        result = db.get_inventory_numbers({'book': book_name}, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


# 14 request
@app.post('/api/get_inventory_numbers_by_book')
async def get_inventory_numbers_by_book(author_name: str):
    try:
        result = db.get_inventory_numbers_by_book({'book': author_name}, check_connection(connection))
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


@app.post('/api/add_student')
async def add_student(student: models.Student):
    try:
        req_data = {
            'fio': f'{student.lastname} {student.firstname} {student.middlename}',
            'id_library': student.id_library,
            'university': student.university,
            'course': student.course,
            'faculty': student.faculty
        }
        db.add_student(req_data, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/add_teacher')
async def add_teacher(teacher: models.Teacher):
    try:
        req_data = {
            'fio': f'{teacher.lastname} {teacher.firstname} {teacher.middlename}',
            'id_library': teacher.id_library,
            'university': teacher.university,
            'rank': teacher.rank,
            'faculty': teacher.faculty
        }
        db.add_teacher(req_data, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/add_people')
async def add_people(people: models.People):
    try:
        req_data = {
            'fio': f'{people.lastname} {people.firstname} {people.middlename}',
            'id_library': people.id_library,
            'place': people.place
        }
        db.add_people(req_data, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/add_pensioner')
async def add_pensioner(pensioner: models.Pensioner):
    try:
        req_data = {
            'fio': f'{pensioner.lastname} {pensioner.firstname} {pensioner.middlename}',
            'id_library': pensioner.id_library,
            'certificate': pensioner.certificate
        }
        db.add_pensioner(req_data, check_connection(connection))
        result = 0
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/add_scientist')
async def add_scientist(scientist: models.Scientist):
    try:
        req_data = {
            'fio': f'{scientist.lastname} {scientist.firstname} {scientist.middlename}',
            'id_library': scientist.id_library,
            'organization': scientist.organization,
            'theme': scientist.theme
        }
        db.add_scientist(req_data, check_connection(connection))
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
