import mariadb
import dbcreds

def SearchFoodListInUser(content, user_id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        word = "%" + content + "%"
        cursor.execute("SELECT DISTINCT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN methods m ON m.food_id= f.food_id INNER JOIN collection c ON c.food_id = f.food_id WHERE f.food_name LIKE ? AND (u.user_id = ? OR c.user_id = ?) OR f.food_description LIKE ? AND (u.user_id = ? OR c.user_id = ?) OR f.food_category LIKE ? AND (u.user_id = ? OR c.user_id = ?) OR f.food_location LIKE ? AND (u.user_id = ? OR c.user_id = ?) OR f.tag LIKE ? AND (u.user_id = ? OR c.user_id = ?) OR m.ingredient LIKE ? AND (u.user_id = ? OR c.user_id = ?) ORDER BY f.food_id DESC", [word,user_id,user_id, word,user_id,user_id, word,user_id,user_id, word,user_id,user_id,word,user_id,user_id,word,user_id,user_id])
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
    
    
def SearchFoodListbyCateLocation(content):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        word = "%" + content + "%"
        cursor.execute("SELECT DISTINCT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id  WHERE f.food_category LIKE ? OR f.food_location LIKE ? ORDER BY f.food_id DESC", [word, word])
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
    
def SearchFoodListbyTag(content):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        word = "%" + content + "%"
        cursor.execute("SELECT DISTINCT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id  WHERE f.tag LIKE ? ORDER BY f.food_id DESC", [word,])
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
    
def SearchFoodListbyContent(content):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        word = "%" + content + "%"
        cursor.execute("SELECT DISTINCT u.user_id ,u.username ,u.birthday ,u.join_date ,u.email ,u.icon ,u.location ,u.bio ,f.food_id ,f.food_name ,f.image ,f.cooking_time ,f.cooking_way ,f.created_at ,f.difficulty ,f.food_category ,f.food_description ,f.food_location ,f.tag,f.grade ,f.lang FROM food f INNER JOIN users u ON f.user_id = u.user_id INNER JOIN methods m ON m.food_id= f.food_id WHERE f.food_name LIKE ? OR f.food_description LIKE ? OR f.food_category LIKE ? OR f.food_location LIKE ? OR f.tag LIKE ? OR m.ingredient LIKE ? ORDER BY f.food_id DESC", [word,word,word,word,word,word,])
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