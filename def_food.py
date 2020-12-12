import mariadb
import dbcreds
from datetime import datetime
import os
# if os.path.exists("C:/Users/Taylo/InnoTech/Assignments/Project/Home delicious/home_delicious_frontend/users_food_004.jpg"):
#   os.remove("C:/Users/Taylo/InnoTech/Assignments/Project/Home delicious/home_delicious_frontend/users_food_004.jpg")
# else:
#   print("The file does not exist")


def getOneFood(food_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        print(food_id)
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.food_id = ?", [food_id,])
        rows = cursor.fetchone()
        print(rows)
        data = {}
        headers = [ i[0] for i in cursor.description]
        data = dict(zip(headers,rows)) 
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
    
def getMethod(food_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        print(food_id)
        cursor.execute("SELECT * FROM methods m WHERE m.food_id = ?", [food_id,])
        rows = cursor.fetchone()
        print(rows)
        data = {}
        headers = [ i[0] for i in cursor.description]
        data = dict(zip(headers,rows)) 
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
    
def getUserFoods(user_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.user_id = ? ORDER BY f.food_id DESC", [user_id,])
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
    
def getCategoryFoods(cooking_way):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.cooking_way = ? ORDER BY f.food_id DESC", [cooking_way,])
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
    
def getAllFoods():
    conn = None
    cursor = None
    print("all")
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade FROM food f INNER JOIN users u ON f.user_id = u.user_id ORDER BY f.food_id DESC")
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
    
def newFood(token,food_name,food_description,food_location,food_category,cooking_way,difficulty,cooking_time,tag,images):
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
            created_at = str(datetime.now())[0:19]
            cursor.execute("INSERT INTO food(food_name,food_description,food_location,food_category,user_id,created_at,cooking_way,difficulty,cooking_time,tag,image) VALUES (?,?,?,?,?,?,?,?,?,?,?)",[food_name,food_description,food_location,food_category,user_id,created_at,cooking_way,difficulty,cooking_time,tag,images])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1: 
                cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.created_at = ? AND f.image=?", [created_at, images])
                rows = cursor.fetchone()
                print(rows)
                data = {}
                headers = [ i[0] for i in cursor.description]
                data = dict(zip(headers,rows)) 
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
    
def newMethod(token,food_id,ingredient,process,remark,video):
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
            created_at = str(datetime.now())[0:19]
            cursor.execute("INSERT INTO methods(food_id,ingredient,process,remark,video) VALUES (?,?,?,?,?)",[food_id,ingredient,process,remark,video])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1: 
                data = getMethod(food_id)           
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
    
def editFood(token,food_id,food_name,food_description,food_location,food_category,cooking_way,difficulty,cooking_time,tag,images):
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
            food = getOneFood(food_id)
            print(food)
            if food_name != None and food_name != "" and food_name != food.food_name:
                cursor.execute("UPDATE food SET food_name=? WHERE food_id=? AND user_id=?", [food_name, food_id, user_id])
                conn.commit
                rows = cursor.rowcount
                if rows == 1: 
                    data = getOneFood(food_id)       
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
    
def deleteFood(token, food_id):
    conn = None
    cursor = None
    rows = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM token WHERE token=?", [token,])
        user_id = cursor.fetchone()[0]
        if user_id != None:
            cursor.execute("DELETE FROM food WHERE food_id=? AND user_id=?",[food_id, user_id])
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