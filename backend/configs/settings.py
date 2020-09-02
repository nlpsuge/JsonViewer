from enum import Enum


class TimeType(Enum):
    UNIX_TIMESTAMP = 'unix_time'


class UnixTimestampType(Enum):
    SECOND = 'second'
    MILLISECOND = 'millisecond'

