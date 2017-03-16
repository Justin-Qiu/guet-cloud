#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

# 用户登录函数
def user_log(usr, pwd):
    #连接MySQL数据库
    conn = MySQLdb.connect(
            host='localhost', 
            user='admin', 
            passwd='123456', 
            db='project',
            charset='utf8'
            )
            
    # 创建游标
    cur = conn.cursor()
    
    # SQL查询语句
    sql = "SELECT * FROM users WHERE loginid = '%s'" % usr
    
    # 执行SQL语句
    cur.execute(sql)
    
    # 获取所有记录列表
    results = cur.fetchall()
    for row in results:
        pass_word = row[2]
        if pwd == pass_word:
            name = row[3]
            sex = row[4]
            unitid = row[5]
            title = row[6]
            
            # 性别标识符转中文
            sex = str(sex)
            if sex == '0':
                sex_zh = u'男'
            elif sex == '1':
                sex_zh = u'女'
                
            # 查询所在单位
            sql_unit = "SELECT * FROM unit WHERE id = %d" % unitid
            cur.execute(sql_unit)
            result_unit = cur.fetchall()
            unit_name = result_unit[0][1]
            if unit_name == u'西安电子科技大学':
                area = u'域内'
            else:
                area = u'域外'
            
            # 获取所有文件和权限
            cur.execute("SELECT * FROM files")
            results_files = cur.fetchall()
            files = []
            if title == u'校长':
                colume = 2
            elif title == u'院长':
                colume = 3
            elif title == u'老师':
                colume = 4
            elif title == u'学生':
                colume = 5
            trans = {'R': u'读', 'W': u'写', 'O': u'操作'}
            for row in results_files:
                row[colume]
                auth = u''
                for cha in row[colume]:
                    auth = auth + trans[cha]
                files.append([row[1], auth])
            
            # 返回信息
            return name, sex_zh, unit_name, title, area, files
        else:
            # 口令错误
            return -1
       
    # 用户不存在
    return -2

    # 关闭数据库连接
    conn.close()
