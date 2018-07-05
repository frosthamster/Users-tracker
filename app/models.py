from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_part_len = 30
    first_name = db.Column(db.String(name_part_len))
    last_name = db.Column(db.String(name_part_len))
    middle_name = db.Column(db.String(name_part_len))
    pet = db.Column(db.String(60))
    gender = db.Column(db.String(6))
    birthday = db.Column(db.Date)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __str__(self):
        return f'<{self.__class__.__name__}> {self.full_name} [{self.timestamp}]'
