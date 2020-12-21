import mariadb
import dbcreds
from datetime import datetime
import os
# image_path = "/var/www/homeDelicious/home_delicious_frontend/dist/img/uploadImgs/1_food_Seafood-Paella-LEAD-3.jpg"
# if os.path.exists(image_path):
#   os.remove(image_path)
# else:
#   print("The file does not exist")


def getOneFood(food_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        # print(food_id)
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.food_id = ?", [food_id,])
        rows = cursor.fetchone()
        # print(rows)
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
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.user_id = ? ORDER BY f.food_id DESC", [user_id,])
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
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.cooking_way = ? ORDER BY f.food_id DESC", [cooking_way,])
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
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id ORDER BY f.food_id DESC")
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
    
def getAllFoodsByRate():
    conn = None
    cursor = None
    print("all")
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id ORDER BY f.grade DESC LIMIT 5")
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
    
def newFood(token,food_name,food_description,food_location,food_category,cooking_way,difficulty,cooking_time,tag,images,lang):
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
            cursor.execute("INSERT INTO food(food_name,food_description,food_location,food_category,user_id,created_at,cooking_way,difficulty,cooking_time,tag,image,lang) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",[food_name,food_description,food_location,food_category,user_id,created_at,cooking_way,difficulty,cooking_time,tag,images,lang])
            print("aa")
            conn.commit()
            rows = cursor.rowcount
            if rows == 1: 
                cursor.execute("SELECT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag, f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id WHERE f.created_at = ? AND f.image=?", [created_at, images])
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

def editMethod(token,food_id,ingredient,process,remark,video):
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
            if user_id == getOneFood(food_id)['user_id']:
                method = getMethod(food_id)
                if ingredient != None and ingredient != "" and ingredient != method['ingredient']:
                    cursor.execute("UPDATE methods SET ingredient=? WHERE food_id=?",[ingredient, food_id])
                if process != None and process != "" and process != method['process']:
                    cursor.execute("UPDATE methods SET process=? WHERE food_id=?",[process, food_id])
                if remark != None and remark != "" and remark != method['remark']:
                    cursor.execute("UPDATE methods SET remark=? WHERE food_id=?",[remark, food_id])
                if video != None and video != "" and video != method['video']:
                    cursor.execute("UPDATE methods SET video=? WHERE food_id=?",[ingredient, food_id])
                conn.commit()
                rows = cursor.rowcount
                # if rows == 1: 
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
            print(food_id)
            if food_name != None and food_name != "" and food_name != food['food_name']:
                print(food_name)
                cursor.execute("UPDATE food SET food_name=? WHERE food_id=? AND user_id=?", [food_name, food_id, user_id])
                conn.commit()
            if food_description != None and food_description != "" and food_description != food['food_description']:
                cursor.execute("UPDATE food SET food_description=? WHERE food_id=? AND user_id=?", [food_description, food_id, user_id])
                conn.commit()
            if food_location != None and food_location != "" and food_location != food['food_location']:
                cursor.execute("UPDATE food SET food_location=? WHERE food_id=? AND user_id=?", [food_location, food_id, user_id])
                conn.commit()
            if food_category != None and food_category != "" and food_category != food['food_category']:
                cursor.execute("UPDATE food SET food_category=? WHERE food_id=? AND user_id=?", [food_category, food_id, user_id])
                conn.commit()
            if cooking_way != None and cooking_way != "" and cooking_way != food['cooking_way']:
                cursor.execute("UPDATE food SET cooking_way=? WHERE food_id=? AND user_id=?", [cooking_way, food_id, user_id])
                conn.commit()
            if difficulty != None and difficulty != "" and difficulty != food['difficulty']:
                cursor.execute("UPDATE food SET difficulty=? WHERE food_id=? AND user_id=?", [difficulty, food_id, user_id])
                conn.commit()
            if cooking_time != None and cooking_time != "" and cooking_time != food['cooking_time']:
                cursor.execute("UPDATE food SET cooking_time=? WHERE food_id=? AND user_id=?", [cooking_time, food_id, user_id])
                conn.commit()
            if tag != None and tag != "" and tag != food['tag']:
                cursor.execute("UPDATE food SET tag=? WHERE food_id=? AND user_id=?", [tag, food_id, user_id])
                conn.commit()
            if images != None and images != "" and images != food['image']:
                cursor.execute("UPDATE food SET image=? WHERE food_id=? AND user_id=?", [images, food_id, user_id])
                conn.commit()
            rows = cursor.rowcount
            print(rows)
            # if rows >=1: 
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