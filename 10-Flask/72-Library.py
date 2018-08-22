from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:chuanzhi@127.0.0.1:3306/library"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "a13uo1ccl"


class Register(FlaskForm):
    author = StringField("作者", render_kw={"placeholder": "添加作者"})
    book = StringField("书名", render_kw={"placeholder": "添加书名"})
    submit = SubmitField("添加")


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    books = db.relation("Book", backref="author")

    def __repr__(self):
        return "Author: {} {}".format(self.name, self.id)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    def __repr__(self):
        return "Book: {} {}".format(self.name, self.id)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Register()
    if request.method == "POST":
        if form.validate_on_submit():
            author_name = request.form.get("author")
            book_name = request.form.get("book")
            author = Author.query.filter(Author.name == author_name).first()
            if author:
                # 有作者只添加书籍
                book = Book.query.filter(Book.name == book_name).first()
                if book:
                    flash("已经有此书了，请勿重复添加")
                else:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
            else:
                # 没有该作者，添加作者再添加书籍
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
        else:
            flash("参数错误")
    authors = Author.query.all()
    return render_template("temp4_72.html", form=form, authors=authors)


@app.route('/del_book/<book_id>')
def del_book(book_id):
    delbook = Book.query.get(book_id)
    if delbook:
        try:
            db.session.delete(delbook)
        except Exception as e:
            flash(e)
            db.session.rollback()
        finally:
            db.session.commit()
    else:
        flash("书名不存在。。。")
    return redirect(url_for("index"))


@app.route('/del_author/<author_id>')
def del_author(author_id):
    delauthor = Author.query.get(author_id)
    if delauthor:
        # 删除作者需要先删除旗下所有书籍
        books = Book.query.filter(author_id == Book.author_id)
        try:
            for book in books:
                db.session.delete(book)
            db.session.delete(delauthor)
        except Exception as e:
            flash(e)
            db.session.rollback()
        finally:
            db.session.commit()
    else:
        flash("作者不存在。。。")
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.drop_all()
    # 创建所有表
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
