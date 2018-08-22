import pymysql


def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="jing_dong", charset="utf8")
    cs1 = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cs1.execute("update goods_cates set name='网线' where id=14")
    cs1.execute("update goods_cates set name='显卡' where id=16")
    cs1.execute("update goods_cates set name='主板' where id=15;")
    conn.commit()
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
