import pymysql

def mysql_init():
    conn = pymysql.connect(
        host="localhost",
        user="root", password="root",
        database="hotel",
        charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    return conn, cursor

def mysql_close(conn,cursor):
    conn.close()
    cursor.close()

def get_info(cursor,sql):
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        print("Error: unable to fetch data")