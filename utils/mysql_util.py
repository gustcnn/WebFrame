# --*--coding:utf-8
# Author:cnn
import pymysql


class ConnMysql(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="root", database="stock_db", charset="utf8")
        self.cursor = self.conn.cursor()

    def execute_myql(self, sql):
        """执行查询"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    conn = ConnMysql()
    result = conn.execute_myql("select *from focus")
    print(result)
