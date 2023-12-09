from flask import Flask, request,jsonify


from sql_connection import get_sql_connection
import products_dao

connection = get_sql_connection()


app = Flask(__name__)

@app.route('/getProducts')
def hello():
    products =  products_dao.get_all_products(connection)
    print(products)
    response = jsonify(products)
    response.headers.add('Accesss-control-Allow-or-origin','*')
    return response



if __name__=="__main__":
    print("Starting Python Flask Server For Grocery Store System")
    app.run(host='0.0.0.0', debug=True)
    
