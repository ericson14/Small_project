import re
import time
import pymysql

route_list = []


def routers(url):
    def wrapper(func):
        route_list.append((url, func))
    return wrapper


@routers("/center.html")
def center():
    data_from_sql = ""
    conn = pymysql.connect(host="localhost", user="root", password="chuanzhi",
                           database="stock", port=3306, charset='utf8')
    curs1 = conn.cursor()
    sql = "select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info " \
          "from info as i inner join focus as f on f.info_id=i.id"
    curs1.execute(sql)
    result = curs1.fetchall()
    for line in result:
        line_ui_data = """<tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update.html"> 
                    <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
                </td>
            </tr>""".format(*line)
        data_from_sql += line_ui_data
    with open("./templates/center.html", encoding='utf8') as f:
        content = f.read()
    content = re.sub(r"{%content%}", data_from_sql, content)
    return content


@routers("/time.html")
def get_time():
    return time.ctime()


@routers("/index.html")
def index():
    conn = pymysql.connect(host="localhost", user="root", password="chuanzhi",
                           database="stock", port=3306, charset='utf8')
    curs1 = conn.cursor()
    curs1.execute("select * from info")
    result = curs1.fetchall()
    data_from_sql = ""
    for line in result:
        line_ui_data = """<tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>
                            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000036">
                        </td>
                    </tr>""".format(*line)
        data_from_sql += line_ui_data
    curs1.close()
    conn.close()
    with open("./templates/index.html", encoding='utf8') as f:
        content = f.read()
    content = re.sub(r"{%content%}", data_from_sql, content)
    return content


@routers("/grand.html")
def grand():
    with open("./static/grand.html", encoding='utf8') as f:
        content = f.read()
    return content


@routers("/update.html")
def update():
    with open("./templates/update.html", encoding='utf8') as f:
        content = f.read()
    return content


def error():
    return "<a href=http://www.douyu.com/directory/game/yz><img src=/images/404.jpg></a>"


def dynamic_resource(env):
    request_url = env["PATH_INFO"]
    for url, func in route_list:
        if url == request_url:
            return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], func()
    else:
        return '404 Page Not Found', [('Content-Type', 'text/html;charset=utf-8')], error()
