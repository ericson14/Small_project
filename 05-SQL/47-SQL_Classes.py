import pymysql


class ClassesSQL(object):
    def __init__(self):
        """连接数据库，返回游标和连接对象"""
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", password="chuanzhi",
                                    database="student", charset="utf8")
        self.cs = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):
        self.cs.close()
        self.conn.close()

    def select(self):
        """查询指定班级或全部班级信息"""
        name = input("请输入要查询的班级信息（按回车查询全部）：")
        if name:
            sql = "select * from classes where name rlike %s"
            ex = self.cs.execute(sql, [name])
        else:
            sql = "select * from classes"
            ex = self.cs.execute(sql)
        if ex == 0:
            print("没有获得结果。。")
        else:
            print("获得了{}组数据".format(ex))
        for i in self.cs.fetchall():
            print(i)
        print("查询完成")

    def insert(self):
        """插入新班级"""
        sql = "insert into classes(name) values(%s)"
        name = input("请输入要插入的班级：")
        ex = self.cs.execute("select * from classes where name=%s", [name])
        if ex:
            print("已经存在该班级。。。")
            return
        self.cs.execute(sql, [name])
        self.conn.commit()
        if self.cs.rowcount == 1:
            print("插入完成")
        else:
            print("插入失败")

    def update(self):
        """按照编号或者名字修改班级信息"""
        flag = input("修改班级信息，请输入查询信息，按1输入名字，按2输入编号，按其余键退出")
        if flag == "1":
            sql = "update classes set name=%s where name=%s"
            name = input("请输入要修改的班级名字：")
            new_name = input("请输入修改后的班级名字：")
            self.cs.execute(sql, [new_name, name])
            self.conn.commit()
            if self.cs.rowcount == 1:
                print("修改完成")
            else:
                print("修改失败")
        elif flag == "2":
            sql = "update classes set name=%s where id=%s"
            cid = input("请输入要修改的班级编号：")
            new_name = input("请输入修改后的班级名字：")
            self.cs.execute(sql, [new_name, cid])
            self.conn.commit()
            if self.cs.rowcount == 1:
                print("修改完成")
            else:
                print("修改失败")
        else:
            return

    def delete(self):
        """按照编号或者班级名称逻辑删除班级"""
        flag = input("删除班级信息，请输入查询信息，按1输入名字，按2输入编号，按其余键退出")
        if flag == "1":
            sql = "update classes set is_delete=1 where name=%s"
            name = input("请输入要删除的班级名称：")
            self.cs.execute(sql, [name])
            self.conn.commit()
            if self.cs.rowcount == 1:
                print("删除完成")
            else:
                print("删除失败")
        elif flag == "2":
            sql = "update classes set is_delete=1 where id=%s"
            name = input("请输入要删除的班级编号：")
            self.cs.execute(sql, [name])
            self.conn.commit()
            if self.cs.rowcount == 1:
                print("删除完成")
            else:
                print("插入失败")
        else:
            return

    def start(self):
        while True:
            self.menu()
            flag = input("请输入要做的事情：")
            if flag == "1":
                self.select()
            elif flag == "2":
                self.insert()
            elif flag == "3":
                self.update()
            elif flag == "4":
                self.delete()
            elif flag == "5":
                print("下次再见！")
                break
            else:
                print("输入错误，请重新输入。。。")

    @staticmethod
    def menu():
        print("*" * 50)
        print("1.查询，2.插入，3.修改，4.删除，5.退出")
        print("*" * 50)


if __name__ == '__main__':
    c = ClassesSQL()
    c.start()
