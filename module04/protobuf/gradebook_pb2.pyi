from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ("id", "name", "scores")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    scores: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., scores: _Optional[_Iterable[int]] = ...) -> None: ...

class GradeBook(_message.Message):
    __slots__ = ("course", "students")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    STUDENTS_FIELD_NUMBER: _ClassVar[int]
    course: str
    students: _containers.RepeatedCompositeFieldContainer[Student]
    def __init__(self, course: _Optional[str] = ..., students: _Optional[_Iterable[_Union[Student, _Mapping]]] = ...) -> None: ...
