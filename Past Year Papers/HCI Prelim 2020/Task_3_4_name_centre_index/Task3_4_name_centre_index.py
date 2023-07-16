from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["post"])
def submit():
    data = request.form
    location = data["location"]
    connection = sqlite3.connect('bakery.db')
    query = '''
    SELECT Name, Type, Price FROM PRODUCT
    WHERE Location=? ORDER BY Price ASC'''
    results = connection.execute(query,(location,))

    products = []
    for product in results:
        name, typ, price = product
        products.append([name, typ, str(price)])

    connection.close()
    return render_template("results.html", location=location, products=products)

if __name__ == '__main__':
    app.run()
