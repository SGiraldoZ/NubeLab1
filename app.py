import flask
from flask import Flask, request, Response
from DbConnection import DBInsert, sql_query, sql_edit
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/', methods=['GET', 'POST', 'PUT'])
def data():
    print(request)
    if request.method == "GET":
        content = request.json
        usersQuery = '''SELECT * FROM Person;'''
        user = sql_query(usersQuery)

        json = {'id': user["Id"], 'name': user["name"], 'email': user["email"]}

        resp = flask.jsonify(json)
        resp.headers.add('Access-Control-Allow-Origin', '*')

        return resp
    if request.method == "POST":
        try:
            print(request)
            print(request.json)
            content = request.json
            PersonInsertQuery = '''INSERT INTO Person(name, email) Values(%s,%s);'''
            DBInsert(PersonInsertQuery, (content["name"], content["email"]))
            return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=420)
    if request.method == "PUT":
        try:
            content = request.json
            sql_query('''UPDATE Person SET name=%s, email=%s WHERE Id = %s;''',(content["name"], content["email"], content["Id"]))
            return Response(status=200)
        except:
            return Response(status=420)


# Running app
if __name__ == '__main__':
    app.run(debug=True)

