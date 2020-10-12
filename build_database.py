import os
from configuration import db
from models import Note, Arch_Note

# Data to initialize database with
NOTE = [
    {"title": "Note1", "content": "Lorem ipsum 1"},
    {"title": "Note2", "content": "Lorem ipsum 2"},
    {"title": "Note3", "content": "Lorem ipsum 3"},
]


# Delete database file if it exists currently
if os.path.exists('note.db'):
    os.remove('note.db')


# Create the database
db.create_all()

for note in NOTE:
    n = Note(title=note['title'], content=note['content'])
    db.session.add(n)

db.session.commit()
note_all = Note.query.all()

for n_all in note_all:
    arch_n = Arch_Note(note_id=n_all.note_id, title=n_all.title, content=n_all.content,comment='created')
    db.session.add(arch_n)

db.session.commit()