from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:chuanzhi@127.0.0.1/migrate"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.Boolean)
    email = db.Column(db.String(50))


if __name__ == "__main__":
    us1 = User(name="小明", sex=True)
    manager.run()
