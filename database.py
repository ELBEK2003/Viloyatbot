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

def create_table_category():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists category(
        id integer primary key unique,
        name varchar(125)
        )  
        """)

    conn.commit()



def get_all_categories():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
    select * from category  
    """)

    data=cursor.fetchall()
    return data


# print(get_all_categories())







def add_user(telegram_id,full_name,first_name,phone,viloyat):
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute(f"""
    insert into users(telegram_id, full_name,first_name,phone,viloyat)
    values("{telegram_id}","{full_name}","{first_name}","{phone}","{viloyat}")
    """)
    conn.commit()

def chek_user(telegram_id):
    conn=connect('main.db')
    cursor=conn.cursor()

    cursor.execute(f"""
    select * from users
    where telegram_id={telegram_id}       
    """)
    data=cursor.fetchone()
    if data:
        return True
    else:
        return False

def create_table_product():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists products(
        id integer primary key unique,
        cat_id integer,
        name varchar(125),
        price integer,
        image varchar(125)  
        )  
        """)

    conn.commit()
create_table_product()


def get_products_by_catid(cat_id):
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute(f"""
    select name from category
    where id={cat_id}
    """)
    data=cursor.fetchone()
    return data
# print(get_products_by_catid(2))










