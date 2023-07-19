import flask
from flask import Flask, request, Response
from DbConnection import DBInsert, sql_query, sql_edit
from flask_cors import CORS
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://localhost:5000"])
# Route for seeing a data
@app.route('/', methods=['GET', 'POST', 'PUT'])
def data():
    if request.method == "GET":
        usersQuery = '''SELECT * FROM Person;'''
        users = sql_query(usersQuery)
        print(users)
        list=[]
        for user in users:
            print(user)
            list.append({'id': user["id"], 'name': user["name"], 'email': user["email"]})

        json = {'users': list}

        resp = flask.jsonify(json)
        resp.headers.add('Content-Type', 'application/json')
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        resp.headers.add('Access-Control-Allow-Methods', 'GET')

        return resp
    if request.method == "POST":
        try:
            print(request)
            print(request.json)
            content = request.json
            PersonInsertQuery = '''INSERT INTO Person(name, email) Values(%s,%s);'''
            DBInsert(PersonInsertQuery, (content["name"], content["email"]))

            resp = {}
            resp.headers.add('Content-Type', 'application/json')
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            resp.headers.add('Access-Control-Allow-Methods', 'POST')
            resp.status_code = 200

            return resp
        except Exception as e:
            print(e)
            return Response(status=420)
    if request.method == "PUT":
        try:
            content = request.json
            sql_query('''UPDATE Person SET name=%s, email=%s WHERE Id = %s;''',(content["name"], content["email"], content["Id"]))

            resp = {}
            resp.headers.add('Content-Type', 'application/json')
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            resp.headers.add('Access-Control-Allow-Methods', 'PUT')
            resp.status_code = 200

            return resp
        except:
            return Response(status=420)


# Running app
if __name__ == '__main__':
    app.run(debug=True)

