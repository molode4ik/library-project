import unittest
import requests

host = "http://188.120.240.45"
port = "7000"
url = f"{host}:{port}/api/"


class TestBooks(unittest.TestCase):
    def test_get_books(self):
        self.assertNotEqual(requests.post(url + 'get_books').json(), int)
        self.assertIsInstance(requests.post(url + 'get_books').json(), list)

    def test_get_books_from_shelf(self):
        self.assertNotEqual(requests.post(url + 'get_books_from_shelf?shelf=1&name=ТЦ').json(), int)
        self.assertIsInstance(requests.post(url + 'get_books_from_shelf?shelf=1&name=ТЦ').json(), list)

    def test_get_scrapped_books(self):
        req_body = {
            "start_date": "12.12.2000",
            "finish_date": "12.12.2020"
        }
        self.assertNotEqual(requests.post(url + 'get_scrapped_books', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_scrapped_books', json=req_body).json(), list)

    def test_get_popular_books(self):
        self.assertNotEqual(requests.post(url + 'get_popular_books').json(), int)
        self.assertIsInstance(requests.post(url + 'get_popular_books').json(), list)

    def test_get_books_by_user(self):
        self.assertNotEqual(requests.post(url + 'get_user_info?u_fio=oleg').json(), int)
        self.assertIsInstance(requests.post(url + 'get_user_info?u_fio=oleg').json(), list)

    def test_get_books_by_user_library(self):
        self.assertNotEqual(requests.post(url + 'get_user_info_library?u_fio=oleg').json(), int)
        self.assertIsInstance(requests.post(url + 'get_user_info_library?u_fio=oleg').json(), list)


class TestUsers(unittest.TestCase):
    def test_get_readers(self):
        self.assertNotEqual(requests.post(url + 'get_readers').json(), int)
        self.assertIsInstance(requests.post(url + 'get_readers').json(), list)

    def test_get_overdue_users(self):
        req_body = {
            "start_date": "12.12.2000",
            "finish_date": "12.12.2000"

        }
        self.assertNotEqual(requests.post(url + 'get_overdue_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_overdue_users',  json=req_body).json(), list)

    def get_serviced_users(self):
        self.assertNotEqual(requests.post(url + 'get_serviced_users?lw_fio=Петр').json(), int)
        self.assertIsInstance(requests.post(url + 'get_serviced_users?lw_fio=Петр').json(), list)

    def test_get_people(self):
        req_body = {
            "user_type": "пользователь",
            "place": "ворош"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "пользователь"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_schools(self):
        req_body = {
            "user_type": "школьник",
            "school": "лицей9",
            "clas": 10
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "школьник"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_pensioners(self):
        req_body = {
            "user_type": "пенсионер",
            "certificate": 123456
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "пенсионер"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_teachers(self):
        req_body = {
            "user_type": "преподаватель",
            "university": "горхоз",
            "faculty": "фаигр",
            "rank": "доцент"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "преподаватель"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_students(self):
        req_body = {
            "user_type": "студент",
            "university": "горхоз",
            "course": 3,
            "faculty": "фаигр"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "студент"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_scientists(self):
        req_body = {
            "user_type": "научный работник",
            "organization": "клевая",
            "theme": "супер"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)
        req_body = {
            "user_type": "научный работник"
        }
        self.assertNotEqual(requests.post(url + 'get_users', json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_users', json=req_body).json(), list)

    def test_get_users_by_date(self):
        req_body = {
            "start_date": "12.12.2000",
            "finish_date": "12.12.2022",
            "b_type": "Поэзия",
            "b_name": "Драчки"
        }
        self.assertNotEqual(
            requests.post(url + 'get_users_by_date', json=req_body).json(), int)
        self.assertIsInstance(
            requests.post(url + 'get_users_by_date', json=req_body).json(), list)

    def test_get_users_with_deadline(self):
        self.assertNotEqual(requests.post(url + 'get_users_with_deadline').json(), int)
        self.assertIsInstance(requests.post(url + 'get_users_with_deadline').json(), list)

    def test_get_users_with_book(self):
        self.assertNotEqual(
            requests.post(url + 'get_users_with_book?book_name=дадо').json(), int)
        self.assertIsInstance(
            requests.post(url + 'get_users_with_book?book_name=дадо').json(), list)

    def test_get_users_with_type_book(self):
        self.assertNotEqual(
            requests.post(url + 'get_users_with_type_book?b_type=книга').json(), int)
        self.assertIsInstance(
            requests.post(url + 'get_users_with_type_book?b_type=книга').json(), list)

    def test_add_people(self):
        req_body = {
            "user_type": "пользователь",
            "firstname": "Владислав",
            "middlename": "Владиславович",
            "lastname": "Владов",
            "place": "ТЗР"
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)

    def test_add_schools(self):
        req_body = {
            "user_type": "школьник",
            "firstname": "Петя",
            "middlename": "Петров",
            "lastname": "Петрович",
            "school": "лицей9",
            "clas": 10
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)

    def test_add_pensioner(self):
        req_body = {
            "user_type": "пенсионер",
            "firstname": "Петр",
            "middlename": "Олегович",
            "lastname": "Олегов",
            "certificate": 123456
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)

    def test_add_teacher(self):
        req_body = {
            "user_type": "преподаватель",
            "firstname": "Олег",
            "middlename": "Петрович",
            "lastname": "Петров",
            "university": "горхоз",
            "faculty": "фаигр",
            "rank": "доцент"
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)

    def test_add_student(self):
        req_body = {
            "user_type": "студент",
            "firstname": "Олег",
            "middlename": "Олегович",
            "lastname": "Олегов",
            "university": "горхоз",
            "course": 3,
            "faculty": "фаигр"
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)

    def test_add_scientists(self):
        req_body = {
            "user_type": "научный работник",
            "firstname": "Дмитрий",
            "middlename": "Олегович",
            "lastname": "Петров",
            "organization": "клевая",
            "theme": "супер"
        }
        self.assertEqual(requests.post(url + 'add_user', json=req_body).json(), 0)


class TestAuthors(unittest.TestCase):
    def test_get_authors(self):
        self.assertNotEqual(requests.post(url + 'get_authors').json(), int)
        self.assertIsInstance(requests.post(url + 'get_authors').json(), list)


class TestInventoryNumbers(unittest.TestCase):
    def test_get_number_by_book(self):
        self.assertNotEqual(requests.post(url + 'get_inventory_numbers_by_book?book_name=дадо').json(), int)
        self.assertIsInstance(requests.post(url + 'get_inventory_numbers_by_book?book_name=дадо').json(), list)

    def test_get_number_by_author(self):
        self.assertNotEqual(requests.post(url + 'get_inventory_numbers_by_author?author_name=пушкин').json(), int)
        self.assertIsInstance(requests.post(url + 'get_inventory_numbers_by_author?author_name=пушкин').json(), list)


class TestWorkers(unittest.TestCase):
    def test_get_hall_workers(self):
        self.assertNotEqual(requests.post(url + 'get_hall_workers?number_hall=1').json(), int)
        self.assertIsInstance(requests.post(url + 'get_hall_workers?number_hall=1').json(), list)

    def test_get_workers_production(self):
        req_body ={
            "start_date": "12.12.2000",
            "finish_date": "12.12.2000"
        }
        self.assertNotEqual(requests.post(url + 'get_worker_production',  json=req_body).json(), int)
        self.assertIsInstance(requests.post(url + 'get_worker_production', json=req_body).json(), list)
