from flask import Flask,render_template,request,url_for,redirect
from dbservice import get_data
from dbservice import insert_products
from dbservice import insert_sales
from datetime import datetime
# create flask instance
app=Flask(__name__)

# first route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products',methods=['GET'])
def products():
    prods=get_data(" products")
    return render_template('products.html',products=prods)
   

@app.route('/sales')
def sales():
    prod=get_data("products")
    sales=get_data("sales")
    return render_template('sales.html',sales=sales,prodducts=prod)
    
    


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/add_product', methods=['POST'])
def add_product_route():
    name = request.form['name']
    buyingprice = float(request.form['buyingprice'])
    sellingprice = float(request.form['sellingprice'])
    quantity = int(request.form['quantity'])

    product = (name, buyingprice, sellingprice, quantity)
    insert_products(product)
    return redirect(url_for('products'))


@app.route('/add_sales',methods=['POST'])
def add_sales_route():
    productid=int(request.form['productid'])
    quantity=int(request.form['quantity'])
    created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sales=(productid,quantity,created_at)
    insert_sales(sales)
    return redirect(url_for('sales'))

# create 3 html files  and ensure 
# all html files are bs enabled
# products.html,sales.html,dashboard.html
# render the html files
# create the dashboard route

app.run(debug=True)




