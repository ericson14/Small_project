from flask import Flask, render_template, flash, g, session, request
from functools import reduce

app = Flask(__name__)
app.secret_key = "dacjkacbakjc3o4901ir19i113;"


@app.template_filter("addlist")
def add_list(list1):
    return reduce(lambda x, y: x+y, list1)


@app.route('/')
def index():
    str1 = "itheima"
    list1 = [x for x in range(0, 30, 3)]
    goods_list = [
        {
            "goods_name": "西瓜",
            "price": 10
        },
        {
            "goods_name": "芒果",
            "price": 13
        },
        {
            "goods_name": "荔枝",
            "price": 12
        }
    ]
    return render_template("temp2_68.html", list1=list1, goods_list=goods_list,
                           str1=str1)


@app.route('/control')
def control():
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template("temp3_68_2.html", my_list=my_list)


@app.route('/special')
def special():
    g.name = "James"
    session["name"] = "Lebanon"
    flash("沉迷学习")
    flash("日渐消瘦")
    return render_template("temp3_68_3.html")


if __name__ == "__main__":
    app.run(debug=True)
