import mysql.connector


# crear la conexión

def connect():
    conn = mysql.connector.connect(host="localhost",
                                   database="HandBallCup",
                                   user="HandballApp",
                                   password="handball1234",
                                   port=3306
                                   )
    return conn


def DBInsert(query, var):
    conn = connect()

    cur = conn.cursor()

    cur.execute(query, var)
    conn.commit()
    conn.close()


def sql_query_var(query, var):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, var)
    rows = cur.fetchall()
    conn.close()
    return rows


def sql_query(query):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


# def DBEdit(query, var):

def sql_edit(query, var):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()
    conn.close()


def sql_delete(query, var):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()
    conn.close()