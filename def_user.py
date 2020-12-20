import mariadb
import dbcreds
import random
import string
import hashlib
from datetime import datetime

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def login(username, password):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.salt FROM users u WHERE u.username=?", [username, ])
        salt = cursor.fetchone()[0]
        print(salt)
        new_password = salt + password
        hash = hashlib.sha512(new_password.encode()).hexdigest()
        print(hash)
        cursor.execute("SELECT u.user_id FROM users u WHERE u.username=? AND u.password=?", [username, hash])
        user_id = cursor.fetchone()[0]
        if user_id != None:
            token = get_random_alphanumeric_string(50)
            login_time = str(datetime.now())[0:19]
            cursor.execute("INSERT INTO token(user_id, token, login_time) VALUES (?,?,?)", [user_id, token, login_time])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1:
                cursor.execute("SELECT u.username ,u.user_id ,u.email ,u.birthday ,u.bio ,u.join_date ,u.location ,u.icon FROM users u  WHERE user_id=?", [user_id])
                rows = cursor.fetchone()
                users = {}
                headers = [ i[0] for i in cursor.description]
                users = dict(zip(headers,rows))
                users['token'] = token
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
    

def logout(token):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM token WHERE token=?", [token,])
        conn.commit()
        rows = cursor.rowcount
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
        if rows == 1:
            return True
        else:
            return False


def getUsers(user_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        if user_id == None: 
            cursor.execute("SELECT u.username ,u.user_id ,u.email ,u.birthday ,u.bio ,u.join_date ,u.location FROM users u ")
            rows = cursor.fetchall()
            users = []
            headers = [ i[0] for i in cursor.description]
            for row in rows:
                users.append(dict(zip(headers,row)))
            print(users)
        else:
            cursor.execute("SELECT u.username ,u.user_id ,u.email ,u.birthday ,u.bio ,u.join_date ,u.location, u.icon FROM users u  WHERE user_id=?", [user_id])
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
    
def newUsers(username,password,email,birthday,bio,location,icon):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        join_date = str(datetime.now())[0:10]
        salt = get_random_alphanumeric_string(10)
        print(salt)
        new_password = salt + password
        hash = hashlib.sha512(new_password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username,password,email,birthday,bio,location,icon,join_date, salt) VALUES (?,?,?,?,?,?,?,?,?)", [username,hash,email,birthday,bio,location,icon,join_date,salt])
        conn.commit()
        rows = cursor.rowcount
        if rows == 1:
            user = login(username, password)
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
        return user
    
def editUsers(username,password,old_password,email,birthday,bio,location,icon,token):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            user = getUsers(user_id)
            print(user)
            salt = get_random_alphanumeric_string(10)
            print(salt)
            new_password = salt + password
            hash = hashlib.sha512(new_password.encode()).hexdigest()
            print(hash)
            cursor.execute("SELECT u.salt, u.password FROM users u WHERE u.user_id=?", [user_id, ])
            # old_salt = cursor.fetchone()
            # old_new_password = old_salt[0] + old_password
            # old_hash = hashlib.sha512(old_new_password.encode()).hexdigest()
            if username != None and username != "" and username != user['username']:
                cursor.execute("UPDATE users SET username=? WHERE user_id=?",[username, user_id])
                conn.commit()
            if email != None and email != "" and email != user['email']:
                cursor.execute("UPDATE users SET email=? WHERE user_id=?",[email, user_id])
                conn.commit()
            if birthday != None and birthday != "" and birthday != user['birthday']:
                cursor.execute("UPDATE users SET birthday=? WHERE user_id=?",[birthday, user_id])
                conn.commit()
            if bio != None and bio != "" and bio != user['bio']:
                cursor.execute("UPDATE users SET bio=? WHERE user_id=?",[bio, user_id])
                conn.commit()
            if icon != None and icon != "" and icon != user['icon']:
                cursor.execute("UPDATE users SET icon=? WHERE user_id=?",[icon, user_id])
                conn.commit()
            if location != None and location != "" and location != user['location']:
                print(location)
                cursor.execute("UPDATE users SET location=? WHERE user_id=?",[location, user_id])
                conn.commit()
            if password != None and password != "" and hash != old_salt[1]:
                cursor.execute("UPDATE users SET password=? WHERE user_id=? AND password=?",[hash, user_id, old_hash])
                cursor.execute("UPDATE users SET salt=? WHERE user_id=?",[salt, user_id])
                conn.commit()
            rows = cursor.rowcount
            if rows >= 1:
                newuser = getUsers(user_id)
            print(newuser)
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
        return newuser
    
    
def deleteUsers(password,token):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            cursor.execute("SELECT u.salt, u.password FROM users u WHERE u.user_id=?", [user_id,])
            salt = cursor.fetchone()[0]
            print(salt)
            new_password = salt + password
            hash = hashlib.sha512(new_password.encode()).hexdigest()
            cursor.execute("DELETE FROM users WHERE user_id=? AND password=?",[user_id, hash])
            conn.commit()
            rows = cursor.rowcount      
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
        if rows == 1:
            return True
        else:
            return False