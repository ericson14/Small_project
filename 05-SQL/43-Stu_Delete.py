import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="student", charset="utf8")
    cs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "delete from students where name=%s"
    name = input("请输入要删除的学生姓名：")
    para = [name]
    cs.execute(sql, para)
    conn.commit()
    print("删除完成")
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
