from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Employee(_message.Message):
    __slots__ = ("name", "department", "salary", "birth_year", "full_time", "address")
    class Address(_message.Message):
        __slots__ = ("city", "country")
        CITY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        city: str
        country: str
        def __init__(self, city: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    SALARY_FIELD_NUMBER: _ClassVar[int]
    BIRTH_YEAR_FIELD_NUMBER: _ClassVar[int]
    FULL_TIME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    department: str
    salary: int
    birth_year: int
    full_time: bool
    address: Employee.Address
    def __init__(self, name: _Optional[str] = ..., department: _Optional[str] = ..., salary: _Optional[int] = ..., birth_year: _Optional[int] = ..., full_time: _Optional[bool] = ..., address: _Optional[_Union[Employee.Address, _Mapping]] = ...) -> None: ...

class Employees(_message.Message):
    __slots__ = ("employees",)
    EMPLOYEES_FIELD_NUMBER: _ClassVar[int]
    employees: _containers.RepeatedCompositeFieldContainer[Employee]
    def __init__(self, employees: _Optional[_Iterable[_Union[Employee, _Mapping]]] = ...) -> None: ...
