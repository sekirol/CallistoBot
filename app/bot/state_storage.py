
import pathlib

from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.utils import json

from marshmallow import Schema, fields

class StateStorage(JSONStorage):
    def read(self, path: pathlib.Path):
        with path.open('r') as f:
            return json.load(f)

    def write(self, path: pathlib.Path):
        for chat_id, chat_context in self.data.items():
            for user_id, user_context in chat_context.items():
                schema = StateContextSchema()
                object_string = schema.dumps(user_context['data'])
                self.data[chat_id][user_id]['data'] = object_string
                
        with path.open('w') as f:
            return json.dump(self.data, f, indent=4)

class StateContextSchema(Schema):
    _last_activity_time = fields.DateTime()