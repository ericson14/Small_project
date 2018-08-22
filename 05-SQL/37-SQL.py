from pymysql import *


def main():
    conn = connect(host="localhost", port=3306, database="jing_dong", user="root",
                   password="chuanzhi", charset="utf8")
    cs1 = conn.cursor()
    count = cs1.execute("insert into goods_cates(name) VALUES('硬盘')")
    print(count)

    count = cs1.execute("insert into goods_cates(name) VALUES ('光盘')")
    print(count)

    count = cs1.execute("update goods_cates set name='机械硬盘' WHERE NAME='硬盘'")
    print(count)

    cs1.execute("update goods_cates set name='固态硬盘' where id=11")

    count = cs1.execute("select id, name from goods WHERE id>=4")
    print("查询到{}条数据".format(count))
    for i in range(count):
        result = cs1.fetchone()
        print(result)
    result = cs1.fetchall()
    print(result)
    file_name = input("请输入商品名称：")
    paras = file_name
    count = cs1.execute("select name, price from goods where NAME rlike %s", paras)
    print(count)
    result = cs1.fetchall()
    for i in result:
        print(i)
    conn.commit()
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
