from flask import Flask, Request, Response
from flask_restful import Resource, Api
from methods  import getData
from DbConnection import DBInsert, sql_query
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/', methods=['GET', 'POST'])
def data():
    if Request.method == "GET":
        content = Request.json
        usersQuery = '''SELECT * FROM Coach WHERE id like "''' + content["id"] + '";'
        user = sql_query(usersQuery)

        json = {'id': user["id"], 'name': user["name"], 'Bdate': user["Bdate"]}

        return Response(json, status=200, mimetype='application/json')
    if Request.method == "POST":
        try:
            content = Request.json
            PersonInsertQuery = '''INSERT INTO Person(firstname, Bdate) Values(%s,%s);'''
            DBInsert(PersonInsertQuery, (content["name"], content["Bdate"]))
            return Response(status=200)
        except:
            return Response(status=420)


# Running app
if __name__ == '__main__':
    app.run(debug=True)

