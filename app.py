from flask import Flask, request, Response,render_template
import mariadb
import json
import random
from datetime import datetime
from flask_cors import CORS
import os
import def_food
import def_user


app = Flask(__name__)
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/api/users', methods=["GET","POST","PATCH","DELETE"])
def users():
    if request.method == "GET":
        user_id = request.args.get("user_id")
        print(user_id)
        data = def_user.getUsers(user_id)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "POST":
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        birthday = request.json.get('birthday')
        local = request.json.get('local')
        bio = request.json.get('bio')
        icon = request.json.get('icon')
        data = def_user.newUsers(username,password,email,birthday,bio,local,icon)
        if data !=None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "PATCH":
        username = request.json.get('username')
        password = request.json.get('password')
        old_password = request.json.get('old_password')
        email = request.json.get('email')
        birthday = request.json.get('birthday')
        local = request.json.get('local')
        bio = request.json.get('bio')
        icon = request.json.get('icon')
        token = request.json.get('token')
        data = def_user.editUsers(username,password,old_password,email,birthday,bio,local,icon,token)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "DELETE":
        password = request.json.get('password')
        token = request.json.get('token')
        data = def_user.deleteUsers(password,token)
        if data != None:
            return Response("Delete Sucess", mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)

@app.route('/api/login', methods=["POST","DELETE"])
def login():
    if request.method == "POST":
        username = request.json.get('username')
        password = request.json.get('password')
        data = def_user.login(username, password)
        if data !=None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "DELETE":
        token = request.json.get('token')
        if def_user.logout(token):
            return Response("Logout success", mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
        
@app.route('/api/foods', methods=["GET","POST","PATCH","DELETE"])
def food():
    if request.method == "GET":
        user_id = request.args.get("user_id")
        food_id = request.args.get("food_id")
        cooking_way = request.args.get("cooking_way")
        print(user_id)
        if food_id != None:
            data = def_food.getOneFood(food_id)
        elif user_id != None:
            data = def_food.getUserFoods(user_id)
        elif cooking_way != None:
            data = def_food.getCategoryFoods(cooking_way)
        else:
            data = def_food.getAllFoods()
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "POST":
        token = request.json.get('token')
        food_name = request.json.get("food_name")
        food_description = request.json.get("food_description")
        food_local = request.json.get("food_local")
        food_category = request.json.get("food_category")
        cooking_way = request.json.get("cooking_way")
        difficulty = request.json.get("difficulty")
        cooking_time = request.json.get("cooking_time")
        tag = request.json.get("tag")
        images = request.json.get("images")
        data = def_food.newFood(token,food_name,food_description,food_local,food_category,cooking_way,difficulty,cooking_time,tag,images)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "POST":
        token = request.json.get('token')
        food_id = request.json.get("food_id")
        food_name = request.json.get("food_name")
        food_description = request.json.get("food_description")
        food_local = request.json.get("food_local")
        food_category = request.json.get("food_category")
        ingredient = request.json.get("ingredient")
        ingredient_id = request.json.get("ingredient_id")
        ingredient_remark = request.json.get("ingredient_remark")
        process = request.json.get("process")
        process_id = request.json.get("process_id")
        video = request.json.get("video")
        process_remark = request.json.get("process_remark")
        images = request.json.get("images")
        data = def_food.editFood(token,food_id,food_name,food_description,food_local,food_category,ingredient,ingredient_remark,process,video,process_remark,images)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "DELETE":
        token = request.json.get('token')
        food_id = request.json.get("food_id")
        if def_food.deleteFood(token,food_id):
            return Response("Delete success", mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
        
@app.route('/api/methods', methods=["GET","POST","PATCH","DELETE"])
def method():
    if request.method == "GET":
        food_id = request.args.get("food_id")
        data = def_food.getMethod(food_id)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
    if request.method == "POST":
        token = request.json.get('token')
        food_id = request.json.get("food_id")
        ingredient = request.json.get("ingredient")
        process = request.json.get("process")
        remark = request.json.get("remark")
        video = request.json.get("video")
        data = def_food.newMethod(token,food_id,ingredient,process,remark,video)
        if data != None:
            return Response(json.dumps(data, default=str), mimetype="application/json", status=200)
        else:
            return Response("Something went wrong!", mimetype="text/html", status=500)
                         
@app.route('/api/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, '/var/www/homeDelicious/home_delicious_frontend/dist/img/uploadImgs')   
    if not os.path.isdir(target):
        os.mkdir(target)
    files = request.files.getlist("file")
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return Response(json.dumps(destination, default=str), mimetype="application/json", status=204)
if __name__=="__main__":
    app.run(port=4555,debug=True)