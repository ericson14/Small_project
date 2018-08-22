from flask import Flask, render_template, current_app
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/demo1')
def demo1():
    my_str = "黑马程序员"
    my_int = 10
    my_arr = [3, 4, 6, 10, 5]
    print(current_app.config["DEBUG"])
    return render_template("temp1.html", my_str=my_str, my_arr=my_arr, my_int=my_int)


if __name__ == "__main__":
    manager.run()
