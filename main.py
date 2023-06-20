from flask import Flask,render_template
import psycopg2
app = Flask(__name__)


conn = psycopg2.connect(user="postgres", password="444god", host="localhost", port="5432", database="company")

cur=conn.cursor()

@app.route( '/' )
def hello_world():
     name="Moses"
     return render_template('index.html',name=name)

@app.route('/customers')
def customers():
    cur.execute("select * from customers")
    customers=cur.fetchall()
    print(customers)
    return render_template('customers.html',customers=customers)

if __name__== "__main__":
    app.run()