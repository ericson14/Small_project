from flask import Flask, jsonify, redirect, url_for, abort, request, make_response, session
from werkzeug.routing import BaseConverter
import json

app = Flask(__name__)


class RegConverter(BaseConverter):
    def __init__(self, url_map, re):
        super(RegConverter, self).__init__(url_map)
        self.regex = re
# class Config(object):
#     Debug = True
#
# app.config.from_object(Config)


app.url_map.converters["re"] = RegConverter
app.config["SECRET_KEY"] = "assda123ccnklacjandeiqfaje32fklzzxxc"


@app.route("/")
def index():
    print(app.url_map)
    print(app.config["DEBUG"])
    return "Hello Flask", "666 Welcome to Flask"


@app.route('/demo1')
def demo1():
    return 'Demo1'


@app.route('/demo2/<int:user_id>')
def demo2(user_id):
    return "Demo2 {}".format(user_id)


@app.route('/demo3', methods=['POST'])
def demo3():
    return "Only post method can be rendered"


@app.route('/demo4')
def demo4():
    return redirect("http://www.baidu.com")


@app.route('/demo5')
def demo5():
    return redirect(url_for("demo2", user_id=21345))


@app.route('/demo6/<re("\d{6}"):user>')
def demo6(user):
    return "正则通过{}".format(user)


@app.route('/demo7')
def demo7():
    abort(404)


@app.route('/get')
def get():
    if request.method == "GET":
        name = request.args.get("name", "")
        age = request.args.get("age", "")
        return "{}-----{}".format(name, age)
    else:
        return "405 请求方式错误"


@app.route('/post', methods=['POST'])
def post():
    if request.method == "POST":
        name = request.form.get("name", "")
        pwd = request.form.get("pwd", "")
        return "{}----{}".format(name, pwd)
    else:
        return "405 请求方式错误"


@app.route('/login')
def login():
    response = make_response("登录成功")
    response.set_cookie("user_id", "1", max_age=3600)
    response.set_cookie("pwd", "12345", max_age=3600)
    return response


@app.route('/login2')
def login2():
    session["user_id"] = "2"
    session["pwd"] = "654321"
    return "用Session登录成功"


@app.route('/reload')
def reload():
    user_id = request.cookies.get("user_id", "")
    pwd = request.cookies.get("pwd", "")
    return "用户名：{}，密码：{}".format(user_id, pwd)


@app.route('/reload2')
def reload2():
    user_id = session["user_id"]
    pwd = session["pwd"]
    return "用户名：{}，密码：{}（Session版本）".format(user_id, pwd)


@app.route('/logout')
def logout():
    response = make_response("退出登录成功")
    response.delete_cookie("user_id")
    response.delete_cookie("pwd")
    return response


@app.route('/logout2')
def logout2():
    session.pop("user_id")
    session.pop("pwd")
    return "Session退出成功"


@app.route('/image', methods=['POST'])
def image():
    if request.method == "POST":
        img = request.files.get("img")
        img.save('./1.png')
        return "上传成功"
    else:
        return "405 请求方式错误"


@app.errorhandler(404)
def error1(error):
    print(error)
    return redirect("http://hd.mi.com/webfile/zt/hd/2014042802/cn.html")


@app.route('/json1')
def json1():
    info = {
        "name": "James",
        "age": 38,
        "info": {
            "city": "Los Angeles",
            "team": "Lakers"
        }
    }
    json_str = json.dumps(info)
    print(json_str)
    json_str1 = jsonify(info)
    return json_str1


@app.before_first_request
def before_fr():
    print("First Request")


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
