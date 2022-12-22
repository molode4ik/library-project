from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    VARCHAR,
    DATE,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    u_id = Column(INTEGER, primary_key=True)
    u_last_date = Column(DATE, nullable=True, default=None)
    u_type = Column(VARCHAR(50), nullable=True, default=None)
    id_library = Column(INTEGER, nullable=True, default=None)
    u_fio = Column(VARCHAR(50), nullable=True, default=None)
    login = Column(VARCHAR(50), nullable=True, default=None)
    password = Column(VARCHAR(50), nullable=True, default=None)


class Teachers(Base):
    __tablename__ = "teachers"
    t_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    t_university = Column(VARCHAR(50), nullable=True, default=None)
    t_faculty = Column(VARCHAR(50), nullable=True, default=None)
    t_rank = Column(VARCHAR(50), nullable=True, default=None)


class Peoples(Base):
    __tablename__ = "peoples"
    p_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    p_place = Column(VARCHAR(50), nullable=True, default=None)


class Students(Base):
    __tablename__ = "students"
    s_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    s_university = Column(VARCHAR(50), nullable=True, default=None)
    s_course = Column(INTEGER, nullable=True, default=None)
    s_faculty = Column(VARCHAR(50), nullable=True, default=None)


class Schools(Base):
    __tablename__ = "schools"
    sc_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    school = Column(VARCHAR(50), nullable=True, default=None)
    sc_class = Column(VARCHAR(50), nullable=True, default=None)


class Pensioners(Base):
    __tablename__ = "pensioners"
    pen_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    pen_certificate_number = Column(INTEGER, nullable=True, default=None)


class Scientists(Base):
    __tablename__ = "scientists"
    sci_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    organization = Column(VARCHAR(50), nullable=True, default=None)
    theme = Column(VARCHAR(150), nullable=True, default=None)

#############################

class Libraries(Base):
    __tablename__ = "libraries"
    l_id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), nullable=True, default=None)
    location = Column(VARCHAR(50), nullable=True, default=None)


class Halls(Base):
    __tablename__ = "halls"
    h_id = Column(INTEGER, primary_key=True)
    number_hall = Column(INTEGER, nullable=True, default=None)
    l_id = Column(ForeignKey('libraries.l_id'), nullable=False, index=True)


class Shelves(Base):
    __tablename__ = "shelves"
    sh_id = Column(INTEGER, primary_key=True)
    h_id = Column(ForeignKey('halls.h_id'), nullable=False, index=True)


class Books(Base):
    __tablename__ = "books"
    b_id = Column(INTEGER, primary_key=True)
    b_name = Column(VARCHAR(50), nullable=True, default=None)
    b_type = Column(VARCHAR(50), nullable=True, default=None)
    genre = Column(VARCHAR(50), nullable=True, default=None)
    quantity = Column(INTEGER, nullable=True, default=None)
    a_id = Column(ForeignKey('authors.a_id'), nullable=False, index=True)
    sh_id = Column(ForeignKey('shelves.sh_id'), nullable=False, index=True)


class Authors(Base):
    __tablename__ = "authors"
    a_id = Column(INTEGER, primary_key=True)
    authors_fio = Column(VARCHAR(50), nullable=True, default=None)


class Library_workers(Base):
    __tablename__ = "library_workers"
    lw_id = Column(INTEGER, primary_key=True)
    l_id = Column(ForeignKey('libraries.l_id'), nullable=False, index=True)
    lw_fio = Column(VARCHAR(50), nullable=True, default=None)


class Decommissioned(Base):
    __tablename__ = "decommissioned"
    d_id = Column(INTEGER, primary_key=True)
    b_id = Column(ForeignKey('books.b_id'), nullable=False, index=True)
    date_dec = Column(DATE, nullable=True, default=None)


class Extradition(Base):
    __tablename__ = "extradition"
    e_id = Column(INTEGER, primary_key=True)
    b_id = Column(ForeignKey('books.b_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.u_id'), nullable=False, index=True)
    finish_date = Column(DATE, nullable=True, default=None)
    start_date = Column(DATE, nullable=True, default=None)
    lw_id = Column(ForeignKey('library_workers.lw_id'), nullable=False, index=True)


Base.metadata.create_all(create_engine("postgresql+psycopg2://postgres:postgres@188.120.240.45/library", ))
