from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
import pickle
sc = pickle.load(open('/Users/simrandeepsingh/ADT/scaler.pkl', 'rb'))
lr = pickle.load(open('/Users/simrandeepsingh/ADT/predictHousePrice.pkl', 'rb'))
app = Flask(__name__)
@app.route("/")
def home():
    return open('/Users/simrandeepsingh/ADT/predictprice.html').read() #  read html file 
@app.route("/index")
@app.route("/backgroud")
def img():
    return open("/Users/simrandeepsingh/ADT/housepriceimage.jpeg").read()
@app.route('/predict', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'POST':
        bedrooms = float(request.form['Bedrooms'])
        bathrooms = float(request.form['Bathrooms'])
        sqft_living = float(request.form['Sqrft_liv'])
        sqft_lot=float(request.form['Sqrft_lot'])
        floors = float(request.form['Floors'])
        yr_built = float(request.form['yr_built'])
        condition = float(request.form['condition'])
        waterfront = float(request.form['waterfront'])
        yr_reno = float(request.form['yr_renov'])

        house=[[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, condition, yr_built, yr_reno]]

        house = sc.transform(house)
        ab = lr.predict(house)

        result = "The Predicted House Price is "+ str(round(ab[0],2)) +" thousand dollars."
        resp = make_response(result)
        resp.headers['Content-Type'] = "text/html"
        resp.headers['Access-Control-Allow-Origin'] = "*"
        return resp
if __name__ == "__main__":
    app.run(debug = True)
