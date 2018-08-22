import pymysql
import time


def main():
    a = time.time()
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                           database="news", charset="utf8")
    cs = conn.cursor()
    try:
        conn.begin()
        for i in range(100000):
            cs.execute("insert into news(title) values ('News!-%d')" % i)
    except Exception as e:
        print("插入失败", e)
        conn.rollback()
    else:
        print("插入成功")
    finally:
        conn.commit()
        cs.close()
        conn.close()
    b = time.time()
    print(b-a)


if __name__ == '__main__':
    main()
