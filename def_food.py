import mariadb
import dbcreds
from datetime import datetime

def getOneFood(food_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        print(food_id)
        cursor.execute("SELECT u.user_id,u.username ,u.icon ,u.birthday ,u.`local` ,u.bio ,u.join_date ,f.food_id ,f.food_description ,f.food_name ,f.food_local ,f.food_category ,f.created_at ,i.ingredient_id, i.ingredient ,i.ingredient_remark ,mp.process_id, mp.process ,mp.video ,mp.process_remark FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN making_process mp ON f.food_id = mp.food_id INNER JOIN ingredient i ON f.food_id = i.food_id WHERE f.food_id = ?", [food_id,])
        rows = cursor.fetchone()
        print(rows)
        data = {}
        headers = [ i[0] for i in cursor.description]
        data = dict(zip(headers,rows)) 
        cursor.execute("SELECT fi.image_id ,fi.image_url FROM 	food f INNER JOIN food_image fi ON f.food_id = fi.food_id WHERE f.food_id = ?", [food_id])
        rows = cursor.fetchall()
        img=[]
        headers = [ i[0] for i in cursor.description]
        for row in rows:
            img.append(dict(zip(headers,row)))
        data['image'] = img
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
        cursor.execute("SELECT u.user_id,u.username ,u.icon ,u.birthday ,u.`local` ,u.bio ,u.join_date ,f.food_id ,f.food_description ,f.food_name ,f.food_local ,f.food_category ,f.created_at ,i.ingredient_id, i.ingredient ,i.ingredient_remark ,mp.process_id, mp.process ,mp.video ,mp.process_remark FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN making_process mp ON f.food_id = mp.food_id INNER JOIN ingredient i ON f.food_id = i.food_id WHERE f.user_id = ?", [user_id,])
        rows = cursor.fetchall()
        # print(rows)
        data = []
        headers = [ i[0] for i in cursor.description]
        for row in rows:
            food = dict(zip(headers,row)) 
            cursor.execute("SELECT fi.image_id ,fi.image_url FROM 	food f INNER JOIN food_image fi ON f.food_id = fi.food_id WHERE f.food_id = ?", [food['food_id']])
            images = cursor.fetchall()
            img=[]
            imgheaders = [ i[0] for i in cursor.description]
            for image in images:
                img.append(dict(zip(imgheaders,image)))
            food['image'] = img
            data.append(food)
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
    
def getCategoryFoods(food_category):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_id,u.username ,u.icon ,u.birthday ,u.`local` ,u.bio ,u.join_date ,f.food_id ,f.food_description ,f.food_name ,f.food_local ,f.food_category ,f.created_at ,i.ingredient_id, i.ingredient ,i.ingredient_remark ,mp.process_id, mp.process ,mp.video ,mp.process_remark FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN making_process mp ON f.food_id = mp.food_id INNER JOIN ingredient i ON f.food_id = i.food_id WHERE f.food_category = ?", [food_category,])
        rows = cursor.fetchall()
        print("food_category")
        data = []
        headers = [ i[0] for i in cursor.description]
        for row in rows:
            food = dict(zip(headers,row)) 
            cursor.execute("SELECT fi.image_id ,fi.image_url FROM 	food f INNER JOIN food_image fi ON f.food_id = fi.food_id WHERE f.food_id = ?", [food['food_id']])
            images = cursor.fetchall()
            img=[]
            imgheaders = [ i[0] for i in cursor.description]
            for image in images:
                img.append(dict(zip(imgheaders,image)))
            food['image'] = img
            data.append(food)
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
        cursor.execute("SELECT u.user_id,u.username ,u.icon ,u.birthday ,u.`local` ,u.bio ,u.join_date ,f.food_id ,f.food_description ,f.food_name ,f.food_local ,f.food_category ,f.created_at ,i.ingredient_id, i.ingredient ,i.ingredient_remark ,mp.process_id, mp.process ,mp.video ,mp.process_remark FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN making_process mp ON f.food_id = mp.food_id INNER JOIN ingredient i ON f.food_id = i.food_id")
        rows = cursor.fetchall()
        data = []
        headers = [ i[0] for i in cursor.description]
        for row in rows:
            food = dict(zip(headers,row)) 
            cursor.execute("SELECT fi.image_id ,fi.image_url FROM 	food f INNER JOIN food_image fi ON f.food_id = fi.food_id WHERE f.food_id = ?", [food['food_id']])
            images = cursor.fetchall()
            img=[]
            imgheaders = [ i[0] for i in cursor.description]
            for image in images:
                img.append(dict(zip(imgheaders,image)))
            food['image'] = img
            data.append(food)
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
    
def newFood(token,food_name,food_description,food_local,food_category,ingredient,ingredient_remark,process,video,process_remark,images):
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
            cursor.execute("INSERT INTO food(food_name,food_description,food_local,food_category,user_id,created_at) VALUES (?,?,?,?,?,?)",[food_name,food_description,food_local,food_category,user_id,created_at])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1: 
                cursor.execute("SELECT food_id FROM food WHERE food_description=? AND created_at=?", [food_description,created_at])
                food_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO ingredient(ingredient,ingredient_remark,food_id) VALUES (?,?,?)",[ingredient,ingredient_remark,food_id])
                cursor.execute("INSERT INTO making_process(process,video,process_remark,food_id) VALUES (?,?,?,?)",[process,video,process_remark,food_id])
                for image in images:
                    cursor.execute("INSERT INTO food_image(image_url,food_id) VALUES (?,?)",[image,food_id])
                conn.commit()
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
    
def editFood(token,food_id,food_name,food_description,food_local,food_category,ingredient,ingredient_remark,process,video,process_remark,images):
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
            cursor.execute("INSERT INTO food(food_name,food_description,food_local,food_category,user_id,created_at) VALUES (?,?,?,?,?,?)",[food_name,food_description,food_local,food_category,user_id,created_at])
            conn.commit()
            rows = cursor.rowcount
            if rows == 1: 
                cursor.execute("SELECT food_id FROM food WHERE food_descreption=? AND created_at=?", [food_descreption,created_at])
                food_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO ingredient(ingredient,ingredient_remark,food_id) VALUES (?,?,?)",[ingredient,ingredient_remark,food_id])
                cursor.execute("INSERT INTO making_process(process,video,process_remark,food_id) VALUES (?,?,?,?)",[process,video,process_remark,food_id])
                for image in images:
                    cursor.execute("INSERT INTO food_image(image_url,food_id) VALUES (?,?)",[image,food_id])
                conn.commit()
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