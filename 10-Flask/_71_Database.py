from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:chuanzhi@127.0.0.1:3306/user"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)

    def __repr__(self):
        return "Role: id:{}, name:{}".format(self.id, self.name)


class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    role_id = db.Column(db.Integer)

    def __repr__(self):
        return "Account: id:{}, name:{}".format(self.id, self.name)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    role1 = Role(name="管理员")
    role2 = Role(name="用户")
    role3 = Role(name="游客")
    db.session.add_all([role1, role2, role3])
    db.session.commit()
    user1 = Account(name="Plea", role_id=role1.id)
    user2 = Account(name="Kelve", role_id=role2.id)
    user3 = Account(name="Xenoye", role_id=role3.id)
    user4 = Account(name="Zenith", role_id=role2.id)
    user5 = Account(name="Querte", role_id=role2.id)
    db.session.add_all([user1, user2, user3, user4, user5])
    db.session.commit()
    app.run(debug=True)
