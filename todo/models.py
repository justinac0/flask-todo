from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from datetime import date

db = SQLAlchemy()


class Entry(db.Model):
    id = db.Column("entry_id", db.Integer, primary_key=True)
    body = db.Column(db.String(128))
    date_created = db.Column(db.Date())
    is_done = db.Column(db.Boolean(False))

    def __init__(self, body):
        self.body = body
        self.date_created = date.today()
        self.is_done = False
