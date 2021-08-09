from database import db_operations

def get_hotel_byid(id):

    conn,cursor = db_operations.mysql_init()
    sql = "select id,name,address,instruction,phone,star from hotel where id = %s"
    cursor.execute(sql, id)
    result = cursor.fetchone()
    db_operations.mysql_close(conn,cursor)
    return result

def update_by_id(id,name,address,instruction,phone,star):
    conn, cursor = db_operations.mysql_init()
    sql = "update hotel set name = %s,address = %s,instruction = %s,phone = %s,star = %s where id = %s"
    map = {}

    try:
        result = cursor.execute(sql, (name, address, instruction, phone, star, id))
        if result == 1:
            map.update({'desc':'修改成功'})
            map.update({'code':'200'})
        else:
            map.update({'desc': '修改失败'})
            map.update({'code': '404'})
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(e)
        cursor.close()
        conn.close()
    return map

def new_hotel(name,address,instruction,phone,star):
    conn,cursor = db_operations.mysql_init()
    sql = "insert into hotel(name,address,instruction,phone,star) values (%s,%s,%s,%s,%s)"
    map = {}
    lastid = 1
    try:
        result = cursor.execute(sql, (name, address, instruction, phone, star))
        lastid = cursor.lastrowid
        if result==1:
            map.update({'desc': '添加成功'})
            map.update({'code': '200'})
        else:
            map.update({'desc': '添加失败'})
            map.update({'code': '404'})
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(e)
        cursor.close()
        conn.close()
    return lastid,map