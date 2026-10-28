from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contract(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_UNSPECIFIED: _ClassVar[Contract]
    CONTRACT_FULL_TIME: _ClassVar[Contract]
    CONTRACT_PART_TIME: _ClassVar[Contract]
CONTRACT_UNSPECIFIED: Contract
CONTRACT_FULL_TIME: Contract
CONTRACT_PART_TIME: Contract

class Employee(_message.Message):
    __slots__ = ("name", "department", "salary", "birth_year", "full_time", "address", "skills", "contract", "email")
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
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    department: str
    salary: int
    birth_year: int
    full_time: bool
    address: Employee.Address
    skills: _containers.RepeatedScalarFieldContainer[str]
    contract: Contract
    email: str
    def __init__(self, name: _Optional[str] = ..., department: _Optional[str] = ..., salary: _Optional[int] = ..., birth_year: _Optional[int] = ..., full_time: _Optional[bool] = ..., address: _Optional[_Union[Employee.Address, _Mapping]] = ..., skills: _Optional[_Iterable[str]] = ..., contract: _Optional[_Union[Contract, str]] = ..., email: _Optional[str] = ...) -> None: ...
