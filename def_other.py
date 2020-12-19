import mariadb
import dbcreds

def getCollection(user_id):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade ,f.lang FROM collection c INNER JOIN food f ON c.food_id = f.food_id INNER JOIN users u ON c.user_id=u.user_id WHERE c.user_id = ?", [user_id])
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

def getGrade(food_id,user_id):
    conn = None
    cursor = None
    rows = None
    try:
        print(food_id)
        print(user_id)
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT grade FROM grade WHERE food_id=? AND user_id=?", [food_id, user_id])
        rows = cursor.fetchone()
        print(rows)
        if rows == None:
            data = 0
        else:
            data = rows[0]
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
        
def getCateLocationTags():
    conn = None
    cursor = None
    data = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        print("a")
        cursor = conn.cursor()
        cursor.execute("SELECT f.food_category , COUNT(*) FROM food f GROUP BY f.food_category ORDER BY 2 DESC")
        category = cursor.fetchall()
        print(category)
        cursor.execute("SELECT f.food_location , COUNT(*) FROM food f GROUP BY f.food_location ORDER BY 2 DESC")
        location = cursor.fetchall()
        print(location)
        data = category + location    
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
        if data != None:
            return data
        
def getOtherTags():
    conn = None
    cursor = None
    data = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        print("a")
        cursor = conn.cursor()
        cursor.execute("SELECT f.tag , COUNT(*) FROM food f GROUP BY f.tag ORDER BY 2 DESC")
        data = cursor.fetchall()   
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
        if data != None:
            return data
        
        
def getCollection(user_id):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade FROM collection c INNER JOIN food f ON c.food_id = f.food_id INNER JOIN users u ON c.user_id=u.user_id WHERE c.user_id = ?", [user_id])
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