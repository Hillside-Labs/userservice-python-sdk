from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EQUALS: _ClassVar[Operator]
    NOT_EQUALS: _ClassVar[Operator]
    GREATER_THAN: _ClassVar[Operator]
    GREATER_THAN_OR_EQUALS: _ClassVar[Operator]
    LESS_THAN: _ClassVar[Operator]
    LESS_THAN_OR_EQUALS: _ClassVar[Operator]
    IN: _ClassVar[Operator]
    NOT_IN: _ClassVar[Operator]
    CONTAINS: _ClassVar[Operator]
    NOT_CONTAINS: _ClassVar[Operator]
EQUALS: Operator
NOT_EQUALS: Operator
GREATER_THAN: Operator
GREATER_THAN_OR_EQUALS: Operator
LESS_THAN: Operator
LESS_THAN_OR_EQUALS: Operator
IN: Operator
NOT_IN: Operator
CONTAINS: Operator
NOT_CONTAINS: Operator

class NewUser(_message.Message):
    __slots__ = ("username", "uuid", "attributes", "traits")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    username: str
    uuid: str
    attributes: _struct_pb2.Struct
    traits: _struct_pb2.Struct
    def __init__(self, username: _Optional[str] = ..., uuid: _Optional[str] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UserRequest(_message.Message):
    __slots__ = ("id", "username", "uuid", "attributes", "traits")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    uuid: str
    attributes: _struct_pb2.Struct
    traits: _struct_pb2.Struct
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., uuid: _Optional[str] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("id", "uuid", "username", "attributes", "traits")
    ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    id: int
    uuid: str
    username: str
    attributes: _struct_pb2.Struct
    traits: _struct_pb2.Struct
    def __init__(self, id: _Optional[int] = ..., uuid: _Optional[str] = ..., username: _Optional[str] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UserQuery(_message.Message):
    __slots__ = ("page_size", "page_token", "order_by", "id", "username", "uuid", "attributeFilters", "traitFilters")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTEFILTERS_FIELD_NUMBER: _ClassVar[int]
    TRAITFILTERS_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    order_by: str
    id: int
    username: str
    uuid: str
    attributeFilters: _containers.RepeatedCompositeFieldContainer[AttributeFilter]
    traitFilters: _containers.RepeatedCompositeFieldContainer[TraitFilter]
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., id: _Optional[int] = ..., username: _Optional[str] = ..., uuid: _Optional[str] = ..., attributeFilters: _Optional[_Iterable[_Union[AttributeFilter, _Mapping]]] = ..., traitFilters: _Optional[_Iterable[_Union[TraitFilter, _Mapping]]] = ...) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ("users", "next_page_token")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserResponse]
    next_page_token: str
    def __init__(self, users: _Optional[_Iterable[_Union[UserResponse, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class EventRequest(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: Event
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class EventResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: Event
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("id", "timestamp", "source", "specversion", "type", "datacontenttype", "dataschema", "subject", "data", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SPECVERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATACONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    DATASCHEMA_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    source: str
    specversion: str
    type: str
    datacontenttype: str
    dataschema: str
    subject: str
    data: bytes
    user_id: int
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., specversion: _Optional[str] = ..., type: _Optional[str] = ..., datacontenttype: _Optional[str] = ..., dataschema: _Optional[str] = ..., subject: _Optional[str] = ..., data: _Optional[bytes] = ..., user_id: _Optional[int] = ...) -> None: ...

class UserID(_message.Message):
    __slots__ = ("id", "uuid")
    ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    id: int
    uuid: str
    def __init__(self, id: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class SearchUserTraitsRequest(_message.Message):
    __slots__ = ("user_id", "names", "begin", "end", "limit", "latest")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    user_id: UserID
    names: _containers.RepeatedScalarFieldContainer[str]
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    limit: int
    latest: bool
    def __init__(self, user_id: _Optional[_Union[UserID, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., latest: bool = ...) -> None: ...

class GetUsersByAggregatedTraitsRequest(_message.Message):
    __slots__ = ("type", "name", "operator", "value", "begin", "end", "limit")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    operator: str
    value: float
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[float] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class GetAggregateForUsersRequest(_message.Message):
    __slots__ = ("user_ids", "type", "name")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedCompositeFieldContainer[UserID]
    type: str
    name: str
    def __init__(self, user_ids: _Optional[_Iterable[_Union[UserID, _Mapping]]] = ..., type: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AggregateResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class SearchUserEventsRequest(_message.Message):
    __slots__ = ("types", "subjects", "sources", "schemas", "begin", "end", "limit")
    TYPES_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[str]
    subjects: _containers.RepeatedScalarFieldContainer[str]
    sources: _containers.RepeatedScalarFieldContainer[str]
    schemas: _containers.RepeatedScalarFieldContainer[str]
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, types: _Optional[_Iterable[str]] = ..., subjects: _Optional[_Iterable[str]] = ..., sources: _Optional[_Iterable[str]] = ..., schemas: _Optional[_Iterable[str]] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class SearchUserTraitsResponse(_message.Message):
    __slots__ = ("traits",)
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    traits: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, traits: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class SearchEventsRequest(_message.Message):
    __slots__ = ("user_id", "names", "begin", "end", "limit")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    user_id: UserID
    names: _containers.RepeatedScalarFieldContainer[str]
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, user_id: _Optional[_Union[UserID, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class SearchEventsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class NaturalBreaksQueryRequest(_message.Message):
    __slots__ = ("name", "breaks", "begin", "end")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BREAKS_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    name: str
    breaks: int
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., breaks: _Optional[int] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NaturalBreaksRequest(_message.Message):
    __slots__ = ("values", "breaks")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    BREAKS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    breaks: int
    def __init__(self, values: _Optional[_Iterable[float]] = ..., breaks: _Optional[int] = ...) -> None: ...

class NaturalBreaksResponse(_message.Message):
    __slots__ = ("breaks",)
    BREAKS_FIELD_NUMBER: _ClassVar[int]
    breaks: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, breaks: _Optional[_Iterable[float]] = ...) -> None: ...

class AttributeFilter(_message.Message):
    __slots__ = ("name", "operator", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    operator: Operator
    value: _struct_pb2.Value
    def __init__(self, name: _Optional[str] = ..., operator: _Optional[_Union[Operator, str]] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class TraitFilter(_message.Message):
    __slots__ = ("name", "operator", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    operator: Operator
    value: _struct_pb2.Value
    def __init__(self, name: _Optional[str] = ..., operator: _Optional[_Union[Operator, str]] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
