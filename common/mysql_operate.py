#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/11 9:56 PM
# @Author: william

import pymysql
from common.yaml_config import GetConf


class MysqlOperate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = str(mysql_conf["password"])
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
                                        port=self.port, charset="utf8")
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("没有获取到数据，表为空")
        else:
            pass
        self.__close_conn()
        return query_data

    def insert_update_table(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close_conn()


# if __name__ == '__main__':
    # select = MysqlOperate()
    # result = select.query("select * from user;")
    # print(result)
    # print(result[0][1])
    # sql = "INSERT INTO `product` VALUES (29, '全心宿舍床垫2，1.2*2，舍友不用了，便宜出', 1, 50.00, '全心宿舍床垫，1.2*2，舍友不用了，便宜出', 'http://47.101.216.239:9090/product/product_img/16574178408375f8f7935-67cb-4749-b320-e6e4c285b607', '', 1, '2022-07-10 09:50:48', '2022-07-10 09:50:48', 13);"
    # MysqlOperate().insert_update_table(sql)
