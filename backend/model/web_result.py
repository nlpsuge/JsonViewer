import json

from backend.model.base import Base
from backend.utils import string_utils


class WebResult(Base):

    result: object
    code: int
    message: str

    def __init__(self, code, message=None, result=None):
        self.code = code
        self.message = message
        self.result = result

    @classmethod
    def success(cls, result):
        return cls(code=200, result=result)

    @classmethod
    def failed(cls, message=None):
        return cls(500,
                   message="Internal error!" if string_utils.empty_string(message) else message)

    def to_json(self) -> str:
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

