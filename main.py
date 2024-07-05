from flask import Flask,render_template,request,url_for,redirect,flash,session
from dbservice import get_data,profits_products,sales_perday,sales_today,topprofit_product,check_eamil_password
from dbservice import insert_products,total_sales,profits_perday,topselling_product,insert_users
from dbservice import insert_sales,sales_product,total_profits,profit_today,last_10,check_email
from datetime import datetime
# create flask instance
app=Flask(__name__)
app.secret_key = 'NALI'
# first route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products',methods=['GET'])
def products():
    if "email" in session:
        prods=get_data(" products")
    else:
        flash('Please login to access this page','danger')
        return redirect(url_for('login'))
   
    return render_template('products.html',products=prods)
   

@app.route('/sales')
def sales():
    if "email" in session:

        prod=get_data("products")
        sales=get_data("sales")
    else:
        flash('Please login to access this page','danger')
        return redirect(url_for('login'))
    
    return render_template('sales.html',sales=sales,prodducts=prod)
    
    


@app.route('/dashboard')
def dashboard():
        if "email" in session:
            salep=sales_product()
            p_name=[]
            p_sale=[]
            for i in salep:
                p_name.append(i[0])
                p_sale.append(i[1])

            product_name=[]
            profits_prod=[]
            prof=profits_products()
            for i in prof:
                product_name.append(i[0])
                profits_prod.append(i[1])
            prof1=[]
            day1=[]
            day_prof=profits_perday()
            for i in day_prof:
                prof1.append(str(i[0]))
                day1.append(i[1])
            sales1=[]
            date2=[]
            day_persales=sales_perday()
            for i in day_persales:
                sales1.append(str(i[0]))
                date2.append(i[1])
            top_pro=topselling_product()
            tatal_s=total_sales()
            total_p=total_profits()
            today_sales=sales_today()
            top_profit=topprofit_product()
            today_profit=profit_today()
            latest=last_10()
        else:
            flash('Please login to access this page','danger')
            return redirect(url_for('login'))
        return render_template('dashboard.html',p_name=p_name,p_sale=p_sale,tatal_s=tatal_s,product_name=product_name,profits_prod=profits_prod,total_p=total_p,prof1=prof1,day1=day1,sales1=sales1,date2=date2,today_sales=today_sales,top_pro=top_pro,top_profit=top_profit,today_profit=today_profit,latest=latest)



@app.route('/add_product', methods=['POST'])
def add_product_route():
    name = request.form['name']
    buyingprice = float(request.form['buyingprice'])
    sellingprice = float(request.form['sellingprice'])
    quantity = int(request.form['quantity'])

    product = (name, buyingprice, sellingprice, quantity)
    insert_products(product)
    flash('Product added successfully','success')
    return redirect(url_for('products'))


@app.route('/add_sales',methods=['POST'])
def add_sales_route():
    productid=int(request.form['productid'])
    quantity=int(request.form['quantity'])
    created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sales=(productid,quantity,created_at)
    insert_sales(sales)
    flash('Sales added successfully','success')
    return redirect(url_for('sales'))

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
            email=request.form['email']
            password=request.form['password']
            c_mail=check_email(email)
            if len(c_mail)==1:
                cc=check_eamil_password(email,password)
                if len(cc)==1:
                 session['email']=email
                 flash("login successful",'success')
                 return redirect(url_for('dashboard'))
                else:
                    flash("invalid password",'danger')
            else:
                flash("email does not exist please register",'danger')
                return redirect(url_for("register"))
    return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
        if request.method == 'POST':
            full_name = request.form['full_name']
            email = request.form['email']
            password = request.form['password']
            new_user = (full_name, email, password)
            c_email=check_email(email)
            if len(c_email)==0:
                 insert_users(new_user)
                 flash("registered successfully",'success')
                 return redirect(url_for('login'))
            else:
                flash("email already exists",'danger')    
       
           
        return render_template('register.html')



@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect(url_for('login'))

# create 3 html files  and ensure 
# all html files are bs enabled
# products.html,sales.html,dashboard.html
# render the html files
# create the dashboard route

app.run(debug=True)




