# 1.	Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating 
# (id,name,price, color,image) . 

import psycopg2 as db

conn = db.connect(database="product",
                        user="postgres",
                        password="LevRaven.1",
                        host="localhost",
                        port=5432)

cur = conn.cursor()


table_creation = """
    create table if not exists product(
        id serial PRIMARY KEY,
        name varchar(100) not null,
        price varchar(255) not null,
        color varchar(20),
        image varchar(1000)
    );
"""

cur.execute(table_creation)
conn.commit()


# 2. insert_product, select_all_products, update_product, delete_product nomli funksiyalar yarating

#inserting product
#inserting product
def insert_product():
    insert_product_query = """
        INSERT INTO product (name, price, color, image) VALUES 
        ('coke', '6000', 'black', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPA8ZTZ9k6-Kckk3yrkQjT_5uoOy1a5i4zoq1Me2Ew7A&s'),
        ('fanta', '5000', 'orange', 'https://t0.gstatic.com/images?q=tbn:ANd9GcT7J2lL77_Pf7mEEA_J2x5iMF9Aw84m_595yAf1wXSlJCGx10HM'),
        ('pepsi', '8000', 'purple', 'https://preview.redd.it/pepsi-purple-jaze-v0-td6kiufltq7c1.jpeg?auto=webp&s=3bad5a33f1d37c2762eef399681f6114e70b59e3')
    """
    cur.execute(insert_product_query)
    conn.commit()

#fetching all products
def select_all_products():
    select_all_products_query = "SELECT * FROM product"
    cur.execute(select_all_products_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Test your functions
insert_product()
select_all_products()

#updating products
def update_product():
    update_product_query = """
        UPDATE product SET image = 'https://upload.wikimedia.org/wikipedia/commons/c/c2/Fanta_2023.svg' WHERE name = 'fanta'
    """
    cur.execute(update_product_query)
    conn.commit()

#deleting products
def delete_product():
    delete_product_query = "DELETE FROM product WHERE name = 'pepsi'"
    cur.execute(delete_product_query)
    conn.commit()


#6.	DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga
#ulanish (conn,cur)

class DbConnect:
    def init(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def enter(self):
        self.conn = db.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def exit(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()

with DbConnect('dbname', 'user', 'password') as (conn, cur):
    cur.execute("SELECT * FROM your_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)