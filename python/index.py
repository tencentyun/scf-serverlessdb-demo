# -*- coding: utf8 -*-
from serverless_db_sdk import database
import random


def main_handler(event, context):
    print('Start Serverlsess DB SDK function')

    # 全流程增删改查测试
    # 连接数据库
    connection = database().connection(autocommit=False)

    # 创建游标
    cursor = connection.cursor()

    table = 'scf_test_%d' % random.randint(1000, 9999)
    # 创建表
    sql = """CREATE TABLE %s (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT )""" % table
    # 执行sql
    cursor.execute(sql)

    # 插入
    sql = """INSERT INTO %s (FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'Mohan', 20, 'M', 2000)""" % table
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        connection.commit()
    except:
        # 出现异常回滚
        connection.rollback()

    # 更新数据
    sql = "UPDATE %s SET AGE = AGE + 1 WHERE SEX = '%c'" % (table, 'M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()

    # 查询
    sql = "SELECT * FROM %s \
           WHERE INCOME > '%d'" % (table, 1000)
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
          fname = row[0]
          lname = row[1]
          age = row[2]
          sex = row[3]
          income = row[4]
          # 打印结果
          print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
    except:
       print("Error: unable to fecth data")

    # 删除测试
    sql = "DELETE FROM %s WHERE AGE > '%d'" % (table, 20)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()

    # 闪表
    sql = "DROP TABLE %s" % table
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()

    # 连接复用测试
    cursor = database().connection().cursor()
    cursor.execute("SELECT * FROM departments LIMIT 100")
    row_1 = cursor.fetchall()
    print(row_1)

    conn = database('DB1').connection(autocommit=False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees LIMIT 10000")
    row_1 = cursor.fetchall()
    conn.commit()
    print(len(row_1))

    cursor = database('DB2').connection().cursor()
    cursor.execute("SELECT NOW();")
    row_2 = cursor.fetchone()
    print(row_2)

    cursor = database('DB2').connection().cursor()
    cursor.execute("SELECT NOW();")
    row_2 = cursor.fetchone()
    print(row_2)

    # 关闭连接测试
    # 连接数据库
    connection = database().connection()

    # 创建游标
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    row_3 = cursor.fetchone()
    print(row_3)
    connection.close()

    # 连接数据库
    connection = database().connection()

    # 创建游标
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    row_3 = cursor.fetchone()
    print(row_3)

    # 连接数据库
    connection = database().connection()

    # 创建游标
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    row_3 = cursor.fetchone()
    print(row_3)
 