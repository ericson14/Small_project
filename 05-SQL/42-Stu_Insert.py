import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="student", charset="utf8")
    cs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "insert into students(name) values(%s)"
    name = input("请输入要插入的学生姓名：")
    para = [name]
    cs.execute(sql, para)
    conn.commit()
    print("插入完成")
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
