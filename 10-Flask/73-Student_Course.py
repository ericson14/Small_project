from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:chuanzhi@127.0.0.1:3306/stucour"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "a13uo1ccl"


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

stucur = db.Table("stucour",
                  db.Column("stu_id", db.Integer, db.ForeignKey("student.id")),
                  db.Column("cour_id", db.Integer, db.ForeignKey("course.id")))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    courses = db.relation("Course", backref="students", secondary=stucur)

    def __repr__(self):
        return "Student: {} {}".format(self.name, self.id)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "Course: {} {}".format(self.name, self.id)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    # 添加测试数据

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    # 使用关系字段将学生选修的课程表示出来，（多对多）
    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu3])
    db.session.commit()
    db.session.add_all([cou1, cou2, cou3])

    db.session.commit()
    app.run(debug=True)
