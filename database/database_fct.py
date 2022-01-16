import cx_Oracle
import constants

def connect_db():
    connection = cx_Oracle.connect(user=constants.USER,
                                   password=constants.PASSWORD,
                                   dsn=constants.DSN,
                                   encoding=constants.ENCODING)

    return connection


def select_bd(connection, username, password):
    cursor = connection.cursor()

    querry="SELECT id FROM users WHERE username='%s' AND password='%s'" % (username, password)

    ceva=cursor.execute(querry)

    ceva=ceva.fetchone()

    id=ceva[0]

    if(id!=0):
        return id
    else:
        return None


def insert_bd(connection, username, password):
    cursor = connection.cursor()

    querry = "INSERT INTO users VALUES (null,'%s','%s')" % (username, password)

    cursor.execute(querry)

    connection.commit()

