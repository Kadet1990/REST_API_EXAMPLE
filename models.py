from datetime import datetime
from configuration import db, ma


class Note(db.Model):
    __tablename__ = "note"
    note_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String(32))
    createdtime = db.Column(
        db.DateTime, default=datetime.utcnow)
    modifiedtime = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True


class Arch_Note(db.Model):
    __tablename__ = "arch_note"
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer)
    title = db.Column(db.String(32))
    content = db.Column(db.String(32))
    comment =db.Column(db.String(32))
    createdtime = db.Column(
        db.DateTime, default=datetime.utcnow)

class Arch_NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Arch_Note
        load_instance = True
