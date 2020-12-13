import mariadb
import dbcreds

def addCollection(token,food_id):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            cursor.execute("INSERT INTO collection(user_id, food_id) VALUES (?,?)", [user_id, food_id])
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
              
def deleteCollection(token,food_id):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            cursor.execute("DELETE FROM collection WHERE user_id=? AND food_id=?", [user_id, food_id])
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
        
def addGrade(token,food_id,grade):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            cursor.execute("INSERT INTO grade(user_id, food_id, grade) VALUES (?,?,?)", [user_id, food_id,grade])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1:
                cursor.execute("SELECT AVG(g.grade) FROM grade g WHERE g.food_id=?", [food_id,])
                average_grade = round(cursor.fetchone()[0],1)
                print(average_grade)
                cursor.execute("UPDATE food SET grade=? WHERE food_id=?", [average_grade, food_id])
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
            return average_grade
        
def editGrade(token,food_id,grade):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        print(user_id)
        if user_id != None:
            cursor.execute("UPDATE grade SET grade=? WHERE food_id=? AND user_id=?", [grade, food_id, user_id])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1:
                cursor.execute("SELECT AVG(g.grade) FROM grade g WHERE g.food_id=?", [food_id,])
                average_grade = round(cursor.fetchone()[0],1)
                print(average_grade)
                cursor.execute("UPDATE food SET grade=? WHERE food_id=?", [average_grade, food_id])
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
            return average_grade