"""Flask configuration class."""
import os


class Config:
    def __init__(self):
        self._boardId = os.environ.get('boardId')
        self._key = os.environ.get('key')
        self._token = os.environ.get('token')

    @property
    def boardId(self) -> str:
        return self._boardId

    @property
    def key(self) -> str:
        return self._key

    @property
    def token(self) -> str:
        return self._token
