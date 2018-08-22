import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="student", charset="utf8")
    cs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from students where name rlike %s"
    name = input("请输入要查询的学生姓：")
    para = ['^%s' % name]
    cs.execute(sql, para)
    result = cs.fetchall()
    for i in result:
        print(i)
    print("查询完成")
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
