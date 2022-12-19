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
    type: str


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


class UserData(BaseModel):
    user_type: str
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None
    organization: Optional[str] = None
    theme: Optional[str] = None
    id_library: Optional[int] = None
    certificate: Optional[int] = None
    place: Optional[str] = None
    university: Optional[str] = None
    course: Optional[int] = None
    faculty: Optional[str] = None
    rank: Optional[str] = None
