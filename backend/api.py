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


@app.post('/api/get_user_info')
async def get_user_info(user_id: int):
    try:
        result = db.get_user_info(user_id, check_connection(connection))
    except Exception as er:
        print(er)
        result = -1
    finally:
        return result


@app.post('/api/get_students')
async def get_users():
    try:
        result = db.list_charters('students', check_connection(connection))
        print(db.get_library(check_connection(connection)))
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