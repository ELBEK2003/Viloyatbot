from sqlite3 import connect

def create_table_users():
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute("""
    create table if not exists users(
    id integer primary key unique,
    telegram_id integer,
    full_name varchar(185),
    first_name varchar(125),
    phone varchar(20),
    viloyat varchar(125)
    )  
    """)
    conn.commit()
create_table_users()









