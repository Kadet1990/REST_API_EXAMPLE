from models import Arch_Note,Arch_NoteSchema
from flask import  abort

def read_all():


    arch_note = Arch_Note.query.order_by(Arch_Note.title).all()

    if arch_note is not None:
        # Serialize the data for the response
        arch_note_schema = Arch_NoteSchema(many=True)
        data = arch_note_schema.dump(arch_note)
        return data
    else:
        abort(
            404,
            "History of note not found ",
        )

def read_one(note_id):


    arch_note = Arch_Note.query.filter(Arch_Note.note_id == note_id).order_by(Arch_Note.createdtime).all()

    if arch_note is not None:

        # Serialize the data for the response
        note_schema = Arch_NoteSchema(many=True)
        data = note_schema.dump(arch_note)
        return data

    else:
        abort(
            404,
            "Note not found for Id: {note_id}".format(note_id=note_id),
        )