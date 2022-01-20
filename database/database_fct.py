import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="/Users/floreac/Downloads/instantclient_19_8")
#import constants

USER="bd149"
PASSWORD="Stef10012000"
DSN="bd-dc.cs.tuiasi.ro:1539/orcl"
ENCODING="UTF-8"

def connect_db():
    connection = cx_Oracle.connect(user=USER,
                                   password=PASSWORD,
                                   dsn=DSN,
                                   encoding=ENCODING)

    return connection


def select_bd(connection, username, password):
    cursor = connection.cursor()

    querry="SELECT id FROM users WHERE username='%s' AND password='%s'" % (username, password)

    ceva=cursor.execute(querry)

    ceva=ceva.fetchone()

    id=ceva[0]

    if(id != 0):
        return id
    else:
        return None


def insert_bd(connection, username, password):
    cursor = connection.cursor()

    querry = "INSERT INTO users VALUES (null,'%s','%s')" % (username, password)

    cursor.execute(querry)

    connection.commit()

