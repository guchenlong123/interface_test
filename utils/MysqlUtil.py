#coding=utf-8
from utils.LogUtil import my_log
import pymysql
import pymssql


# 1、创建封装类
class Mysql:
# 2、初始化数据，连接数据库，光标对象
    def __init__(self,host, user, password, database):
        self.log = my_log()
        self.conn = pymssql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            )
        self.cursor = self.conn.cursor()
# 3、创建查询、执行方法
    def fetchone(self,sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self,sql):
        """
        执行
        :return:
        """
        try:
            if self.conn and self.cursor:
               self.cursor.execute(sql)
               self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

# 4、关闭对象
    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.cursor.close()


# if __name__ == "__main__":
#     mysql = Mysql("192.168.40.234\SQL2012",
#                    "sa",
#                    "iamnts",
#                    "NTS-IOMS",
#                    )
#
#     res = mysql.execute("select campus_code from ioms_role where rolecode = 'administrators' ")
#     print(res)


#1、导入pymysql包
import pymysql
#2、连接database
# conn = pymsql.connect(
#     host = "192.168.40.234\sql2012",
#     user = "sa",
#     password = "iamnts",
#     database = 'NTS-IOMS',
#     )
# #3、获取执行sql的光标对象
# cursor = conn.cursor()
# #4、执行sql
# sql = "select campus_code from dbo.ioms_role where rolecode = 'administrators'"
# # sql1 = "select campus_code from dbo.ioms_role where rolecode = 'administrators'"
# cursor.execute(sql)
# res = cursor.fetchone()
# print(res)
# #5、关闭对象
# cursor.close()
# conn.close()



# 校验数据库是否连接成功
# def conn():
#     connect = pymssql.connect('192.168.40.234\SQL2012', 'sa', 'iamnts', 'NTS-9000')
#     if connect:
#         print("连接成功")
#     return connect
#
#
# if __name__ == "__main__":
#     conn =conn()

