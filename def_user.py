import mariadb
import dbcreds
import random
import string
from datetime import datetime

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def getUsers(user_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        if user_id == None or user_id == "": 
            cursor.execute("SELECT username, id, email, birthdate, bio, url, join_date FROM users")
            rows = cursor.fetchall()
            users = []
            headers = [ i[0] for i in cursor.description]
            for row in rows:
                users.append(dict(zip(headers,row)))
        else:
            cursor.execute("SELECT username, id, email, birthdate, bio, url, join_date FROM users WHERE id=?", [user_id])
            rows = cursor.fetchone()
            users = {}
            headers = [ i[0] for i in cursor.description]
            users = dict(zip(headers,rows))    
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
        return users