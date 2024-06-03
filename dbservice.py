import psycopg2

# connect to database

conn=psycopg2.connect(
    dbname="myduka",
    user="postgres",
    host="localhost",
    password="johnrommel",
    port=5432,
)

# cursor perform database operations

cur=conn.cursor()

def get_products():
    query="select * from products"
    cur.execute(query)
    products=cur.fetchall()
    print(products)

get_products()

def get_sales():
    query2="select * from sales"
    cur.execute(query2)
    sales=cur.fetchall()
    print(sales)

get_sales()

