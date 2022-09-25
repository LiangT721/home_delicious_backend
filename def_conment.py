import mariadb
import dbcreds
from datetime import datetime


def getComments(food_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        print(food_id)
        cursor.execute("SELECT u.username ,u.user_id ,u.icon ,c.comment_id ,c.content ,c.date_time ,c.images FROM comments c INNER JOIN users u ON c.user_id = u.user_id WHERE c.food_id=? ORDER BY c.comment_id DESC ", [food_id,])
        rows = cursor.fetchall()
        data = []
        headers = [ i[0] for i in cursor.description]
        for row in rows:
            data.append(dict(zip(headers,row)))
    except mariadb.ProgrammingError:
        print("program error...")
    except mariadb.DataError:
        print("Data error...")
    except mariadb.DatabaseError:
        print("Database error...")
    except mariadb.OperationalError:
        print("connect error...")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
        return data
    
def create_comment(food_id,token,content,images):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        if user_id != None:
            created_at = str(datetime.now())[0:19]
            cursor.execute("INSERT INTO comments(food_id, user_id, content, images, date_time) VALUES (?,?,?,?,?)", [food_id, user_id, content, images, created_at])
            print("aa")
            conn.commit()
            rows = cursor.rowcount
            print(rows)
            if rows == 1:
                cursor.execute("SELECT u.username ,u.user_id ,u.icon ,c.comment_id ,c.content ,c.date_time ,c.images FROM comments c INNER JOIN users u ON c.user_id = u.user_id WHERE c.content=? AND c.date_time=? ", [content, created_at])
                row = cursor.fetchone()
                data = {}
                headers = [ i[0] for i in cursor.description]
                data = dict(zip(headers,rows)) 
                print(data)
    except mariadb.ProgrammingError:
        print("program error...")
    except mariadb.DataError:
        print("Data error...")
    except mariadb.DatabaseError:
        print("Database error...")
    except mariadb.OperationalError:
        print("connect error...")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
        return data