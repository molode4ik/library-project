from typing import Optional
from pydantic import BaseModel


class Teacher(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    university: str
    rank: str
    faculty: str
    id_library: Optional[int] = None


class Student(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    university: str
    course: int
    faculty: str
    id_library: Optional[int] = None


class People(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    place: str
    id_library: Optional[int] = None


class Pensioner(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    certificate: Optional[int] = None
    id_library: Optional[int] = None


class Scientist(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    organization: Optional[str] = None
    theme: Optional[str] = None
    id_library: Optional[int] = None