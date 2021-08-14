from database import db_operations
from database import hotelinfo_db


def get_all_room():
    conn,cursor = db_operations.mysql_init()
    sql = "select id,name,square,price,num,hotelid from room"
    results = db_operations.get_info(cursor,sql)
    db_operations.mysql_close(conn,cursor)
    rooms = []
    room = {}
    for result in results:
        hotel = hotelinfo_db.get_hotel_byid(result[5])
        room = {'id':result[0],'name':result[1],'square':result[2],'price':result[3],'num':result[4],'hotel':hotel.get('name')}
        rooms.append(room)
        room = {}
    print(results)
    return rooms
def get_room_byid(id):

    conn,cursor = db_operations.mysql_init()
    sql = "select id,name,square,price,num,hotelid from room where id = %s"
    cursor.execute(sql, id)
    room = cursor.fetchone()
    result={'id':room[0],'name':room[1],'square':room[2],'price':room[3],'num':room[4]}
    db_operations.mysql_close(conn,cursor)
    return result

def update_by_id(id,name,square,price,num):
    conn, cursor = db_operations.mysql_init()
    sql = "update room set name = %s,square = %s,price = %s,num = %s where id = %s"
    map = {}

    try:
        result = cursor.execute(sql, (name, square, price, num, id))
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