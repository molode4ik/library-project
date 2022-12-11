import psycopg2
from psycopg2 import Error
from config import host,password, user, db_name
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def added_student():
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  database = db_name)
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "Select * from users;"
    #     )
    #
    #     print(cursor.fetchall())
    data = "2002-10-11"
    fio = "Якунин Олег Александрович"
    univer = "ВОЛГГТУ"
    course = 3
    fac = "ФАИГР"
    cur = connection.cursor()
    cur.execute("INSERT INTO users(u_last_data, u_fio) VALUES ( %s, %s)", (data, fio))

    #connection.commit()
    #u_id = cur.fetchall()
    #print(u_id)
    cur.execute("INSERT INTO student(s_university, s_course, s_faculty) VALUES (%s, %s, %s)", (univer,course,fac))
    #connection.commit()




print(added_student())