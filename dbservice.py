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

# def get_products():
#     query="select * from products"
#     cur.execute(query)
#     products=cur.fetchall()
#     print(products)

# get_products()

# def get_sales():
#     query2="select * from sales"
#     cur.execute(query2)
#     sales=cur.fetchall()
#     print(sales)

# get_sales()

def get_data(tablename):
    query=f"select * from {tablename}"
    cur.execute(query,tablename)
    data=cur.fetchall()
    return data
# get_data("select * from products","products")
# get_data("select * from sales","sales")

# insert

def insert_products():
    query="insert into products(name,buyingprice,sellingprice,stockquantity)values('ginger','100','200','80')"
    cur.execute(query)
    conn.commit()
# insert_products()

def insert_sales():
    query="insert into sales(productid,quantity,created_at)values(7,'100',now())"
    cur.execute(query)
    conn.commit()
# insert_sales()

# create 1 function to insert data  to each table 
# the function should be able to insert multiple data 
# it should have parameters 
# insert 2 products and make 4 sales

def insert_products(values):
   
    query = "INSERT INTO products(name, buyingprice, sellingprice,\
    stockquantity)VALUES(%s, %s, %s, %s)"
    cur.execute(query,values)
    conn.commit()
# x=('Ak47', '100', '200', '80')
# insert_products(x)

def insert_sales(values):
    query = "INSERT INTO sales(productid,quantity,\
    created_at)VALUES(%s, %s, %s)"
    cur.execute(query,values)
    conn.commit()
# x=('5', '100', 'now()')
# insert_sales(x)

def sales_product():
    query="SELECT products.name, SUM(products.sellingprice * sales.quantity) FROM products INNER JOIN sales ON products.productid = sales.productid GROUP BY products.name;"
    cur.execute(query)
    data=cur.fetchall()
    
    return data 
# sales_product()


def total_sales():
    query="SELECT sum(products.sellingprice * sales.quantity) FROM public.sales inner join products on products.productid=sales.productid ;"
    cur.execute(query)
    data=cur.fetchall()
    
    return data


def sales_perday():
    query="SELECT sales.created_at, SUM(products.sellingprice * sales.quantity) AS total_sales FROM sales INNER JOIN products ON products.productid = sales.productid GROUP BY sales.created_at ORDER BY sales.created_at;"
    cur.execute(query)
    data=cur.fetchall()
    return data


def sales_today():
    query="SELECT date(sales.created_at), sum(products.sellingprice * sales.quantity) AS profits FROM products inner  JOIN sales  ON products.productid = sales.productid group by sales.created_at order by sales.created_at desc limit 1;"
    cur.execute(query)
    data=cur.fetchall()
    return data


def profit_today():
    query="SELECT date(sales.created_at), sum((products.sellingprice - products.buyingprice)  * sales.quantity) AS profits FROM products inner  JOIN sales  ON products.productid = sales.productid group by sales.created_at order by sales.created_at desc limit 1;"
    cur.execute(query)
    data=cur.fetchall()
    return data




def topselling_product():
    query="SELECT products.name,sum(sales.quantity) from products inner join sales on products.productid=sales.productid group by products.name order by sum(sales.quantity) desc limit 1;"
    cur.execute(query)
    data=cur.fetchall()
    return data

def topprofit_product():
    query="SELECT products.name,sum((products.sellingprice - products.buyingprice)  * sales.quantity) AS profits FROM products inner  JOIN sales  ON products.productid = sales.productid group by Products.name order by sum((products.sellingprice - products.buyingprice)  * sales.quantity) desc limit 1;"
    cur.execute(query)
    data=cur.fetchall()
    return data

def total_profits():
    query="SELECT sum((products.sellingprice - products.buyingprice)  * sales.quantity) AS profits FROM products inner  JOIN sales  ON products.productid = sales.productid;"
    cur.execute(query)
    data=cur.fetchall()
    return data
# task
# 1.write a query to display profit per product psql=>function on dbservice
# 2. write a query to display profit per product psql => function on db
# 3. write a query to display profit per product psql => function on db
def last_10():
    query="SELECT sales.created_at,sum(products.buyingprice*sales.quantity) FROM sales inner join products on products.productid=sales.productid group by sales.created_at order by sales.created_at desc  limit 10;"
    cur.execute(query)
    data=cur.fetchall()
    return data


def profits_products():
    query="SELECT products.name,sum((products.sellingprice - products.buyingprice)  * sales.quantity) AS profits FROM products inner  JOIN sales  ON products.productid = sales.productid group by Products.name ;"
    cur.execute(query)
    data=cur.fetchall()
    return data
# profits_products()

def profits_perday():
    query="SELECT date(sales.created_at) AS SaleDate, SUM((products.sellingprice - products.buyingprice) * sales.quantity) AS Profit FROM products JOIN sales ON products.productid = sales.productid GROUP BY date(sales.created_at) ORDER BY date(Sales.created_at) desc;"
    cur.execute(query)
    data=cur.fetchall()
    return data
# profits_perday()

def insert_users(values):
    query="insert into users (full_name, email, password) values (%s, %s,%s);"
    cur.execute(query,values)
    conn.commit()

def check_email(email):
    query="select * from users where email = %s"
    cur.execute(query,(email,))
    data=cur.fetchall()
    return data

def check_eamil_password(email,password):
    query="select * from users where email =%s and password=%s"
    cur.execute(query,(email,password,))
    data=cur.fetchall()
    return data
