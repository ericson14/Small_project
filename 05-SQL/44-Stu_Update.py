import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="student", charset="utf8")
    cs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "update students set name=%s where name=%s"
    name = input("请输入要修改的学生姓名：")
    new_name = input("请输入修改后的名字：")
    para = [new_name, name]
    cs.execute(sql, para)
    conn.commit()
    print("修改完成")
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
