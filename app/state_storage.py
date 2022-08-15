
import pathlib

from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.utils import json

from marshmallow import Schema, fields

class StateStorage(JSONStorage):
    def read(self, path: pathlib.Path):
        with path.open('r') as f:
            return json.load(f)

    def write(self, path: pathlib.Path):
        with path.open('w') as f:
            return json.dump(self.data, f, indent=4)

class StateContextSchema(Schema):
    _last_activity_time = fields.DateTime()
