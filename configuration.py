import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
database = "note.db"
#path to the current file
dir = os.path.abspath(os.path.dirname(__file__))

# Connexion application instance
connex_app = connexion.App(__name__, specification_dir=dir)

# Flask app instance
app = connex_app.app

# Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(dir, database)

# Configure the SqlAlchemy
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

