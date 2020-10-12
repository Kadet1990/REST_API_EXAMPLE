from models import Note, NoteSchema,Arch_Note
from flask import make_response, abort
from configuration import db

count = 1

def read_all():


    note = Note.query.order_by(Note.title).all()

    if note is not None:
        # Serialize the data for the response
        note_schema = NoteSchema(many=True)
        data = note_schema.dump(note)
        return data
    else:
        abort(
            404,
            "Notes not found ",
        )

def read_one(note_id):


    note = Note.query.filter(Note.note_id == note_id).one_or_none()

    if note is not None:

        # Serialize the data for the response
        note_schema = NoteSchema()
        data = note_schema.dump(note)
        return data

    else:
        abort(
            404,
            "Note not found for Id: {note_id}".format(note_id=note_id),
        )

def update(note_id, note):


    update_note = Note.query.filter(
        Note.note_id == note_id
    ).one_or_none()

    # Try to find an existing note with the same title as the update
    title = note.get("title")
    content = note.get("content")

    existing_note = (
        Note.query.filter(Note.title == title)
        .filter(Note.content == content)
        .one_or_none()
    )


    if update_note is None:
        abort(
            404,
            "Note not found for Id: {note_id}".format(note_id=note_id),
        )

    elif (
        existing_note is not None and existing_note.note_id != note_id
    ):
        abort(
            404,
            "Note {title} {content} exists already".format(
                title=title, content=content
            ),
        )
    else:

        # turn the passed in note into a db object
        schema = NoteSchema()
        update = schema.load(note, session=db.session)

        # Set the id to the note we want to update
        update.note_id = update_note.note_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        note_add = Note.query.filter(Note.note_id == note_id).one_or_none()
        print(note_add)
        arch_n = Arch_Note(note_id=note_add.note_id, title=note_add.title, content=note_add.content,comment='updated')
        db.session.commit()

        data = schema.dump(update_note)

        return data, 200

def create(note):
    global count
    title = note.get("title")
    content = note.get("content")

    existing_note = (
        Note.query.filter(Note.title == title)
        .filter(Note.content == content)
        .one_or_none()
    )

    if existing_note is None:
        note_all = Note.query.all()
        schema = NoteSchema()
        if len(note_all)==0:
            note['note_id'] = count
        else:
            print(note_all)
            if (count <= note_all[-1].note_id):
                count = note_all[-1].note_id+1

        new_note = schema.load(note, session=db.session)

        # Add the note to the database
        db.session.add(new_note)
        db.session.commit()

        note_all = Note.query.all()
        arch_n = Arch_Note(note_id=note_all[-1].note_id, title=note_all[-1].title, content=note_all[-1].content, comment='created')
        db.session.add(arch_n)
        db.session.commit()

        # Serialize and return the newly created note in the response
        data = schema.dump(new_note)

        return data, 201

    else:
        abort(
            404,
            "Note {title} {content} exists already".format(
                title=title, content=content
            ),
        )

def delete(note_id):
    global count
    note = Note.query.filter(Note.note_id == note_id).one_or_none()

    if note is not None:
        note_all = Note.query.all()
        if(count<=note_all[-1].note_id):
            count = note_all[-1].note_id+1

        db.session.delete(note)
        db.session.commit()

        arch_n = Arch_Note(note_id=note.note_id, title=note.title, content=note.content,comment='deleted')
        db.session.add(arch_n)
        db.session.commit()

        return make_response(
            "Note {note_id} deleted".format(note_id=note_id), 200
        )

    else:
        abort(
            404,
            "Note not found for Id: {note_id}".format(note_id=note_id),
        )