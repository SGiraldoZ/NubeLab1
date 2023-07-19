import flask
from flask import Flask, request, Response, make_response
from DbConnection import DBInsert, sql_query, sql_edit
from flask_cors import CORS, cross_origin
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
CORS(app, support_credentials=True)
# Route for seeing a data
@app.route('/', methods=['GET', 'POST', 'PUT'])
@cross_origin(supports_credentials=True)
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
        resp = make_response(flask.jsonify(json))
        resp.headers.add('Access-Control-Allow-Headers', '*')
        resp.headers.add('Access-Control-Allow-Methods', '*')

        return resp
    if request.method == "POST":
        try:
            print(request)
            print(request.json)
            content = request.json
            PersonInsertQuery = '''INSERT INTO Person(name, email) Values(%s,%s);'''
            DBInsert(PersonInsertQuery, (content["name"], content["email"]))

            resp = make_response()
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.headers.add('Access-Control-Allow-Headers', '*')
            resp.headers.add('Access-Control-Allow-Methods', '*')
            resp.status_code = 200

            return resp
        except Exception as e:
            print(e)
            resp = make_response()
            resp.status_code = 420
            return resp

    if request.method == "PUT":
        try:
            content = request.json
            sql_query('''UPDATE Person SET name=%s, email=%s WHERE Id = %s;''',(content["name"], content["email"], content["Id"]))

            resp = make_response()
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.headers.add('Access-Control-Allow-Headers', '*')
            resp.headers.add('Access-Control-Allow-Methods', '*')
            resp.status_code = 200

            return resp
        except:
            resp = make_response()
            resp.status_code = 420
            return resp


# Running app
if __name__ == '__main__':
    app.run(debug=True)

