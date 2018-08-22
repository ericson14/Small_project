from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, DataRequired

app = Flask(__name__)
app.secret_key = "121lkfni932nflkn"


class RegisterForm(FlaskForm):
    username = StringField("用户名", [DataRequired("请输入用户名")],
                           render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码", [DataRequired("请输入密码")],
                             render_kw={"placeholder": "请输入密码"})
    password2 = PasswordField("确认密码",
                              [DataRequired("请再次输入密码"), EqualTo("password", "密码不一致")],
                              render_kw={"placeholder": "确认密码"})
    submit = SubmitField("注册")


@app.route('/', methods=['GET', 'POST'])
def index():
    register = RegisterForm()
    if request.method == "POST":
        if register.validate_on_submit():
            username = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            print(username, password, password2)
            return "注册成功!"
        else:
            flash(register.errors)
    return render_template("temp3_70.html", register=register)


if __name__ == "__main__":
    app.run(debug=True)
