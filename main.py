import psycopg2

host = 'localhost'
db_name = 'teste'
user = 'postgres'
password = '1234'
sslmode = 'required'

str_conn = 'host={0} dbname={1} user={2} password={3}'.format(host, db_name, user, password)

conn = psycopg2.connect(str_conn)
cursor = conn.cursor()


def create(conn, cursor):
    query = ("""
        create table if not exists contatos(
            loginUser varchar(10) primary key,
            password varchar(10),
            nameUser varchar(10),
            access varchar(10),
            phoneNumber varchar(15),
            eMail varchar(30)
            ) 
    """)
    cursor.execute(query)
    conn.commit()


def drop(conn, cursor):
    query = """
        drop table contatos
    """
    cursor.execute(query)
    conn.commit()


def select(cursor):
    query = """
        select * from contatos
    """
    cursor.execute(query)
    return cursor.fetchall()


def selectByName( cursor, login):
    query = """
        select * from contatos where loginUser='{}'
""".format(login)
    cursor.execute(query)
    return cursor.fetchall()


def insert(conn, cursor, loginUser: str, password: str, nameUser: str, access: str, phone: str, eMail: str):
    query = """
        insert into contatos(loginUser, password, nameUser, access, phoneNumber, eMail) values (
        '{}','{}','{}','{}','{}','{}')
    """.format(loginUser, password, nameUser, access, phone, eMail)
    cursor.execute(query)
    conn.commit()


def update(conn, cursor, login_user, password):
    query = """
        update contatos set password='{}' where loginUser='{}'
    """.format(password, login_user)
    cursor.execute(query)
    conn.commit()


def delete(cursor, conn, login_user):
    query = """
        delete from contatos where loginUser = '{}'
    """.format(login_user)
    cursor.execute(query)
    conn.commit()


if __name__ == '__next__':
    create()
    insert('radicore', '1234', 'alisson', 'publico', '(85)996775745', 'emailradi@gmail.com')
    result = select()
    print(result)

#cursor.close()
#conn.close()
