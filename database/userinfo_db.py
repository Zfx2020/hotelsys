from flask import jsonify

from database import db_operations
from utils import psw_processor

def get_all_user():
    conn,cursor = db_operations.mysql_init()
    data = '1234'
    md5psw = psw_processor.to_md5(data)
    sql = "select id,username,password,name,type from user"
    results = db_operations.get_info(cursor,sql)
    db_operations.mysql_close(conn,cursor)
    users = []
    user = {}
    for result in results:
        user = {'id':result[0],'username':result[1],'password':result[2],'name':result[3]}
        users.append(user)
        if(result[2]==md5psw):
            print(result[1],result[0])
        user = {}
    print(results)
    return jsonify(users)

def get_user_byid(id):

    conn,cursor = db_operations.mysql_init()
    sql = "select id,username,password,name,phone from user where id = %s"
    cursor.execute(sql, id)
    result = cursor.fetchone()
    db_operations.mysql_close(conn,cursor)
    return result

def admin_login(username,psw):
    map = {}
    conn, cursor = db_operations.mysql_init()
    md5psw = psw_processor.to_md5(psw)
    sql = "select id,username,name,password,type from user where username = %s and password = %s"
    cursor.execute(sql, (username, md5psw))
    result = cursor.fetchone()
    print(result)
    if(len(result)>0):
        map.update({'status':'登录成功','code':200})
        map.update({'user':result})
    else:
        map.update({'status': '登录失败', 'code': 404})
    return jsonify(map)

def new_hotel_admin(psw,name,phone):
    conn,cursor = db_operations.mysql_init()
    sql = "insert into user(username, password, name, phone, state, type) values ('酒店管理员',%s,%s,%s,1,2)"
    map = {}
    lastid = 1
    try:
        result = cursor.execute(sql, (psw, name, phone))
        lastid = cursor.lastrowid
        if result == 1:
            map.update({'desc': '注册成功'})
            map.update({'code': '200'})
        else:
            map.update({'desc': '注册失败'})
            map.update({'code': '404'})
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(e)
        cursor.close()
        conn.close()
    return lastid, map
