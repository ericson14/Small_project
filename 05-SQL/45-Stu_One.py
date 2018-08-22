import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="student", charset="utf8")
    cs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from students where name like %s"
    name = input("请输入要查询的学生姓名：")
    para = [name]
    cs.execute(sql, para)
    result = cs.fetchone()
    print(result)
    print("查询完成")
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
